# 練習重複除法到小數點第10位
# 練習寫程式的邏輯思考
a, b = 2,7
ans = "0."
i = 0
while i < 10:
    # 2 -> 20
    a10 = a*10 
    # 20 // 7
    ans = ans + (str(a10 // 7))
    print(ans)
    # 20 % 7
    a = a10 % b
    i = i + 1


# 機器人走路練習
x, y = 0, 0
# x = -2 y = 0
commands = 'ULLRDL'
i = 0
while i < len(commands):
    c = commands[i] 
    if c == "U":
        y = y + 1
    elif c == "D":
        y = y - 1
    elif c == "R":
        x = x + 1
    elif c == "L":
        x = x - 1
    i = i + 1

print(x, y)

# 算面積
import random

count = 0
total = 100000
i = 0
while i < total:
    # 對於這次隨機(x, y)
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    # 如果這座標在圓裡面，累積次數增加1
    if x ** 2 + y ** 2 <= 1:
        count = count + 1
    i = i + 1
# 圓形裡面 / 全部 * 參照物面積
ratio = count / total
print(ratio * 4)