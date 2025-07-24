# 題目 1：
# 把下面的數字平方後印出結果

nums = [2, 3, 4, 5]
caculate = list(map(lambda x: x ** 2, nums))
print(caculate)

# 題目 2：
# 有一串英文名字，請把它們全部轉成小寫

names = ["ALICE", "Bob", "CHARLIE"]
lo = list(map(lambda x : x.lower(), names))
print(lo)

# 題目 3：
# 請從一堆人的 dict 中，取出他們的年齡（age 欄位）

people = [
    {"name": "Ann", "age": 18},
    {"name": "Ben", "age": 22},
    {"name": "Cindy", "age": 25}
]
age_people = list(map(lambda x :x["age"], people))
print(age_people)

# 題目 4：
# 一群學生分數請都加 10 分（不超過 100 分）

scores = [70, 85, 95, 99]
plus_score = list(map(lambda x: min(x + 10, 100), scores))


# 題目 5：
# 你有一串金額的字串，請轉成整數後加總（提示：map + sum）

amounts = ["100", "250", "50"]
sum_mon = sum(map(int, amounts))
print(sum_mon)