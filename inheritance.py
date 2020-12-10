class Parent():
    def first(self):
        print("this is the first function")
class Child(Parent):
    def second(self):
        print("this is the second function")
ob=Child()
ob.first()
ob.second()