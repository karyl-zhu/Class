# 題目 1：動物 + 貓
# 請在 Animal 類別裡加一個屬性 age。

# 建立 Cat 類別繼承 Animal，新增一個屬性 color。

# 覆寫 speak()，讓貓叫聲變成「喵喵～」。

# 新增一個 show() 方法，印出名字、年齡和顏色。

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("不知道怎麼叫")

    def show(self):
        print(f"名字: {self.name}")
        print(f"年齡: {self.age}")

# 子類別：Dog（狗）繼承自 Animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # 呼叫父類別來處理 name
        self.breed = breed      # 自己加上狗品種

    # 覆寫父類別的 speak()
    def speak(self):
        print("汪汪！")

dog1 = Dog("Lucky", 25, "Shiba Inu")
dog1.speak()  # ➜ 印出：汪汪！

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def speak(self):
        print("喵喵~")

    def show(self):
        super().show()
        print(f"顏色: {self.color}")

cat1 = Cat("pipi", 3, "賓士")
cat1.show()
    