print("\nCode on basics of functions:")
print()

def hello():
    print("Hello World")

def number(x):
    print("Counting:")
    for count in range (1,x+1,1):
        print(f"{count} ",end="")

def name(x):
    for i in range (1,x+1):
        print("My name is Rudransh Sharma")

def even(x):
    print("Even number ")
    for i in range (0,x+1):
        if i%2==0:
            print(f"{i} ",end="")

def sqr(x):
    print("Square of the given numbers")
    for i in range (0,x+1):
        print(f"{i*i} ",end='')

def table(x):
    for i in range (1,11):
        print(f"{x} x {i} = {x*i}")   # FIXED

def sum(x):
    sumation=0
    for i in range (1,x+1):
        sumation+=i
    print(f"{sumation}")   # FIXED (moved outside loop)

def odd(x):
    for i in range (0,x+1):
        if i%2!=0:
            print(f"{i} ",end="")

def total(x):
    count=0
    while x>0:
        x=x//10
        count+=1
    print(f"The total digits in the number is {count}")

def rev(x):
    sum2=0
    x2=x
    while x>0:
        remainder=x%10
        x=x//10
        sum2=(sum2*10)+remainder
    print(f"The reverse of {x2} is {sum2}")

def prime(x):
    if x <= 1:
        print(f"{x} is not a prime number")
        return

    flag = True

    for i in range(2, int(x**0.5)+1):   
        if x % i == 0:
            flag = False
            break

    if flag:
        print(f"The given number {x} is prime number")
    else:
        print(f"The given number {x} is not a prime number")

def palindrome(x):
    real=x
    sum=0
    x2=x   

    while x>0:
        remainder= x%10
        x=x//10
        sum=(sum*10)+remainder

    if real==sum:   
        print(f"The given number {x2} is a Palindrome")
    else:
        print(f"The given number {x2} is not a palindrome")

def fibo(x):
    a, b = 0, 1
    print("The given fibonacci series is :")
    for i in range (x):
        print(f"{a} ",end="")   
        a,b=b,a+b

def gcd(x,y):
    result=1
    for i in range (1,min(x,y)+1):
        if x%i==0 and y % i==0:
            result=i

    print(f"GCD of {x} and {y} is {result}")

#printing Hello World
hello()
print()

#Printing the counting of number upto input
num=int(input("Enter the number upto which you want to print number: "))
number(num)
print()

#Printing your names upto the input
num1=int(input("Enter the number of times you want to print your name: "))
name(num1)
print()

#Printing Even number upto the input
num2=int(input("Enter the number upto which you want to print Even number: "))
even(num2)
print()

#Printing Square of the inputs
num3=int(input("Enter the number upto which you want squares: "))
sqr(num3)
print()

#Printing Table from input
num4=int(input("Enter the number you want table for: "))
table(num4)
print()

#Printing the sum of First n number
num5 = int(input("Enter number upto which you want sum of numbers: "))
sum(num5)
print()

#Printing the odd numbers upto input
num6 = int(input("Enter the number uptowhich you want to print Odd number: "))
odd(num6)
print()

#Printing count digits in the number 
num7=int(input("Enter the number: "))
total(num7)
print()

#Priting reverse number from output
num8=int(input("Enter the number You want to reverse: "))
rev(num8)
print()

#Printing and checking the prime number
num9=int(input("Enter the number you want to check prime: "))
prime(num9)   # FIXED (added call)
print()

#Printing and checking palindrome 
num10=int(input("Enter the number you want to check: "))
palindrome(num10)
print()

#Printing fibonacci series
num11=int(input("Enter the number you want series upto: "))
fibo(num11)
print()

# GCD
num12=int(input("Enter the first number You want to check: "))
num13=int(input("Enter the second number you want to check: "))
print(f"GCD of the given numbers {num12} and {num13} :")
gcd(num12,num13)
print()
