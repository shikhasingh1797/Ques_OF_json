import json
dict1={"a":4,
"b":5,
"c":6j
}
print(dict1)
my_file=open("ques5.json","w")
json.dump(dict1,my_file,indent=5)
my_file.close()


# so complex data type is not serializable in json.