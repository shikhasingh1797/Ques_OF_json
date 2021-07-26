import json
emp1=["neelam","programer","24","2400"]
emp2=["komal","trainer","24","20000"]
emp3=["anuradha","HR","25","40000"]
emp4=["Abhishek","manager","29","63000"]
a=["name","post","age","salary"]
dict1={}
dict2={}
dict3={}
dict4={}
i=0
dict_main={}
while i<len(emp1):
    j=0
    while j<len(a):
        dict1[a[j]]=emp1[j]
        dict2[a[j]]=emp2[j]
        dict3[a[j]]=emp3[j]
        dict4[a[j]]=emp4[j]
        j+=1
    dict_main["emp1"]=dict1
    dict_main["emp2"]=dict2
    dict_main["emp3"]=dict3
    dict_main["emp4"]=dict4
    i+=1


# data=json.dumps(dict_main,indent=4)
# print(data)
# print(type(data))
print(dict_main["emp1"])

