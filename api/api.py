# done with help from 
# https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

import flask
from flask import request, jsonify
from FollowerIdApi import query_followers, validAlphaNumOrHyphen

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Follower List</h1>\
    <p>This site is a prototype API to return followers based on a \
    particular user (up to 3 levels deep).</p>"

# A route to return followers.
@app.route('/api/v1/resources/followers', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        userId = str(request.args['id'])
        if(not validAlphaNumOrHyphen(userId)):
            return "The username entered was not valid (or not present). \
            The username must be alpha-numeric characters"
    else:
        return "Error: No user ID provided. Please specify an id."

    if 'maxFollowers' in request.args:
        if(int(request.args['maxFollowers']) <= 5):
            maxFollowers = int(request.args['maxFollowers'])
    else:
        maxFollowers = 5

    # Create an empty list for our results
    results = query_followers(userId, maxFollowers)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


app.run()