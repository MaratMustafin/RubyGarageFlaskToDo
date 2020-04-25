from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db,login

@login.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Projects(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    project_name = db.Column(db.String(50))
    tasks = db.relationship('Tasks',backref='project',lazy='dynamic')
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
        return 'Название проекта - {}'.format(self.project_name)


class Tasks(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    task_name = db.Column(db.String(50))
    task_status = db.Column(db.Boolean)
    task_priority = db.Column(db.Integer)
    date = db.Column(db.String(100)) 
    task_position = db.Column(db.Integer)
    project_id = db.Column(db.Integer,db.ForeignKey('projects.id'))

    def __repr__(self):
        return 'Название таска - {}'.format(self.task_name)



class Users(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50))
    password_hash = db.Column(db.String(64))
    projects = db.relationship('Projects',backref='author',lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return str(self.id)