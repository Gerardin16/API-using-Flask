import flask
from flask import  jsonify,abort,make_response

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

@app.route('/family/api/v1/details/<int:p_id>', methods=['GET'])
def get_person(p_id):
    person = [person for person in family if person['id'] == p_id]
    #  If no ID is provided, display an error in the browser.
    if len(person) == 0:
        abort(404)
    # If ID is provided,return the result.
    return jsonify(person[0])


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run()
