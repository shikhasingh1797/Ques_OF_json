my_file=open("ques7.txt","r")
file_data=my_file.read()
#print(file_data)
files=file_data.split()
#print(files)
b=files[::2]
c=files[1::2]
d=dict(zip(b,c))
#print(d)
d["Designation"]="CEO of Navgurukul"
#print(d)
d.pop("of")
print(d)
import json
open_file=open("quesestion7.json","w")
json.dump(d,open_file,indent=4)
open_file.close()