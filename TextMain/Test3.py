# 物件導向 = 自定義型態
# class Person:
#     def set_data(self, w, h):
#         self.weight = w
#         self.height = h
#     def caculate_bmi(self, d=2):
#         bmi = self.weight / (self.height / 100) ** 2
#         return round(bmi, d)

# p1 = Person()
# p1.set_data(80, 175)
# print(p1.caculate_bmi(d=4))
class Person:
    def __init__(self, w, h):
        self.weight = w
        self.height = h
    def caculate_bmi(self, d=2):
        bmi = self.weight / (self.height / 100) ** 2
        return round(bmi, d)
    def __str__(self):
        return '[weight]:{}\n[height]:{}'.format(self.weight, 
                                                self.height)
    def __eq__(self, value):
        return(self.height == value.height and
               self.weight == value.weight)
# 一個型態可以擁有兩種東西
# 1. 專屬功能： 人.吃飯()
# 2. 專屬值： 人.身高
p1 = Person(70, 175)
print(p1.caculate_bmi(d=4))
# print(p1) -> p1轉換成字串 -> str(p1) -> p1.__str__()
print(p1)
p2 = Person(79, 175)
# p1 == p2 -> p1.__eq__(p2)
print(p1 == p2)