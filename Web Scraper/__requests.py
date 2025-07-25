# requests 套件
# 使用 get() or post() 打開網頁
import requests

url = 'http://httpbin.org/get'

# 向該網頁提出請求
# 網頁回傳回應
res = requests.get(url)

# 透過 requests 把回應的資料 print 出來
print(res.text)
