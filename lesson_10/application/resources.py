from flask_restful import Resource
from flask import request
from .models import User
from .schemas import UserSchema
from marshmallow.exceptions import ValidationError
import json


class UserResource(Resource):

    def get(self, id=None):
        if id:
            return UserSchema().dump(User.objects.get(id=id))
        else:
            users = User.objects()
            return UserSchema().dump(users, many=True)

    def post(self):

        try:
            UserSchema().load(request.json)
        except ValidationError as e:
            return {'text': str(e)}
        user = User(**request.json).save()
        return UserSchema().dump(user)

    def put(self):
        pass

    def delete(self):
        pass