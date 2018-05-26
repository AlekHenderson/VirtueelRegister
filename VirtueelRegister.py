import http.cookiejar
import urllib
import urllib.request
import urllib.parse
import re
from selenium import webdriver

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))


def login():
    url = 'http://reg.pkskj.com/Home/Register?code=1776269188bd43f48dd2266ad7f5e583&viewName=rongyi'
    post_url = 'http://reg.pkskj.com/account/CheckImgCode'
    post_url2 = 'http://reg.pkskj.com/Common/SubmitInvite'
    mobile = input('请输入手机号:')
    code = ''
    password = 'password123'

    # 1.获取短信验证码.
    driver = webdriver.PhantomJS(executable_path=r'F:\learn\python\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver.get(url)
    res = driver.page_source
    reg = r'<font color="#.*?">(.)</font>'
    reg = re.compile(reg, re.S)
    cap = re.findall(reg, res)
    for v in cap:
        code += v
    data = urllib.parse.urlencode({'mobile': mobile, 'code': code}).encode(encoding='UTF8')
    request = urllib.request.Request(post_url, data)
    try:
        response = opener.open(request)
        result = response.read().decode('utf-8')
        print(result)
    except urllib.request.HTTPError as e:
        print(e.code)

    # 2.登录.
    vc = input('请输入短信验证码:')
    post_data = {
        'mobile': mobile,
        'vcode': vc,
        'code': '1776269188bd43f48dd2266ad7f5e583',
        'password': password,
        'appId': '124',
        'isAndroid': '0'
    }
    data2 = urllib.parse.urlencode(post_data).encode(encoding='UTF8')
    request2 = urllib.request.Request(post_url2, data2)
    try:
        response2 = opener.open(request2)
        result2 = response2.read().decode('utf-8')
        print(result2)
    except urllib.request.HTTPError as e:
        print(e.code)

if __name__ == "__main__":
    login()

