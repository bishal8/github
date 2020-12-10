class Parent:
    def first(self):
        print("my name is bishal khadka")
class Parent2(Parent):
    def second(self):
        print("in my right side siddhant")
class Child(Parent2):
    def third(self):
        print("in my left side pramit")
obj=Child()
obj.first()
obj.second()
obj.third()