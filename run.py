#coding=utf-8
from app import create_app, db
from app.models import User, Role, Permission
from flask_script import Manager
import sys


if sys.platform == 'linux':
    config_name = 'production'
else:
    config_name = 'development'
app = create_app(config_name)
manager = Manager(app)


if __name__ == '__main__':
    app.run()
