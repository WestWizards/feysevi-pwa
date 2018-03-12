
from flask import *
from flask_restful import *

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return {'home':'feysevi zanmi !'}


api.add_resource(Home,'/')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5001)