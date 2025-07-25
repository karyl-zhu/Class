import requests
from bs4 import BeautifulSoup
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}
url = 'https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20250715/00/'

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

links_1 = soup.select('tr[class="odd"]')
links_2 = soup.select('tr[class="even"]')
all_links = links_1 + links_2

# ✅ 自動取得使用者桌面資料夾（安全做法）
user_dir = os.path.expanduser("~")  # 例如 C:/Users/qj860
save_path = os.path.join(user_dir, "Desktop", "專題", "爬蟲資料")
os.makedirs(save_path, exist_ok=True)

for each_link in all_links:
    url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20250715/00/" + each_link.a['href']
    file_name = url.split('/')[-1]
    file_path = os.path.join(save_path, file_name)

    res = requests.get(url)
    if res.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(res.content)
        print(f"✅ 檔案已儲存到：{file_path}")
    else:
        print(f"❌ 下載失敗，狀態碼：{res.status_code}")
