import json
add=input("aapko item khareedna hai ya add karna hai=")
item=input("item name=")
quantity=int(input("item quantity="))
a={}
shop={
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20"} 
i=0
if add=="add":
    shop[item]=quantity
    print(shop)
else:
    c=shop[item]
    shop[item]=int(c)-quantity
print(shop)   
my_file=open("question9.json","w")
json.dump(shop,my_file,indent=4)
my_file.close()