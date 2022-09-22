from flask import jsonify
from flask_restful import Resource, reqparse, abort
from models.employee import Employee as EMP
from parsers.employee import register_employee_parser, update_employee_parser
from flask import Flask, request
from psycopg2 import errors
from db import db


class EmployeeRegister(Resource):
    def post(self):
        data = register_employee_parser.parse_args()
        if EMP.find_by_name(data["name"]):
            return {"message": "A Employee with same name already exists"}, 409
        try:
            emp = EMP(**data)
            emp.save_to_db()
        except Exception as e:
            return {"Exception": str(e)}, 400
        return {"message": "Employee created successfully."}, 201


class Employee(Resource):
    def put(self, id: int):
        data = {
            k: v
            for k, v in update_employee_parser.parse_args().items()
            if v is not None
        }
        emp = EMP()
        if emp.query.get(id):
            emp.query.filter_by(id=id).update(data)
            emp.update_to_db()
        else:
            abort(404, message="Employee id does not exist, cannot update.")
        return {"message": "Employee details updated successfully."}, 200

    def get(self, id: int):
        emp = EMP.find_by_id(id)
        if not emp:
            return {"message": "Employee Not Found"}, 404
        return emp.json(), 200

    def delete(self, id: int):
        emp = EMP.find_by_id(id)
        if not emp:
            return {"message": "Employee Not Found"}, 404
        emp.delete_from_db()
        return {"message": "Employee deleted."}, 200
