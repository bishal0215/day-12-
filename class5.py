#set in python is a collection of unique items it doesnot allow duplicates .
"""num={1,2,3,2,3,4}
print(num)

fruits=["apple","banana","mango"]
fruits.add("orange")
print(fruits) """

a={ 1,2,3}
b={3,4,5}
print(a|b) #union
print(a&b) #intersection
print(b-a)
print(a.symmetric_difference(b)) #difference