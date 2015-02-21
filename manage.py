import os
from flask.ext.script import Manager, Shell
from app import create_app, db
from app.models import Activity, Category, Location, Instructor

app = create_app()
app.debug= True
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, Activity=Activity, Category=Category, Location=Location, Instructor=Instructor)
manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
