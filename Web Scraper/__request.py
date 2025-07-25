# request 套件
from urllib import request

url = 'http://httpbin.org/get'

res = request.urlopen(url)
# 網頁給我們的回應
# 印出來的資料型態為 bytes
# print('res.red() :', res.read())

# 透過 decode 以 utf-8 將出來的資料轉為字串(json)
print(res.read().decode('utf-8'))