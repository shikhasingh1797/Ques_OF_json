import json
dict1={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
print(dict1)
my_file=open("ques4.json","w")
json.dump(dict1,my_file,indent=4)
my_file.close()