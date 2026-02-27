# question 1
# Write your code here. 1a
```python
a=input("enter the first value:")
b=input("enter the second value:")
c=input("enter the third value:")
e=input("enter the fourth value:")
f=input("enter the fifth value:")
my_tuple=(a,b,c,e,f)
print(my_tuple)
```
# Write your code here. 1b
```python
my_tuple=(1,2,3)
tem=list(my_tuple)
tem[1]=10
my_tuple=tuple(tem)
print(my_tuple)
```
# Write your code here. 1c
```python
my_tuple = (1,2,3,4,3,2,1,2,3,5,4,3,2,1)
count_dict={}
for num in my_tuple:
    if num in count_dict:
       count_dict[num]+=1
    else:
       count_dict[num]=1
print(count_dict)    
```

# Write your code here. 1d
```python
my_tuple=(1,2,3,4,3,2,1,2,3,5,4,3,2,1) part c
my_tuple=my_tuple+my_tuple
my_tuple=(1,2,3,4,3,2,1,2,3,5,4,3,2,1,1,2,3,4,3,2,1,2,3,5,4,3,2,1) part d
```

# Write your code here. 1e

x = (1,2,3,4)
x.append(1)
x[1] = "hello"
del x[2]
If use comma to seperate the numer, it will save as a tuple. Tuple cannot be changed after creatation. list can be change only
Transfer tuple to list, then change it
```python
x=(1,2,3,4)
tem=list(x)
tem[1]="hello word"
del tem[2]
x=tuple(tem)
print(x)
```

# Write your code here. 2a
(one, two, three, four) =  (1, 2, 3, 4)
type of those variable is tuple. Only list and tuple have unpacking. It is a tuple when use ().

# Write your code here. 2c
```python
x = (1, 2, 3, 4)
a, b, *c = x
a, b, c
2c. What will be the result of a, *b, c = x?
 output: (1,[2,3],4)
```

  
