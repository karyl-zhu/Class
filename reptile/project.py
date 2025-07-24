import requests
from bs4 import BeautifulSoup
import os

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'}
url = 'https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20250715/00/'

res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify)


# .csv 檔案都是 a 標籤
# 找出所有 a 標籤

links_1 = soup.select('tr[class="odd"]')
links_2 = soup.select('tr[class="even"]')

all_links = links_1 + links_2
# 確認有抓到資料
# 這邊抓到的 links 都是 list 所以要一個個抓出來
# print(all_link)

# 建立資料夾語法
# os.makedirs(path, exist_ok=True)
# 要建立的資料夾路徑（可以是相對路徑或絕對路徑）
# 若資料夾已存在是否 不報錯（預設為 False，會報錯），設成 True 則已有資料夾也不會出錯
# 資料夾名稱可以直接加在路徑的最後
# path 前面會加一個"r"是為了要讓程式碼辨識"\""

# 選擇要儲存的資料夾，並設定該地點沒有此資料夾會幫你建立一個
save_path = r'C:\Users\Owner\OneDrive\桌面\專題\爬蟲資料'
os.makedirs(save_path, exist_ok=True)

# 把每個csv的下載路徑抓出來
for each_link in all_links:
    url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20250715/00/" + each_link.a['href']
    
    # 從網址中自動取得檔案名稱
    file_name = url.split('/')[-1]

    # 組合完整儲存路徑 -> 絕對路徑，後面會用到
    file_path = os.path.join(save_path, file_name)
    
    # 發送 GET 請求下載檔案
    res = requests.get(url)
    
    # 如果請求成功（HTTP 200），才寫入檔案，避免寫入錯誤資料或程式中斷
    if res.status_code == 200:
        # 用 open 語法打開/建立檔案（如果檔案不存在會自動建立，檔名來自我們前面定義的 file_name）
        # 使用 'wb' 模式代表以「二進位寫入」方式寫入檔案內容（因為下載的是原始 csv 資料）
        # 然後用 write() 將從 requests 取得的二進位內容 res.content 寫入這個檔案中
        with open(file_path, 'wb') as f:
            f.write(res.content)
        # 這是顯示給我們看的，讓我們知道到底有沒有執行成功
        print(f"✅ 檔案已儲存到：{file_path}")
    else:
        print(f"❌ 下載失敗，狀態碼：{res.status_code}")
