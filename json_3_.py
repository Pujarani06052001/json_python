import json
# a Python object (dict):
python= {
  "name": "David",
  "class":"I",
  "age": 6  
}
j_data = json.dumps(python)
# result is a JSON string:
print(j_data)
