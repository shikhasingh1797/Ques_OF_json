import json
dict1={
 "a":  1,
 "a":  2,
 "a":  3, 
 "a": 4,   
 "b": 1, 
 "b": 2
 }
open_file=open("ques6.json","w")
json.dump(dict1,open_file,indent=4)
open_file.close()