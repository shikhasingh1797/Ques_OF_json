my_file=open("ques7.txt","r")
file_data=my_file.read()
#print(file_data)
files=file_data.split()
#print(files)
b=iter(files)
c=dict(zip(b,b))
#print(c)
c["Designation"]="CEO of Navgurukul"
#print(c)
c.pop("of")
print(c)
import json
open_file=open("ques7.json","w")
json.dump(c,open_file,indent=4)
open_file.close()