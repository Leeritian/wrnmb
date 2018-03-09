#coding=utf-8
from app import create_app, db
from app.models import  User, Role, Permission, Comment, Post
from app.fake import users, posts, fake_posts, find_title
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


def _make_context():
    return dict(app=app, db=db, User=User, Role=Role, Permission=Permission, Comment=Comment,
                Post=Post, db_init=db_reinit, users=users, posts=posts, fake_posts=fake_posts)


def db_reinit():
    db.create_all()
    Role.insert_roles()
    db.session.commit()


app = create_app('development')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=_make_context))


if __name__ == '__main__':
    manager.run()
