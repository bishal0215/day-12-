""" def my_generator():
    yield 1
    yield 2
    yield 3
for value in my_generator():
    print(value) """

#count up to n number
""" def count_to_n(n):
    count = 1
    while count <= n:
        yield count
        count += 1
a = int(input("enter a number "))
for num in count_to_n(a):
    print(num)
 """
""" def large_sequence(n):
    for i in range (n):
        yield i 
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
 """

""" list_comp = [ x * x for x in range (5)]
print(list_comp)

gen_exp = ( x * x for x in range(5))
print(gen_exp)
print(list(gen_exp)) """

""" total = sum(x * x for x in range(10))
print(total)

def fibo():
    a , b = 0 ,1
    while True:
        yield a
        a,b = b, a+b
get = fibo()
for _ in range (11):
    print(next(get)) """


def echo_generetor():
    while True:
        received = yield
        print("Received:", received)
gen = echo_generetor()
next(gen)
gen.send("hello")
gen.send("bosideke")

def my_gen():
    try:
        yield 1
        yield 2
        yield 3
        yield 4
    finally:
        print("generetor close")
gen = my_gen()
print(next(gen))
gen.close()
