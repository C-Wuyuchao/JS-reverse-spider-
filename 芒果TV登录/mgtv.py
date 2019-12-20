import execjs
import requests
import time

session = requests.session()


def get_pwd(s):
    js_path = "login.js"
    with open(js_path, 'r', encoding='utf-8') as f:
        js_content = f.read()
        ctx = execjs.compile(js_content)
        new_pwd = ctx.call("login", s)
    return new_pwd


def get_captcha():
    captcha_url = f"https://i.mgtv.com/vcode?from=pcclient&time={int(time.time() * 1000)}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
    }

    captcha_res = session.get(captcha_url, headers=headers)
    print(captcha_res.status_code)
    with open("captcha.jpg", "wb+") as f:
        f.write(captcha_res.content)
    code = input("请输入验证码: ")
    return code


def login(captcha, pwd):
    url = 'https://i.mgtv.com/account/loginVerify'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
    }
    data = {
        'sub': 1,
        'account': 123456,  # 你的邮箱或者手机号
        'pwd': pwd,
        'vcode': captcha,
        'remember': 1,
    }
    result = session.post(url=url, data=data, headers=headers)
    print(result.status_code)
    print(result.text)


def main():
    code = get_captcha()
    print(code)
    s = '123456'  # 你的密码
    pwd = get_pwd(s)
    login(code, pwd)


if __name__ == '__main__':
    main()


