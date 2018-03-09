# flask-sqlalchemy真的是不好用
import sqlite3
from flask import current_app


def follow_count(user_id, follow='follower'):
    conn = sqlite3.connect(current_app.config['SQLITE3_DATABASE_URI'])
    c = conn.cursor()
    cursor = c.execute("SELECT COUNT(*) FROM follows where {}_id={}".format(follow, user_id))
    for i in cursor:
        result = i[0]
    conn.close()
    return result


def find_title(title):
    conn = sqlite3.connect(current_app.config['SQLITE3_DATABASE_URI'])
    c = conn.cursor()
    cursor = c.execute("SELECT title FROM posts WHERE title = '%s'" % title)
    check=None
    for i in cursor:
        check = i[0]
    conn.close()
    return check is not None

