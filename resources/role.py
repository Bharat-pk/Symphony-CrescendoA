from flask import jsonify
from flask_restful import Resource, reqparse
from models.role import Role
from parsers.role import register_role_parser
from flask import Flask, request


class RoleRegister(Resource):
    def post(self):
        data = register_role_parser.parse_args()
        if Role.find_by_name(data["name"]):
            return {"message": "A Role with same name already exists"}, 400
        role = Role(**data)
        role.save_to_db()
        return {"message": "Role created successfully."}, 201
