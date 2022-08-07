
import json
a={
    "name": "David", 
    "class": "I", 
    "age": 6
}
with open("json_2.json","w") as f:
    json.dump(a,f)

    print("coreted file")

