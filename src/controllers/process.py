from src.cloud.gcp import GCPCloud
from src.helpers.tf_idf import TFIDFProcess

# ProcessData
# In this class we will get the data from FS and build the recommended

# recommended_places
# This function will takes the user id from the API and get the user data from FS.
# Then get the trips that exist in user data.
# Loop over the trips and get the Destinations for each trip.
# Then get the visited places from Destinations and append it to unique list to ensure the places will be only unique.
# Then will build the recommended places.

# Map_place
# This function will map the data from FS to new object that ca use in our system.

# extract_data
# Revert the data to same status that come from FS to return it as the user need.

# get_all_places
# Get all destinations from FS and map it to new object so we can use it to build our recommended places


class ProcessData:
    def __init__(self):
        self.fs_client = GCPCloud()

    def recommended_places(self, user_id):
        # Get user Data from FS (Firestore)
        user_data = self.fs_client.get_user_data(user_id)
        # Extract Trip Id's from User data
        trips = user_data["tripsIds"]
        trip_dict = dict()
        # Loop over trip Id's
        for trip in trips:
            visit_places = list()
            unique_visited_places = list()
            # Get Trip Data from FS
            trip_data = self.fs_client.get_trip_data(trip)
            # Extract Destination Id's from trip
            for des_id in trip_data["destinationsIds"]:
                # Get Destinations Data fromFS
                destination_data = self.fs_client.get_destination_data(des_id)
                # Extract visitedPlaces from Destinations
                for place in destination_data["visitedPlaces"]:
                    visit_places.append(place)
                    unique_visited_places.append(place["name"])
            trip_dict[trip_data["name"]] = dict()
            if len(visit_places) > 0:
                trip_dict_res = self.Map_place(visit_places)
                # Get All destinations data from FS
                destination_places = self.get_all_places(unique_visited_places)
                # Send Destinations data and User Visited Places Data to build the new recommended places
                # The Result will contains all recommended places for the User
                recommend_result = TFIDFProcess().build_recommended_places(
                    destination_places, trip_dict_res
                )
                trip_dict[trip_data["name"]]["visited_places"] = self.extract_data(
                    trip_dict_res
                )
                trip_dict[trip_data["name"]]["recommended_places"] = recommend_result
            else:
                empty_trip = dict()
                empty_trip["message"] = (
                    "This Trip doesn't contains any Recommended Places"
                )
                trip_dict[trip_data["name"]]["recommended_places"] = empty_trip
        return trip_dict

    def Map_place(self, places):
        places_data = list()
        for place in places:
            place_dict = dict()
            place_dict["Name"] = place["name"]
            place_dict["Address"] = place["address"]
            place_dict["Type"] = ",".join(place["types"])
            place_dict["Rating"] = place["rating"] if place["rating"] else 0
            reviews_list = list()
            if "reviews" in place.keys() and place["reviews"] is not None:
                for review in place["reviews"]:
                    reviews_list.append(review)
            place_dict["Reviews"] = (
                ",,".join(reviews_list) if len(reviews_list) > 0 else ""
            )
            place_dict["Description"] = place["description"]
            place_dict["PriceLevel"] = place["priceLevel"]
            place_dict["VisitDate"] = place["visitDate"]
            place_dict["pId"] = place["pId"]
            place_dict["lng"] = place["lng"]
            place_dict["isFav"] = place["isFav"]
            place_dict["lat"] = place["lat"]
            place_dict["imageUrls"] = ",,".join(place["imageUrls"])
            places_data.append(place_dict)
        return places_data

    def extract_data(self, places):
        places_data = list()
        for place in places:
            place_dict = dict()
            place_dict["Name"] = place["Name"]
            place_dict["Address"] = place["Address"]
            place_dict["Type"] = place["Type"].split(",")
            place_dict["Rating"] = place["Rating"]
            place_dict["Reviews"] = place["Reviews"].split(",,")
            place_dict["Description"] = place["Description"]
            place_dict["PriceLevel"] = place["PriceLevel"]
            place_dict["VisitDate"] = place["VisitDate"]
            place_dict["pId"] = place["pId"]
            place_dict["lng"] = place["lng"]
            place_dict["isFav"] = place["isFav"]
            place_dict["lat"] = place["lat"]
            place_dict["imageUrls"] = place["imageUrls"].split(",,")
            places_data.append(place_dict)
        return places_data

    def get_all_places(self, unique_visited_places):
        places_data = self.fs_client.get_destinations()
        visited_places = list()
        for desc in places_data:
            for visited in desc["visitedPlaces"]:
                if visited["name"] not in unique_visited_places:
                    visited_places.append(visited)
        places_res = self.Map_place(visited_places)
        return places_res
