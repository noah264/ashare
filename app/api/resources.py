import uuid
 
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash
 
# from ..models.user import UserModel
 
 
class Register(Resource):
    def get(self):
        print("hello")
        # parser = reqparse.RequestParser()
        # parser.add_argument('username', type=str, location='json')
        # parser.add_argument('password', type=str, dest='pwd', location='json')
        # data = parser.parse_args()
        # if UserModel.find_by_username(data['username']):
        #     return {
        #         'success': False,
        #         'message': "Repeated username!",
        #         'data': None,
        #     }, 400
        # else:
        #     try:
        #         data['salt'] = uuid.uuid4().hex
        #         data['pwd'] = generate_password_hash('{}{}'.format(data['salt'], data['pwd']))
        #         user = UserModel(**data)
        #         user.addUser()
        #         return {
        #             'success': True,
        #             'message': "Register succeed!",
        #             'data': None,
        #         }, 200
        #     except Exception as e:
        #         return {
        #             'success': False,
        #             'message': "Error: {}".format(e),
        #             'data': None,
        #         }, 500
