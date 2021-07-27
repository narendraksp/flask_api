from flask_restful import Resource,Api,reqparse
from flask import jsonify, make_response ,json
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity
from model.user import User

class Student(Resource):
      @jwt_required()
      def get(self, name):
        return{'studentsss' :name}
      @jwt_required()
      def post(self,name):
        return{'studentsxxxss' :name}


class UserRegisitor(Resource):
  TABLE_NAME = 'users'
  parser = reqparse.RequestParser()
  parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
  parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
  def get(self,username):
      user = User.find_by_username(username)
      if user:
       # response = jsonify(user.dict())
       # response.status_code = 200
       # return response, 500
       return {"message": "An error occurred inserting the item." }, 500

  def post(self):
    data = UserRegisitor.parser.parse_args()
    userObj = User(data['username'], data['password'])
    try:
        userObj.save_to_db()
    except:
            return {"message": "An error occurred inserting the item."}, 500
    response = jsonify(data)
    response.status_code = 200
    return response


    # data = UserRegisitor.parse.parse_args()
    # connecteL = sqlite3.connect("mm.db")
    # cursor = connecteL.cursor()
    # create_table = "INSERT INTO users VALUES (NULL, ?, ?)"
    # cursor.execute(create_table,( data['username'],"dsdd,ms"))
    # query = "SELECT * FROM users"
    # result = cursor.execute(query)
    # items = []
    # for row in result:
    #         items.append({'name': row[1], 'price': row[2]})
    # connecteL.commit()
    # connecteL.close()
    # return {'items': items}
