"""looping inside dictionary 
student={
    "name":"Abril",
    "age":17,
    "grade":'A'
}
for value in student.values():
    print(value)
for key, value in student.items():
    print(key,":",value) """
"""
marks={"math":80,"science":75,"English":90}
total=0 #variables initialization
for subject, score in marks.items():
    print(subject,":",score)
    total+=score
print(total)
per=(total/3)
print(per) """
#nested loop iside dictionary
students= {
    "Abril":{
        "math":80,
        "science":75    },
    "Bishal":{
        "math":90,
        "science":85
    }
}
for name, subjects in students.items():
    print("student:",name)
    total=0
    for subject , marks in subjects.items():
        print(subject,"=",marks)
        total+=marks
    print(total)
    per=(total/2)
    print(per)
    print()
    
   
