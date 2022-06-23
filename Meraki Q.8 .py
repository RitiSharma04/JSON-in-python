
a=[["neelam","programer","24","2400"],
["komal","trainer","24","20000"],
["anuradha","HR","25","40000"],
["Abhishek","manager","29","63000"]]
c=["emp1","emp2","emp3","emp4"]
d={}
for j in range(len(a)):
    dic={}
    b=["name","Designation","Age","salary"]
    for i in range(len(a[j])):
        dic.update({b[i]:a[j][i]})
    d.update({c[j]:dic}) 
print(d)               

