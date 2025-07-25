from urllib import request

url = 'https://www.ptt.cc/bbs/joke/index.html'

# 先定義我們的 useragent (類似假名)
# 設定變數 headers
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
headers = {'User-Agent':useragent}

# 帶著 headers 對網頁伺服器提出請求
req = request.Request(url = url, headers = headers)

# 取得回應，將收到的 request 打開
res = request.urlopen(req)

# 回傳PPT的文章頁面 html 原始碼 (字串)
print(res.read().decode('utf-8'))
