from flask import Blueprint
from flask_restful import Api
from .resources.register import Register
from .resources.ashare import Ashare
from .resources.ashare_list import AshareList


api_blueprint = Blueprint('api', __name__, url_prefix="/api")
api = Api(api_blueprint)


api.add_resource(Register, '/register')
api.add_resource(Ashare,'/ashare')
api.add_resource(AshareList,'/ashares')
