import json
# ## convert json objaect into python
# a='[2,4,6,4]'
# b=json.loads(a)
# print(b)

## convert python data in json object

# a='hello'
# b=json.dumps(a)
# print(b)
# print(type(b))

## dumpe as a json str objaect in  json file or (write) in json file

# a={'name':"riti","age":18,"mood":"good"}
# b=open("details.json","w")
# d=json.dumps(a)
# b.write(d)
# b.close()


## convert in dic and then reed a json file


# f=open("details.json","r")
# data=f.read()
# f.close()
# user=json.loads(data)
# print(user["name"])
# print(type(user))

##convert python to json
# a={ "emp1": {
#         "name": "Lisa",
#         "designation": "programmer",
#         "age": "34",
#         "salary": "54000"
#     }}
# b=json.dumps(a)
# print(type(b))
# print(b)   

## convert json to python

# a='{"emp1":{"name": "Lisa","designation": "programmer","age": "34","salary": "54000" }}'
# b=json.loads(a)
# print(b)
# print(type(b))    
a=(2,3,4,2)
file=open("details.json","w")
b=json.dump(a,file)
print(type(a))

# a='{"a":3,"b":7}'
# print(type(a))