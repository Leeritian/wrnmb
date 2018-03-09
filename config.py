#coding= utf-8

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "fuck who bbbitch"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USERNAME = 'lrtiiian@163.com'
    MAIL_PASSWORD = 'lrt545201'
    FLASKY_MAIL_SUBJECT_PREFIX = '[wrnmb]'
    FLASKY_MAIL_SENDER = 'wrnmb 管理员<lrtiiian@163.com>'
    FLASK_ADMIN = 'lrtiiian@163.com'
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE = 30

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLITE3_DATABASE_URI = r'f:\python\wrnmb\app\data-pro.sqlite'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + r'f:\python\wrnmb\app\data-pro.sqlite'


class TestingConfig(Config):
    TESTING = True
    SQLITE3_DATABASE_URI = r'f:\python\wrnmb\app\data-test.sqlite'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLITE3_DATABASE_URI = os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
