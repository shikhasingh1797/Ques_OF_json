import json
a=  {"name":"David",
     "class":"I",
     "age": 6  
 }
my_file=open("ques2.json","w")
json.dump(a,my_file,indent=4)
my_file.close()
