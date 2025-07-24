# ✤ 定義1個 calculate(numbers)，共有 2 個回傳值 
# • 計算numbers所有元素的總和與平均值並回傳 (回傳總和與平均) 
# ✤ 讓使⽤者輸入⼀個數列，輸入完畢後呼叫上述 calculate 函式運算，
# 並將回傳的總和與平均顯⽰在畫⾯上 
# 請輸入整數數列(空⽩分隔): 1 2 3 4 5 
# 數列為: 1 2 3 4 5 
# 總和 = 15 
# 平均 = 3.0

def calculate(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

seq = input('請輸入整數數列(空⽩分隔): ')
num = []
for i in seq.split():
    num.append(int(i))

ans = calculate(num)
print(f'數列為: {seq}')
print(f'總和 = {ans[0]}')
print(f'平均 = {ans[1]}')