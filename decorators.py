""" def my_functions(fname):
    print("hello " + fname +" you are my students")

my_functions("hari")
 """
 
""" def hubit(shakshyam):
    for amrit in shakshyam:
        print(amrit)
hari =["himal","bhuwan","arun"]
hubit(hari) """
#arbitrary arguments
""" def developer(*boys):
    print("hello" , boys[2])
developer("sita","gita","hira")
developer("ram","hari","saru","tanu")

list = ["ram","hari","saru","tanu"]
list = ["sita","gita","hira"]
print(f"hello{list[1]}") """

""" def function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(function(4,5,6))
 """
""" 
def functions(*number): 
    if len(number) == 0 :
        return None
    max_num = number[0]
    for num in number:
        if num > max_num:
            max_num = num
    return max_num
print(functions(2,4,5,1,7)) """

#arbitray keyword arguments
""" def func(**numbers):
    print("type:",type(numbers))
    print("name:",numbers["name"])
    print("Age:",numbers["age"])
    print("All data:", numbers)


func(name="sakshyam" , age=25, city="ktm") """
""" 
def my_functions(a,b,c):
    return a+b+c
sum=(1,2,3)
results = my_functions(*sum)
print(results) """

""" def my_func(a,b):
    return a/b
num = (23,5)
result = my_func(*num)
print(result)

def groups(fname,lname):
    print("hello",fname,lname)

person ={"fname":"Amrit","lname":"Bhattarai"}
groups(**person) """

#decorators 
""" def changecase(func):
    def myinner():
        return func().lower()
    return myinner
 
@changecase
def my_functions():
    return "HELLO SALLY"
print(my_functions()) """
""" 
def changecase(fund):
    def myinner(x):
        return fund(x).upper()
    return myinner
@changecase
def my_functions(name):
    return "hello" + name
print(my_functions("hari"))

def makechange(tea):
    def myinner():
        return tea().upper()
    return myinner

@makechange
def my_functiions():
    return "tea to coffee"
print(my_functiions()) """

""" def changecase(n):
    def changecase(func):
        def myinner():
            if n == 1:
                a = func().upper()
            else:
                a = func().lower()
            return a
        return myinner
    return changecase

@changecase(1)
def my_functions():
    return "Hello Handsome whats are you Doing "
print(my_functions()) """

""" def changecase(func):
    def myinner():
        return func().upper()
    return myinner

def add_greetings(func):
    def myinner():
        return "hello " + func() + " you are handsome"
    return myinner

@changecase
@add_greetings
def myfunction():
    return "hari bhai"

print(myfunction()) """

import functools
def changecase(func):
    @functools.wraps(func) #Import functools.wraps to preserve the original function name and docstring.
    def myinner():
        return func().upper()
    return myinner
@changecase
def my_functions():
    return "hello hari  bhaii"
print(my_functions.__name__)
