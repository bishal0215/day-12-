def fibo(n):
    if n<=1:
       return n
    return fibo(n-1) + fibo(n-2)
def fibonacci(n):
    return [fibo(i) for i in range(n+1)]

print(fibonacci(5))

