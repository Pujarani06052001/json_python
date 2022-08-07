# import json
# a={
#     "name": "David", 
#     "class": "I", 
#     "age": 6
# }
# file=open("json_2.json","r")
# x=file.read()
# finaldata=json.loads(x)

# print(finaldata)

import json
a={
    "name": "David", 
    "class": "I", 
    "age": 6
}
file=open("json_2.json","r")
x=file.read()
finaldata=json.loads(x)

print(finaldata)
