#input block 
name=input("Enter students name :")
print(name)
mark_eng= int ( input("Enter marks in english:"))
mark_nep= int( input("Enter marks in Nepali:"))
mark_science= int( input("Enter marks in Science:"))
mark_math= int( input("Enter marks in Math:"))
#calculation block
total= mark_eng + mark_nep + mark_science + mark_math
print(total)
per=total/4
#conditional block
if per>80:
    grade="Distinction"
elif per>60:
    grade="first"
elif per>40:
    grade="second"
else:
    grade="fail"
#output block
print(per)
print(grade)
print("Student Name:",name)
print("English:",mark_eng)