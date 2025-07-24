# 🔥 練習題：max / min + key
# 題目 1
# 有一串水果字串，找出「字串長度最長」的水果名稱。

fruits = ["apple", "banana", "kiwi", "watermelon", "grape"]
long_fru = max(fruits, key=lambda x : len(x))
print(long_fru)
 
# 題目 2
# 有一串學生分數字典，找出分數最高的學生。

students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 95},
    {"name": "Cindy", "score": 92}
]
high_g = max(students, key=lambda x :x["score"])
print(high_g)

# 題目 3
# 給一串自訂類別物件 Car，找出「最快的車」。

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def __str__(self):
        return f"品牌: {self.brand}, 速度: {self.speed}"

cars = [
    Car("Toyota", 180),
    Car("BMW", 240),
    Car("Tesla", 220)
]

fast_car = max(cars, key=lambda x: x.speed)
print(fast_car)

# 題目 4
# 給一串日期字串，找出「最早的日期」。

# dates = ["2023-05-01", "2022-12-25", "2023-01-01", "2021-11-11"]
# 找出最早的日期字串
# (提示：字串轉成 datetime.datetime 會比較方便比較大小)




# 題目 5
# 有一串英文句子，找出「單字數量最多」的句子。

sentences = [
    "I love Python programming",
    "Hello world",
    "This is a sentence with multiple words",
    "Short one"
]

most_words = max(sentences, key=lambda s: len(s.split))
print(most_words)