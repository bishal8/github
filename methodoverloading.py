class Parent:
    def function1(self):
        print("this is parent")
class Child(Parent):
    def function1(self):
        print("this is child")
obj=Child()
obj.function1()
