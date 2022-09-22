from flask_restful import Resource, reqparse, inputs


register_team_parser = reqparse.RequestParser()
register_team_parser.add_argument(
    "name", type=str, required=True, help=" 'name'This field cannot be blank."
)
