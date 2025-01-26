from flask_restful import Resource, reqparse


class Ashare(Resource):
    def get(self):
        return "ashare"

    def getList(self):
        return []