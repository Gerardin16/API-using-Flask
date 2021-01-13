import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some family data in the form of a list of dictionaries.
family = [
    {'id': 0,
     'name': 'Gerardin Niveadhana',
     'age': '34',
     'DOB': '16-09-1986'},
    {'id': 1,
     'name': 'Loyola Stalin',
     'age': '40',
     'DOB': '03-09-1980'},
    {'id': 2,
     'name': 'Jerwin Joseph',
     'age': '6',
     'DOB': '03-03-2015'},
    {'id': 3,
     'name': 'Jeffrin Stalin',
     'age': '2',
     'DOB': '30-01-2019'}
]


# A route to display Home page
@app.route('/', methods=['GET'])
def homepage():
    return '<h1>Family Records</h1>'


@app.route('/details', methods=['GET'])
def get_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for person in family:
        if person['id'] == id:
            results.append(person)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()