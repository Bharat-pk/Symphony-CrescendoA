from flask_restful import Resource, reqparse, inputs


register_role_parser = reqparse.RequestParser()
register_role_parser.add_argument(
    "name", type=str, required=True, help=" 'name'This field cannot be blank."
)
