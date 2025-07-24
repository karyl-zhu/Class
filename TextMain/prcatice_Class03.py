# 題目 3：書的分類
# 請根據下面描述建立兩個類別：

# 建立父類別 Book，有屬性：title, author。

# 建立子類別 EBook，繼承 Book，並加上 fileSize（檔案大小）。

# 實作一個 show() 方法：

# 父類別印出書名和作者。

# 子類別在印完書名與作者後，還要加上檔案大小。

# 定義類別 Book
class Book:
    # 初始化類別 Book 裡面的值(title, author)，並給他們一個變數(名字)
    def __init__(self,title, author):
        self.title = title
        self.author = author
    # 設定 類別 Book 的 show() 函式會做的事情
    def show(self):
        print(f"書名: {self.title}")
        print(f"作者: {self.author}")
# 定義子類別 EBook，父類別是 Book
class EBook(Book):
    # 初始化類別 EBook 裡面的值
    def __init__(self,title, author, fileSize):
        # 直接繼承父類別擁有的值
        super().__init__(title, author)
        # 補上自己新增的值
        self.fileSize = fileSize
    # 一樣，定義 EBook 的 show() 函式，繼承父類別，並補上自己新增的
    def show(self):
        super().show()
        print(f"檔案大小: {self.fileSize}")
# 輸入某本書的資料，並呼叫Class把值填入
P = EBook("Python", "黃彬華", "317GB")

P.show()