
import json,jwt
from flask import *
from flask_restful import *
from jsonschema import validate, ValidationError, SchemaError


app = Flask(__name__)
api = Api(app)
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

def validate_token(payload,schema):
    try:
        validate(payload,schemas[schema])
    except ValidationError:
        return ValidationError.context

    if schema == 'token':
        token = get_auth_token(payload)
        return token

    if schema == 'login':
        pass

    if schema == 'signup':
        pass


def get_auth_token(payload):
    return str(jwt.encode({'payload':payload},SECRET_KEY,algorithm='HS256'))


#######################################################################################################################

class Home(Resource):
    def get(self):
        return {'home':'feysevi zanmi !'}

class Token(Resource):
    def post(self):
        payload = {'email':request.form['email'],'password':request.form['password']}
        access = validate_token(payload,'token')
        return { 'access':access}


api.add_resource(Home,'/')
api.add_resource(Token,'/token')

if __name__ == "__main__":
    init_schemas()
    app.run(debug=True,host='0.0.0.0',port=5001)