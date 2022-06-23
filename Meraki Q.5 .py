import json

a='{"4" :"5+4j", "6": 7,"1": 3,"2": 4}'
print(a)
b=json.loads(a)
print(b)
print(type(b))
if complex in b:
    print("y")
else:
    print("no")    
