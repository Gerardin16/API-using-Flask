import flask
from flask import jsonify

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


# A route to return all of the available entries in our family section.
@app.route('/family/api/v1/details', methods=['GET'])
def get_details():
    return jsonify(family)


# Curl command to get all data
# $ curl -i http://localhost:5000/family/api/v1/details


if __name__ == '__main__':
    app.run()