# Importing json module
import json
my_data=["Some Author","Reading and writing JSON in python",123455]
# json.dumps(my_data)
with open("jsonfile.json","w") as f:
    json.dump(my_data,f)
f.close()


with open("jsonfile.json","r") as f:
    jsondata=json.load(f)
    print(jsondata)
f.close()