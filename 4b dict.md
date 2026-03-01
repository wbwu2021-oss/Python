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
# 1d
```python
info={}
for item in data:
     key=item[0]
     value=item[1]
     info[key]=value
print(result)
```
# 1e
```python
text="The tiger (Panthera tigris) is a large cat and a member of the genus Panthera native to Asia. It has a powerful, muscular body with a large head and paws, a long tail and orange fur with black, mostly vertical stripes. It is traditionally classified into nine recent subspecies, though some recognise only two subspecies, mainland Asian tigers and the island tigers of the Sunda Islands."
text=text.lower()
clean_text=""
for ch in text:
    if ch. isalpha() or ch==""
       clean_test+=ch
words=clean_text.split()
word_count={}
for word in words:
    if word in word_count:
       word_count[word]+=1
    else:
       word_count[word]=1
print(word_count)
```
# 2a
```python
d_orig = {123:"Coconut"}
d_copy = d_orig
print(d_orig)
print(d_copy)
d_copy[0][123]="apple"
print(d_copy)
```
# 2b
```python
d_orgin={123:"Cononut"}
print(d_orgin)
```
# 2c
```python
info={[1,2,3]}
Cannot use list as a key of dictionary.
List is unhashable
```





      

