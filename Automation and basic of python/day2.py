#Topic
#elif
#nested if..else
#function
#OOP
#constructor
#import library example(calender)


#1. elif
#...if you have more than 2 options

num=-9
if(num>0):
    print("Number is positive")
elif(num<0):
    print("Number is negative")
else:
    print("Number is zero")

#2. nested else if
#..if..else statement inside another if..else condition

# num=float(input("Enter a number:"))
# if num>=0:
#     if num==0:
#         print("ZERO")
#     else:
#         print("Positive")
# else:
#     print("Negative")

#3. function
#a block of code which runs after being called
#def fun_name(parameter)
#def abc(username,password)

def abc(name):
    print("Hello",name)
abc("Proush")
abc(1234)
abc("saroj")

def add(num1, num2):
    return (num1 + num2)
print(add(2,5))
print(add(1,3))

#build in function
#print(), input(), range()

#variables: used to store the value

x=10
def fun():
    x=5
    print("value of x inside the function:",x)
fun()
print("value of x outside the function:",x)

#OOP: object oriented programming language
#class: collection of data and function sets
#object is the instance of a class

class myclass:
    a=100
    def fun1(self):
        print("Hello")
obj=myclass()
print(obj.a)
obj.fun1()

class calculator:
    def add(self,num3,num4):
        return num3+num4
    def mul(self,num3,num4):
        return num3*num4
cal1=calculator()
print(cal1.add(2,5))
print(cal1.mul(3,4))

#constructor: it is a function with double underscore
#__init__(), function is being called when object is created

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def print_emp_detailes(self):
        print("Employee name:",self.name)
        print("Employee Id:",self.id)

emp1=Employee("Proush",1)
emp2=Employee("Saroj",2)
emp1.print_emp_detailes()
emp2.print_emp_detailes()


#import calendar

import calendar
yy=2024
mm=7
dd=8
print(calendar.month(yy,mm,dd))