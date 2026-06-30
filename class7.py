"""Set is a collection which is unordered, unchangeable*, and unindexed.
number=[1,2,3,4,4,5,5]
unique_number=set(number)
added_number=unique_number.add(6)
print(unique_number)

python_students={"ram","shyam","hari"}
django_students={"hari","sita","ram"}
print(python_students|django_students) #union   
print(python_students&django_students) #intersection
print(python_students-django_students) #difference
print(django_students-python_students) #difference
"""
a={ 1,2,3}
b={3,4,5}
common=a&b
a=a-common
b=b-common
print(a|b) #union

visitors=set()
for i in range(5):
    name=input("Enter visitor name: ")
    visitors.add(name)
print("unique visitors: ",visitors)
print("total unique visitors: ",len(visitors))

num = { 1,2,3,4}
unique_id= set(num)
print(num)
