user=input("enter any emploee id:-")
emp1=["neelam","programer","24","2400"]
emp2=["komal","trainer","24","20000"]
emp3=["anuradha","HR","25","40000"]
emp4=["Abhishek","manager","29","63000"]
emp5=["sapna","student","24","34568909"]
emp6=["sikha","fc","29","3456890945"]
a=["name","post","age","salary"]
main_list=[emp1,emp2,emp3,emp4,emp5,emp6]
dict1={}
i=0
while (i<len(main_list)):
    j=i+1
    e="emp"+str(j) 
    dict1[e]=main_list[i]
    i=i+1
b=dict1[user]
c=dict(zip(a,b))
print(c)