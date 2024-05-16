import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class TFIDFProcess:
    def build_recommended_places(self, recommended_places, visited_places):
        df = self.clean_data(pd.DataFrame(recommended_places))
        user_df = pd.DataFrame(visited_places)
        data = self.build_similarity(df, user_df)
        recommended = self.get_recommended(df, data)
        return recommended

    def clean_data(self, df):
        df = df.drop_duplicates(keep="last")
        df = df.dropna(axis=0)
        df["Type"] = df["Type"].str.replace("_", " ")

        return df

    def build_similarity(self, df, user_df):
        # FS DataFrame => Recommended Places
        df["TextData"] = (
            df["Type"] + " " + df["Reviews"]
        )
        #  User data => User selected trips
        user_df["TextData"] = (
            user_df["Type"]
            + " "
            + user_df["Reviews"]
        )
        # Create the TF-IDF vectorizer
        tfidf = TfidfVectorizer(stop_words="english", token_pattern=r"\b[a-zA-Z0-9]+\b")
        # Compute the TF-IDF matrix
        # This will use TF-IDF vectorizer to tfidf matrix
        tfidf_matrix = tfidf.fit_transform(df["TextData"])
        # This will use the same vocabulary and transform the user data based on tfidf_matrix learning
        tfidf_matrix_user = tfidf.transform(user_df["TextData"])
        data = dict()
        # i = => one loop will loop for inner loop 1000 times
        for idx_user, user_row in enumerate(tfidf_matrix_user):
            sim_result = list()
            for idx, row in enumerate(tfidf_matrix):
                cosine_sim = cosine_similarity(row, user_row)
                sim_result.append({idx: cosine_sim[0, 0]})
            # Sort the sim_result to get the top similarity records
            sim_result = sorted(
                sim_result, key=lambda x: list(x.values())[0], reverse=True
            )
            # each place will has array with all recommended records => records will be dict type with key and value
            data[idx_user] = sim_result
        return data

    def get_recommended(self, df, data):
        unique_places = list()
        recommendations = list()
        places_indices = list()
        # user data
        for key, value in data.items():
            # loop sim places
            for item in value:
                # item dict
                for k, v in item.items():
                    places_indices.append(k)

        recommended_places = df.iloc[places_indices].to_dict(orient="records")
        for recommend_place in recommended_places:
            if recommend_place["Name"] not in unique_places:
                unique_places.append(recommend_place["Name"])
                data = dict()
                data["Name"] = recommend_place["Name"]
                data["Address"] = recommend_place["Address"]
                data["Type"] = recommend_place["Type"].split(',')
                data["Rating"] = recommend_place["Rating"]
                # data["Description"] = recommend_place["Description"]
                data["Reviews"] = recommend_place["Reviews"]
                recommendations.append(data)
                if len(recommendations) >= 5:
                    break
        return recommendations
