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


@app.route('/family/api/v1/details', methods=['POST'])
def create_record():
    if not request.json or not 'name' in request.json:
        abort(400)
    person = {
        'id': family[-1]['id'] + 1,
        'name': request.json['name'],
        'age': request.json['age'],
        'DOB': request.json.get('DOB', "")
    }
    family.append(person)
    return jsonify(person), 201

    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



if __name__ == '__main__':
    app.run()