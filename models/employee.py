from db import db
from models.role import Role
from models.team import Team


class Employee(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    salary = db.Column(db.Float(precision=2))

    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "salary": self.salary,
            "role_id": self.role_id,
            "team_id": self.team_id,
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_to_db(self):
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
