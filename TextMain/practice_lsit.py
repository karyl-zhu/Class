# while 寫法
scores = [80, 60, 90, 20, 100]
people = 0
i = 0
# 多用 len, 不要寫5, 不然 list 內容改了就要改很多
while i < len(scores):
    if scores [i] >= 60:
        people = people + 1
    i = i + 1

print(people)

# for in 寫法
scores = [80, 60, 90, 20, 100]
people = 0

for i in scores:
    if i >= 60:
        people = people + 1
print(people)

total = 0

for i in range(11):
    total = total + i

print(total)