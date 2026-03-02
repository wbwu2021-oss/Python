# 1a
```python
def fuel_convert(direction,*values)
    result=[]
    for v in values:
        if direction=="kpl_to_mpg":
           converted=v*2.35215
           result(f"kpl={converted:}mpg")
        else direction=="mpg_to_kpl"
           converted=v*0.42514
           result(f"mpg={converted:}kpl")
return result
```

# 1b
```python
def reverse[]
    for value in reversed[]
        print(value)
```

# 1c
# lists are mutable, it can be changed
create an copy to modify, the original list can not be changed.
```python
def list(name)
     list=list.copy()
     list.append[0]()
print(list)
```

# 1d
funct_1=5   #local scope
funct_1=2   #gobal scope

# 2
def my_func(a,b,**c):
  print(c)

my_func(1,2,3,4,5,6)

```python
def my_func(data):
  a,b,c= data[0],data[1],data[2]
  return a,b**c
data_list=(1,2,3,4,5,6)
print(f"{my_func(data_list)}")
```

# 2
x=100 is to local scope
x=10 is to global scope
the result will output glocal scope, x=10


