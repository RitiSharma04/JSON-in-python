import json


a={"Name": "Abhishek",
    "Designation": "CEO of navgurukul",
    "Gender":"male",
    "Age": "29"
    }
file=open("Taxt.json","a")
b=json.dump(a,file) 
file.close()   
with open("Taxt.json") as f:
   data = json.load(f)

print(data)