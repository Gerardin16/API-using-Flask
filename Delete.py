import flask
from flask import request,abort,make_response,jsonify



app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some family data in the form of a list of dictionaries.
family = [
    {'id': 0,
     'name': 'Gerardin Niveadhana',
     'age': 34,
     'DOB': '16-09-1986'},
    {'id': 1,
     'name': 'Loyola Stalin',
     'age': 40,
     'DOB': '03-09-1980'},
    {'id': 2,
     'name': 'Jerwin Joseph',
     'age': 6,
     'DOB': '03-03-2015'},
    {'id': 3,
     'name': 'Jeffrin Stalin',
     'age': 2,
     'DOB': '30-01-2019'}
]


# A route to display Home page
@app.route('/', methods=['GET'])
def homepage():
    return '<h1>Family Records</h1>'

# A route to delete a record based on the id given
@app.route('/family/api/v1/details/<int:p_id>', methods=['DELETE'])
def delete_record(p_id):
    person = [person for person in family if person['id'] == p_id]
    if len(person) == 0:
        abort(404)
    family.remove(person[0])
    return jsonify({'result': True})

# A route to check the records again
@app.route('/family/api/v1/details', methods=['GET'])
def get_details():
    return jsonify(family)

# A error handler to handle when the id is not found
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# Curl command to delete a record
# curl -i -H "Content-Type: application/json" -X DELETE  http://localhost:5000/family/api/v1/details/1


if __name__ == '__main__':
    app.run()