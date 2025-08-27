#defining a function
def greetings():
    "This is docstring of greetings function"
    print("Hello World")
    return

#defining and calling a function
def printme(str):
    "This prints a passed string into this function"
    print(str)
    return;
printme("I`m first call to user define function!")
printme("Again second call to the same function")

#checking the id() of a variable
def testfunction(arg):
    print("ID inside passing:",id(arg))
    
var = "Hello"
print("ID before passing:",id(var))
testfunction(var)

#an immutable object passed to the function
def testfunction(arg):
    print("ID inside the function:",id(arg))
    arg = arg+1
    print("new object after increment",arg,id(arg))
    
var = 10
print("ID before passing;",id(var))
testfunction(var)
print("value after function call",var)

#passing a list
def testfunction(arg):
    print("Inside function:",arg)
    print("ID inside the function:",id(arg))
    arg=arg.append(100)
var = [10,20,30,40]
print("ID before passing:",id(var))
testfunction(var)
print("list after function call",var)

#function arguments
def greetings(name):
    "This is docstring of greetings function"
    print("Hello {}".format(name))
    return 
greetings("Samay")
greetings("Pratima")
greetings("Steven")

#positional and required argument
def printme(str):
    "This prints a passed string into this function"
    print(str)
    return;
printme("My name victor")

#keyword argument
def printme(str):
    "This points a passed string into the function"
    print(str)
    return;
printme(str = "My string")

def printinfo(name,age):
    "This prints a passed info into this function"
    print("Name:", name)
    print("Age", age)
    return;
printinfo(age = 50,name = "miki")

#Default argument
def printinfo(name,age = 35):
    "This prints a passed info into this function"
    print("Name:", name)
    print("Age", age)
    return;
printinfo(age = 50,name = "miki")
printinfo(name="miki")

#positional-only argument
def posFun(x,y,/,z):
    print(x+y+z)
print("Evaluating positional-only arguments:")
posFun(33,22,11)

#keyword-only argument
def posFun(*, num1, num2, num3):
    print(num1*num2*num3)
print("Evaluating keyword-only arguments:")
posFun(num1=6,num2= 8,num3= 5)

#arbitrary argument
def printinfo( arg1, *vartuple ):
    "This prints a variable passed arguments"
    print ("Output is: ")
    print (arg1)
    for var in vartuple:
        print (var)
        return;
printinfo( 10 )
printinfo(70, 60, 50)

#function with return value
def add(x, y ):
    z = x+y
    return z
a = 10
b = 20
result = add(a,b)
print("a = {} b = {} a+b = {}".format(a,b,result))

#lambda function
sum = lambda arg1, arg2: arg1 + arg2;
print("value of total:",sum(10,20))
print("value of total:",sum(20,20))

#global and local variable
total = 0
def sum(arg1, arg2):
    total = arg1 + arg2;
    print("Inside the function local total:",total)
    return total;
sum(10,20)
print("Outside the function global total:",total)