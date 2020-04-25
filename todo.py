from app import app,db
from app.models import db,Tasks,Projects,Users

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Users': Users, 'Tasks': Tasks, 'Projects':Projects}