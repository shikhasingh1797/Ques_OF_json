import json
x="""{
    "Name": "Jennifer Smith",
    "Contact Number": 7867567898,
    "Email": "jen123@gmail.com",
    "Hobbies":["Reading", "Sketching", "Horse Riding"]
    }"""
# print(x)
# print(type(x))
x=json.loads(x) 
print(x)
print(type(x))
