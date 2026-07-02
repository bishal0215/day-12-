#write s lamda funtion to return the square of a number 
square = lambda x: x*x
print("the suare of 5 is ",square(5))

sum = lambda a, b: a+b
print("the sum of 3 and 4 is",sum(3,4))

is_even = lambda x: x%2==0
print("is 6 even?", is_even(6))
print("is 7 even?", is_even(7))

maximum = lambda a, b:a if a>b else b
print("the maximum of 10 and 20 is", maximum(10,20))

upercase = lambda s: s.upper()
print("the uppercase of 'hello' is", upercase('hello'))

list_uppercase = lambda lst: [s.upper() for s in lst]
print("the uppercase of ['hello', 'world'] is", list_uppercase(['hello', 'world']))

add_10 =lambda list: [x+10 for x in list]
print("adding 10 to each element of [1,2,3] gives", add_10([1,2,3]))

c2f = lambda temp_c: list(map(lambda temp_c: (temp_c * 9/5) + 32, temp_c))
print("the fahrenheit of 0 degree celsius is", c2f(0))

words = ["hello", "world", "python"]
lengths = list(map(lambda word: len(word), words))  
print("the lengths of the words are", lengths)

#filtering even numbers from a list using lambda function
numbers = [1, 2, 3, 4, 5, 6, 7,8,9,10]
result = list(filter(lambda x: x % 2 == 0, numbers))
print("the even numbers from the list are", result)

#filter
num =[5,12,18,3,7]
result = list(filter(lambda x: x>10, num))
print(result)

#remove empty stings 
words = ["hello", "", "data", "", "python"]
result = list(filter(lambda x: x != "", words))
print(result)

#starting with a 
names = ["Anita", "Arun", "Sita", "Ram"]
result = list(filter(lambda x: x.startswith("A"), names))
print(result)

#filtering positive numbers from a list using lambda function
num = [ -2,3,-1,5,0,8]
result = list(filter(lambda x: x>0, num))
print(result)

