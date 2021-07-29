from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
from Resource.student import Student,UserRegisitor
from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
# # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jose'


api = Api(app)

# jwt = JWT(app, authenticate, identity)


# class Item(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('price',
#         type=float,
#         required=True,
#         help="This field cannot be left blank!"
#     )
#
#     @jwt_required()
#     def get(self, name):
#         return {'item': "hihiu"}
#
#     def post(self, name):
#         if next(filter(lambda x: x['name'] == name, items), None) is not None:
#             return {'message': "An item with name '{}' already exists.".format(name)}
#
#         data = Item.parser.parse_args()
#
#         item = {'name': name, 'price': data['price']}
#         items.append(item)
#         return item

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)
api.add_resource(Student, '/item/<string:name>')
api.add_resource(UserRegisitor, '/user/<string:username>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True) # important to mention debug=True
