import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# TF-IDF (Term Frequency-Inverse Document Frequency)
# We use this algorithm because this will help use to weights the terms such commons words.
# It helps in search engine to ranking documents based on their relevance to the search query and for this reason we use it.
# It provides a strong baseline performance for many text mining.
# It will helps in reducing noise in the data.
# Why we choose TF-IDF because Document Similarity (such as clustering similar documents or retrieving similar documents from the data you provided).

# cosine_similarity
# We will use it to measure the similarity in two vectors
# Cosine Similarity range from -1 to 1
#  1 => this mean the text identical
#  0 => this mean the text orthogonal (no similarity).
# -1 => this mean the text diametrically opposed (completely dissimilar)
# It will generate array with all similarity result from the documents.

# Why we use the cosine_similarity
# It help to text analysis to measure similarity between documents.
# Making it suitable for large dataset.
# Build recommender system base on user preferences (in our system user visited places).
# SO the cosine_similarity is a powerful tool to determining the similarity between documents.

# TFIDFProcess CLass
# This class will build the process to get the Recommended places from the Data and user Data.


# build_recommended_places
# This function will build the whole system for use and returns the response.
# It will takes the places Data and user Data.
# This will clean the data first.
# Then will create new DataFrame from user data.
# After this it will build the similarity from the places data and user data.
# Finally build the recommended data from the similarity data that we build.

# clean_data
# It will clean the data from any duplicates data and any NaN values from the records.
# This will returns new DataFrame with the clean data.

# build_similarity
# This will build the TextData from Type and Reviews to use it in similarity build.
# Use TfidfVectorizer to defined the vectorizer.
# Then use the tfidf to fit_transform the data.
# Use transform to fit the user data using the same vocabulary from fit_transform.
# Then will loop over the user data to build the similarity from all places data.
# return the similarity array for each visited place in user data.

# get_recommended
# This function will help to map and build the recommended data from similarity result.

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
        df["TextData"] = df["Type"] + " " + df["Reviews"]
        #  User data => User selected trips
        user_df["TextData"] = user_df["Type"] + " " + user_df["Reviews"]
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
                data["Type"] = recommend_place["Type"].split(",")
                data["Rating"] = recommend_place["Rating"]
                # data["Description"] = recommend_place["Description"]
                data["Reviews"] = recommend_place["Reviews"].split(",,")
                data["Description"] = recommend_place["Description"]
                data["PriceLevel"] = recommend_place["PriceLevel"]
                data["VisitDate"] = recommend_place["VisitDate"]
                data["pId"] = recommend_place["pId"]
                data["lng"] = recommend_place["lng"]
                data["isFav"] = recommend_place["isFav"]
                data["lat"] = recommend_place["lat"]
                data["imageUrls"] = recommend_place["imageUrls"].split(",,")
                recommendations.append(data)
                if len(recommendations) >= 5:
                    break
        return recommendations
