class Test:
    def largest(self, a, b):
        if a>b:
            return a
            
        elif b>a:
            return b
a=int(input("enter a number:"))
b=int(input("enter a number:"))
bishal=Test()
s=bishal.largest(a,b)
print(s)
