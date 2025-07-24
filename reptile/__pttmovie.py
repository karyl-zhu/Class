import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/movie/index10688.html'

res = requests.get(url, headers = headers)

soup = BeautifulSoup(res.text, 'html.parser')

article_title_html = soup.select('div[class="title"]')

for each_article in article_title_html:
    print(each_article.a.text)
    print("https://www.ptt.cc" + each_article.a['href']) 
