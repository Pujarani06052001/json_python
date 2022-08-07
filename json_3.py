import json
a={
    "name": "David", 
    "class": "I", 
    "age": 6
}
with open("json_3.json","w") as p:
    json.dump(a,p)
