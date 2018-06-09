
import json,jwt
from flask import *
from flask_restful import *
from pymongo import *
from jsonschema import validate, ValidationError, SchemaError


app = Flask(__name__)
api = Api(app)
client = MongoClient('mongodb://heroku_stmmjgzt:a8k35bm8jgkbvlloh6g559jkhr@ds239439.mlab.com:39439/heroku_stmmjgzt')
app.secret_key = 'secret7patate@chevalier!kingsman21'
SECRET_KEY = app.secret_key

schemas = {}

#######################################################################################################################

def init_schemas():
    with open('./schemas/schema_login.json', encoding='utf-8') as data_file:
        schemas['login'] = json.load(data_file)
    with open('./schemas/signup.json', encoding='utf-8') as data_file:
        schemas['signup'] = json.load(data_file)
    with open('./schemas/schema_token.json', encoding='utf-8') as data_file:
        schemas['token'] = json.load(data_file)


def validate_request(payload,schema):
    try:
        validate(payload,schemas[schema])
    except ValidationError:
        return 'Fail to pass validating schema.'

    if schema == 'token':
        token = get_auth_token(payload)
        return token

    if schema == 'login':
        pass

    if schema == 'signup':
        # TODO : send_signup(payload) -> Mongo DB.
        return 'inscription validé.'



def get_auth_token(payload):
    return str(jwt.encode({'payload':payload},SECRET_KEY,algorithm='HS256'))


#######################################################################################################################

class Home(Resource):
    def get(self):
        return {'home':'feysevi zanmi !'}

class User_Signup(Resource):
    def post(self):
        payload = {'email',request.form['email'],
                   'civilite', request.form['civilite'],
                   'prenom', request.form['prenom'],
                   'nom', request.form['nom'],
                   'addresse', request.form['addresse'],
                   'code_postal', request.form['code_postal'],
                   'ville', request.form['ville'],
                   'telephone', request.form['telephone']}

        validate = validate_request(payload,'signup')
        return {'state':validate}


api.add_resource(Home,'/')
api.add_resource(User_Signup,'/signup')

if __name__ == "__main__":
    init_schemas()
    app.run(debug=True,host='0.0.0.0',port=5001)