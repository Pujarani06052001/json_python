import json
sm =  '{ "name":"John", "age":30, "city":"New York"}'
with open('new_file.json', 'w') as f:
    json.dump(sm,f)
print("json file coreted") 