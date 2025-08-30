def first_func():
    print("We did it!")
first_func()

def number_squared(number):
    print(number**2)
number_squared(5)

def number_squared_cust(number,power):
    print(number**power)
number_squared_cust(5,3)

args_tuple = (5,6,1,2,8)
def number_args(*number):
    print(number[0]*number[1])
number_args(*args_tuple)

def number_squared_cust(number,power):
    print(number**power)
number_squared_cust(power = 5,number = 3)

def number_kwarg(**number):
    print("My number is:" + number['integer'] + "My other number:" + number['integer2'])
number_kwarg(integer = '2309',integer2 = '349')

def greet(first_name, last_name):
    print(f"Hi there{first_name} {last_name}")
    print("Welcome aboard")
greet("Mosh", "Hamedani" )

def greet(name):
    print(f"Hi {name}")


print(greet("Mosh"))
round(1.9)
def get_greetings(name):
    return f"Hi {name}"


message = get_greetings("Mosh")
print(message)

def increment(number, by=1):
    return number + by


result = increment(2, 1)
print(increment(2, 1))
print(increment(2, 5))



def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2, 3, 4, 5))

def save_user(**user):
    print(user["id"])
    
    
save_user(id=1, name="john", age=22)

def greet(name):
    message = "a"
    
def send_email(name):
    message = "b"
    
greet("Mosh")    
    
global variable
message = "a"

def greet(name):
    global message
    message = "b"    
    

    
greet("Mosh")
print(message)

def fizz_buzz(input):
    if (input % 3==0) and input % 5==0:
        return "FizzBuzz"
    if input % 3==0:
        return "Fizz"
    if input % 5==0:
        return "Buzz"
    if (input % 3==0) and input % 5==0:
        return "FizzBuzz"
print(fizz_buzz(15))
