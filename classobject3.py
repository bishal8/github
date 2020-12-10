class Test:
    def factorial(self,x):
        if x==1:
            return 1
        else:
            return (x *self.factorial(x-1))
num=int(input("enter anumber:"))
bishal=Test()
s=bishal.factorial(num)
print(s)
