def function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(function(4,5,6))
