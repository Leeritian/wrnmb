import unittest
from app.email import send_email
from app import create_app, db
from app.models import User


class EmailTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app.config['SERVER_NAME'] = 'TEST'
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_send_email(self):
        send_email('txt_a1513@163.com', '大哥你好',
                   'auth/email/confirm', user='李日天', token='有没有的吧')
        #登录检查是否收到   todo

    def test_password_setter(self):
        u = User(password='cat')
        self.assertTrue(u.password_hash is not None)


if __name__ == '__main__':
    unittest.main()