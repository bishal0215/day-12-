#recursive function 
def countdown(n):
  if n == 0:
    print("Done!")
    return
    
  print(n)
  countdown(n-1)
  

countdown(5)

#recursive function to calculate factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))

#recursive function to calculate the sum of a list
def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])
print(sum_list([1, 2, 3, 4]))

def fibonacci(n):
    if n<=1:
       return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))