from flask import jsonify
from flask_restful import Resource, reqparse
from models.employee import Employee
from models.role import Role
from models.team import Team
from flask import Flask, request
from db import db


class BudgetMax(Resource):
    def get(self):
        data = (
            db.session.query(Team.name, db.func.sum(Employee.salary))
            .outerjoin(Employee, Employee.team_id == Team.id)
            .group_by(Team.name)
            .all()
        )
        max_budget_team = sorted(data, key=lambda x: x[1], reverse=True)[0]
        return {
            "responce ": f"{max_budget_team[0]} has highest budget among all Teams that is {max_budget_team[1]} -rupees"
        }, 201


class TeamSizeMax(Resource):
    def get(self):
        data = (
            db.session.query(Team.name, db.func.count(Employee.id))
            .outerjoin(Employee, Employee.team_id == Team.id)
            .group_by(Team.name)
            .all()
        )
        max_budget_team = sorted(data, key=lambda x: x[1], reverse=True)[0]
        return {
            "responce ": f"{max_budget_team[0]} has bigger team size among all Teams that is {max_budget_team[1]} members"
        }, 201


class BudgetMin(Resource):
    def get(self):
        data = (
            db.session.query(Team.name, db.func.sum(Employee.salary))
            .outerjoin(Employee, Employee.team_id == Team.id)
            .group_by(Team.name)
            .all()
        )
        max_budget_team = sorted(data, key=lambda x: x[1])[0]
        return {
            "responce ": f"{max_budget_team[0]} has lowest budget among all Teams that is {max_budget_team[1]} -rupees"
        }, 201


class TeamSizeMin(Resource):
    def get(self):
        data = (
            db.session.query(Team.name, db.func.count(Employee.id))
            .outerjoin(Employee, Employee.team_id == Team.id)
            .group_by(Team.name)
            .all()
        )
        max_budget_team = sorted(data, key=lambda x: x[1])[0]
        return {
            "responce ": f"{max_budget_team[0]} has smaller team size among all Teams that is {max_budget_team[1]} members"
        }, 201
