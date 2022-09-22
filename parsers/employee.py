from flask_restful import Resource, reqparse, inputs


register_employee_parser = reqparse.RequestParser()
register_employee_parser.add_argument(
    "name", required=True, type=str, help=" 'name'This field cannot be blank."
)

register_employee_parser.add_argument(
    "salary", required=True, type=int, help=" 'salary'This field cannot be blank."
)

register_employee_parser.add_argument(
    "team_id", required=True, type=int, help=" 'team_id'This field cannot be blank."
)

register_employee_parser.add_argument(
    "role_id", required=True, type=int, help=" 'role_id'This field cannot be blank."
)



#----------------------------------------------------------------------------------------
update_employee_parser = reqparse.RequestParser()
update_employee_parser.add_argument(
    "name", type=str, help=" 'name'This can be left blank."
)

update_employee_parser.add_argument(
    "salary", type=int, help=" 'salary'This can be left blank."
)

update_employee_parser.add_argument(
    "team_id", type=int, help=" 'team_id'This can be left blank."
)

update_employee_parser.add_argument(
    "role_id", type=int, help=" 'role_id'This can be left blank."
)
