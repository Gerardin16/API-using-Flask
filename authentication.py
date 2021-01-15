from flask import Flask, jsonify,request,abort,make_response
from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()
app = Flask(__name__)

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

# A method to check the password for secured authentication
@auth.get_password
def get_password(username):
    if username == 'gerardin':
        return 'jerwin16'
    return None

# A route to display Home page with security
@app.route('/', methods=['GET'])
@auth.login_required
def homepage():
    return '<h1>Family Records</h1>'

# A error handler to handle for unauthorized access
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)



# Curl command for authentication check
#curl -u gerardin:jerwin16 -i http://localhost:5000
    
if __name__ == '__main__':
    app.run(debug=True)
   
  