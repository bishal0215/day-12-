#keyname ;key value (list)
#students={"name":"Raju","age":"24","address":"butwal"}

#print(students["age"])
#students["name"]="sita"
#print(students.get("age"))
#print(students["name"])
#students["grade"]="A"

#students.pop("name")
#print(students)
"""
person={
    "name":"Richen",
    "age":25
}
person.update({
    "city":"Butwal"
})
#print(person)
person.update({"city":"Butwal"})
print(person.keys())
print(person.values())
print(person.items())
"""
# nested dictionsry
students= {
    "student1":{
        "name":"Ram",
        "age":21,
        "course":"data science"

    },
    "student2":{
        "name":"sita",
        "age":23,
        "course":"AI"
    }
}
print(students)
print(students["student1"])
print(students["student1"]["name"])
