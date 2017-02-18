#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from urllib import request, parse, error
import http.cookiejar

url = "https://baidu.com"
headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}

response = request.urlopen(url, timeout=10)
html = response.read().decode("utf-8")

requesta = request.Request(url, data=None, headers={})
response = request.urlopen(requesta, timeout=10)

data = parse.urlencode({"act": "login", "email": "123@qq.com", "password": "123"})
request1 = request.Request(url, data=data) #POST
request2 = request.Request(url+"?%s" % data) #GET
response = request.urlopen(request1, timeout=10)

request3 = request.Request(url, data=data, headers=headers)
request3.add_header("Referer", "https://baidu.com")
response = request.urlopen(request3, timeout=10)

try:
    request.urlopen(request3, timeout=10)
except error.HTTPError as e:
    print(e.code, e.reason)
except error.URLError as e:
    print(e.errno, e.reason)

proxy_handler = request.ProxyHandler(proxies={"http": "127.0.0.1:1080"})

opener = request.build_opener(proxy_handler)
response = opener.open(url)

request.install_opener(opener)
response = request.urlopen(url)

cookie_jar = http.cookiejar.CookieJar()
cookie_jar_handler = request.HTTPCookieProcessor(cookiejar=cookie_jar)
opener = request.build_opener(cookie_jar_handler)
response = opener.open(url)



headers = {
"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
    "Cookie": "PHPSESSID=btqkg9amjrtoeev8coq0m78396; USERINFO=n6nxTHTY%2BJA39z6CpNB4eKN8f0KsYLjAQTwPe%2BhLHLruEbjaeh4ulhWAS5RysUM%2B; "
}
request1 = request.Request(url, headers=headers)

cookie = http.cookiejar.Cookie(name="xx", value="xx", domain="xx", ...)
cookie_jar.set_cookie(cookie)
response = opener.open(url)


opener1 = request.build_opener(cookie_jar_handler)
opener.add_handler(proxy_handler)
response = opener.open("https://baidu.com")

response = request.urlopen("图片地址")
with open("test.jpg", "w+") as file_img:
    file_img.write(response.read())


password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(realm=None, url=url, user="username", passwd="password")
handler = request.HTTPBasicAuthHandler(password_mgr)
opener = request.build_opener(handler)
response = opener.open(url, timeout=10)
