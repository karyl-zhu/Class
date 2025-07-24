# 通常 import 所呼叫的檔案，要在該檔案名稱後面加上.py
# import 引用
# random, ranint (最小值，最大值)
# ranint >> 隨機整數
import random

me = int(input('請輸入 0.剪刀 1.石頭 2.布'))
com = random.randint(0, 2)
game = ['剪刀', '石頭', '布']
print('我出的:', game[me])
print('電腦出的:', game[com])

# 為了解決 2+1=3 的情況(沒有定義3)，判斷式改成「取餘數」(概念：輪迴)
# 7 % 3 -> 1 念作 7 mod 3
# 若要控制產出的數在 n 個範圍，則須對 n+1 取餘數
if me == com + 1 % 3:
    print('我贏')
elif com == me + 1 % 3:
    print('我輸')
else:
    print('平手')

# list 清單[]
# index 預設編號是0，也就是說
# 剪刀 >> 0, 石頭 >> 1, 布 >> 2
# 這種編號和值得對應就是所謂的 key-value 對應
# 只要有 key-value 對應，救支援「查詢操作」
# 只能用 key 查 value，不能反過來


# 查詢功能[]
s = 'apple'
print (s[0])


