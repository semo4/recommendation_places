# Flask is a web framework for creating web applications and APIs in Python.
# jsonify is a helper function to convert Python dictionaries to JSON format.
from flask import Flask, jsonify

# ProcessData is Class to build the process tha will fetch the data from FS and build the recommended data
from src.controllers.process import ProcessData

# app is an instance of the Flask class.
app = Flask(__name__)

# secret_key Used in flask to sign Cookies to application.
# This is important for security for the web application.
app.secret_key = "frY^eN&UB4yZgVt+Isbjq%deH"


# This is the route for recommended_places API that takes the user Id and returns the Recommended.
# This will be the start point for the system That will use the ProcessData class and it will call the recommended_places to build the Recommended places for our system.
# This will use jsonify to build the JSON response.
# If the process failed it will return an Exception with the error.
@app.route("/recommended_places/<user_id>")
def get_recommended_places(user_id):
    try:
        result = ProcessData().recommended_places(user_id)
        return jsonify(result)
    except Exception as e:
        res = {"status": 500, "error": f"Error Occur {e}"}
        return jsonify(res)


# This block will ensure that the flask app will only run for root file.
if __name__ == "__main__":
    # This instance is the WSGI application
    app.run(debug=True)
