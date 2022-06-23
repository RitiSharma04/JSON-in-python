import json


a={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}

f=open("shopping list.json","w")
f=json.dump(a,f)
change=open("shopping list.json","r")
l=json.load(change)
c=input("kon sa item khareedna chahte ho.")
d=int(input("kitne item chahte ho."))
for i in a:
    for j in a[i]:
        if c in a[i]:
            if j==c and int(a[i][j])>=d:
                e=int(a[i][j])-d
                a[i][j]=str(e)
        elif j !=c:
            print("Not in shopping list")
            break
item=input("iteme:-")
num=int(input("enter the num:-"))        
a[i].update({item:str(num)})
final_file=open("shopping list.json","w")
final=json.dump(a,final_file)        

# new=a
# print(new)
# final_file=open("shopping list.json","w")
# final=json.dump(new,final_file)
