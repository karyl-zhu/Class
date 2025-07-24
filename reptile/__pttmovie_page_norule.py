# 爬多頁，每頁頁碼沒規律

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/movie/index10688.html'

# 爬三頁
for i in range(0, 3):

    res = requests.get(url, headers = headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    article_title_html = soup.select('div[class="title"]')

    for each_article in article_title_html:
        if each_article.a:
            print(each_article.a.text.strip())
            print("https://www.ptt.cc" + each_article.a['href']) 
        else:
            print("文章已刪除")

    last_page_url = soup.select('a[class="btn wide"]')[1]['href']
    last_page_url = 'https://www.ptt.cc' + last_page_url

    url = last_page_url