import requests
from bs4 import BeautifulSoup
from random import randint
from sqlalchemy.exc import IntegrityError
from faker import Faker
from . import db
from .models import User, Post
from .sqltool import find_title


def users(count=100):
    fake = Faker()
    i = 0
    while i < count:
        u = User(email=fake.email(),
                 username=fake.user_name(),
                 password='password',
                 confirmed=True,
                 name=fake.name(),
                 location=fake.city(),
                 about_me=fake.text(),
                 member_since=fake.past_date())
        db.session.add(u)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()


def posts(count=100):
    fake = Faker()
    user_count = User.query.count()
    for i in range(count):
        u = User.query.offset(randint(0, user_count - 1)).first()
        p = Post(title='签到',
                 body=fake.text(),
                 timestamp=fake.past_date(),
                 author=u)
        db.session.add(p)
    db.session.commit()


def fake_posts():
    post_list = get_post()
    print(len(post_list))
    get_data(post_list)


def get_post():
    html = "http://bbs.colg.cn/forum.php?mod=forumdisplay&fid=171&filter=typeid&typeid=549"
    link_head = "http://bbs.colg.cn/"
    r = requests.get(html)
    bs = BeautifulSoup(r.text, 'html.parser')
    post_list=[]
    titles = bs.find_all('a', {'class': 's xst'})
    for title in titles:
        t = str(title.string)
        if find_title(t):
            continue
        href = link_head + title['href']
        post_list.append({'title': t, 'href': href})
    return post_list


def get_data(post_list):
    user_count = User.query.count()
    for i, post in enumerate(post_list):
        u = User.query.offset(randint(0, user_count - 1)).first()
        title = post['title']
        link = post['href']
        r = requests.get(link)
        bs = BeautifulSoup(r.text, 'html.parser')
        body = bs.find_all('td', {'class': 't_f'})
        print('%d web get OK 200' % i)
        post = Post(title=title,
                    body=str(body).strip('[]'),
                    author=u)
        db.session.add(post)
        try:
            db.session.commit()
            print('%d database write OK 200' % i)
        except IntegrityError:
            db.session.rollback()

