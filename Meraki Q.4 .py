import json


c={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
a=[]    
for i in c:
    a.append(i)
for j in range(len(a)):
    for k in range(len(a)):
        if a[j]>a[k]:
            a[j],a[k]=a[k],a[j]
print(a)            
d={}            
for l in range(len(a)):
    for m in  c:
        if m==a[l]:
             d.update({m:c[m]})
print(d)                    
j=json.dumps(d)
print(j)
print(type(j))

