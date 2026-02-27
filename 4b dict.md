# question 1
## 1a) 
```python
info={"name":a,"name":b,"name":c,"name":d,"name":e,"name":f,"name":h,"name":g,"name":i
      "name":j,"name":k,"name":l}
print(info)
```
## 1b)
```python
my_user_dict={}
count=1
while True:
    ssn=input("enter ssn:")
    name=input("enter name:")
    my_user_dict["user"+str(count)]={"ssn":ssn,"name":name}
    count+=1
    choice=input("do you want to contine(Y/N):")
    if choice=="N"
       break
print(my_user_dict)
```
# List of tuples where each tuple represents a key-value pair

a = [("a", 1), ("b", 2), ("c", 3)]

# Convert the list of tuples into a dictionary

res = dict(a)

print(res)

```python
dict=[{"a":1,"b":2,"c":3}]
for res in dict:
    print(res)
```
# 1c
```python
data=[('Name', 'Sarah Connor'),
 ('Date of birth', '1 Jan 1980'),
 ('Address', '1000 Black Mountain Drive', 92126),
 ('Name', 'Jim Hawkins')]
my_dict={}
for item in data:
    if len(item)!=2:
        print("invalis key-value pair:",item)
    else:
         key=item[0]
         value=item[1]
print(my_dict)
```


      

