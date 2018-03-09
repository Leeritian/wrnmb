import unittest
from app import create_app, db


class FormPostTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.ctx = self.app.test_client()
        self.app.config['SERVER_NAME'] = 'TEST'
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def login(self, csrf):
        return self.ctx.post('/login', data=dict(
            email='txt_a1513@163.com',
            password="'or'='or'"

        ))

    def test_login_logout(self):
        s = '用户名或密码错误'
        s = s.encode()
        rv = self.ctx.get('/login')
        data = rv.data.decode('utf-8')
        st = data.find('csrf')
        print(data[st:st+30])
#        with open(r'f:\python\wrnmb\app\tokenList.txt', 'a') as f:
#            data = rv.data.decode()
#            f.write('\r\n' + data)
#       这个需要csrf验证
#        assert s in rv.data


if __name__ == '__main__':
    unittest.main()



