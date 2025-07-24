# 練習 6-1
#  ✤ 建立 1 個長⽅體 (Cuboid) 類別，內容包含 
# • 屬性：長 (length)、寬 (width)、⾼ (height) 
# • ⽅法  
# ✦ volume() ⽅法：計算完體積並回傳 
# ✦ getInfo() ⽅法：回傳長、寬、⾼與體積 
# • 建構式：設定屬性初始值 
# ✤ 主流程 
# • 將使⽤者輸入的長、寬、⾼建立 Cuboid 物件，並顯⽰該物件長、寬、⾼與體積
# 請輸入長⽅體的長、寬、⾼(空⽩間隔): 1 2 3 
# 輸入的長⽅體資訊如下:  
# 長: 1.0, 寬: 2.0, ⾼: 3.0, 體積: 6.0


num = input('請輸入長⽅體的長、寬、⾼(空⽩間隔): ')
ans = []
for i in num.split():
    ans.append(int(i))

class Cuboid:
    def __init__(self, l, w ,h):
        self.length = l
        self.width = w
        self.height = h
    
    def volume(self, d=1):
        caculate_volume = self.length * self.width * self.height
        return round(caculate_volume, d)
    
    def getInfo(self):
        return f'輸入的長⽅體資訊如下:\n長: {self.length}, 寬: {self.width}, 高: {self.height}, 體積: {self.volume()}'

    def __str__(self): # 被print()或str()時要顯示啥
        return self.getInfo()
    
c = Cuboid(*ans)  # 把 list 裡的值依順序拆成三個參數

print(c)
#print(c.getInfo()) #由於有設定 __str__ 所以不用這樣寫