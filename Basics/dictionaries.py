student= {"name":"Sarah","Age":22,"course":"Python"}
print(student)

student["city"]= "Hyderabad"
print(student)

print(student["name"])
print(student.get("city"))
print(student.get("country"))

student["country"]= "India"
print(student.get("country"))
print(student)

# methods 
print(student.keys())
print(student.values())
print(student.items())

#loop in dictionaries

for key in student:
    print(key)

for value in student.values():
    print(value)

for key,value in student.items():
    print(key,":", value)

# Nested dictionaries
students ={"student1": {"name":"Neha","Age":21,"course":"java"},
"student2":{"name":"Jane","Age":20,"course":"C++"}}

if "Age" in student:
    print("Age exists")

if "language" in student:
    print("Language exist")
