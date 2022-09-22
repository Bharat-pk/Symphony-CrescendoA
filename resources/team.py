from flask import jsonify
from flask_restful import Resource, reqparse
from models.team import Team
from parsers.team import register_team_parser
from flask import Flask, request


class TeamRegister(Resource):
    def post(self):
        data = register_team_parser.parse_args()
        if Team.find_by_name(data["name"]):
            return {"message": "A Team with same name already exists"}, 400
        team = Team(**data)
        team.save_to_db()
        return {"message": "Team created successfully."}, 201
