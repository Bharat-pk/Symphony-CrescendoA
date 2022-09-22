from flask import Flask, jsonify
from flask_restful import Api
from db import db
from resources.employee import EmployeeRegister, Employee
from resources.role import RoleRegister
from resources.team import TeamRegister
from resources.insights import BudgetMax, TeamSizeMax, TeamSizeMin, BudgetMin

import os

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:yhkv#d2Ex6DJvXX9K2@localhost:5432/symphony_CrescendoA_assessment" # Update your postgres url here with uname and psw
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = 'u"ONmF=Oj)gBQ<:Kz}Pyhkv#d2Ex6DJvXX9K2:iHN<gp>CuhEjdX^,R"B=JP><7'
app.config["SQLALCHEMY_ECHO"] = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(RoleRegister, "/role/register") #POST
api.add_resource(TeamRegister, "/team/register") #POST
api.add_resource(EmployeeRegister, "/employee/register") #POST
api.add_resource(BudgetMax, "/Budget/max") #GET
api.add_resource(BudgetMin, "/Budget/min") #GET
api.add_resource(TeamSizeMin, "/TeamSize/min") #GET
api.add_resource(TeamSizeMax, "/TeamSize/max") #GET
api.add_resource(Employee, "/Employee/<int:id>") #GET, PUT, DELETE


if __name__ == "__main__":
    db.init_app(app)
    app.run()
