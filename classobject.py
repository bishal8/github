class Test:
    def sum(self, a, b):
        s=a+b
        return s
a= int(input("enter a number:"))
b=int(input("enter a number:"))
obj=Test()
s=obj.sum(a,b)
print(s)