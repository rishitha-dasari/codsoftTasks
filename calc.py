import math
def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def product(x,y):
    print(x*y)
def divide(x,y):
    print(x//y)
def module(x,y):
    print(x%y)
def power(x,y):
    print(x**y)
def sqrt(x):
    print(math.sqrt(x))
def square(x):
    print(x**2)
def fact(x):
    if x==0:
        print("1")
    else:
        fact=1
        for i in range(1,x+1):
            fact=fact*i
        print(fact)
def inv(x):
    if x==0:
        print("Infinite")
    else:
        print(round(1/x,5))
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Module")
print("6.Power of a number")
print("7.Squareroot of a number")
print("8.Square of a number")
print("9.Factorial")
print("10.Inverse Of a number")
while(True):
    n=int(input("Enter choice(1-10):"))
    while n>=11:
        n1=int(input("Enter Valid option:"))
        if n1<11:
            n=n1
            break

    if n<=5:
        x=int(input("Enter num1:"))
        y=int(input("Enter num2:"))
        if n==1:
            add(x,y)
        elif n==2:
            sub(x,y)
        elif n==3:
            product(x,y)
        elif n==4:
            divide(x,y)
        elif n==5:
            module(x,y)
    elif n==6:
        x=int(input("Enter base:"))
        y=int(input("Enter power:"))
        power(x,y)
    elif n>6 and n<=10:
        x=int(input("Enter number:"))
        if n==7:
            sqrt(x)
        elif n==8:
            square(x)
        elif n==9:
            fact(x)
        elif n==10:
            inv(x)
    s=input("Do you want to perform another operation(yes/no):")
    if s.lower()=="no":
        break
    elif s.lower()=="yes":
        pass
    else:
        while s.lower()!="yes" or s.lower()!="no":
            s1=input("Enter valid choice!:")
            if s1.lower()=="yes" or s1.lower()=="no":
                s=s1
                break
    if s.lower()=="no":
        break
    
