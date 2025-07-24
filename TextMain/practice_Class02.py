class Parent:
    def hello(self):
        print("Hello from parent")

class Child(Parent):
    def hello(self):
        super().hello()
        print("Hello from child")

c = Child()
c.hello()