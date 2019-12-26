import requests
import execjs


class FangtxLogin():
    def __init__(self, url, headers, uid, session):
        self.session = None
        self.url = url
        self.headers = headers
        self._uid = uid
        self.session = session

    @property
    def get_password(self):
        js_path = 'get_password.js'
        with open(js_path, 'r', encoding='utf-8') as f:
            js_content = f.read()
            ctx = execjs.compile(js_content)
            pwd = ctx.eval('password')
            print(pwd)
            return pwd

    def login(self):
        data = {
            "uid": self._uid,
            "pwd": self.get_password,
            "Service": "soufun-passport-web",
            "AutoLogin": 0,
        }
        # print(data)
        html = self.session.post(url=self.url, headers=self.headers, data=data)
        print(html.status_code)
        print(html.text)


if __name__ == '__main__':
    url = 'https://passport.fang.com/login.api'
    session = requests.session()
    headers = {
        "Host": "passport.fang.com",
        "Referer": "https://passport.fang.com/",  # Referer是必须字段，可能是防止csrf攻击
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
    }
    uid = 123456  # 你的账号
    login = FangtxLogin(url=url, headers=headers, uid=uid, session=session)
    login.login()