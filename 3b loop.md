#1a=========================================================
n0=int(input("enter a non-negative and non-zero integer number:"))
while n0!=1:
        if n0 % 2==0:
           n0=n0//2
           print(n0)
        else:
           n0=3*n0+1
           print(n0)
#1a======================================================
#1b======================================================
x=int(input("enter a integer number:"))
while (x>0):
    print(x)
    x=x-1

x=int(input("enter a non-negative integer number:"))
while(x>0):
    print(x)
    x=x+1
#1b=====================================================
#1c===================================================
x1=int(input("enter a integer number x1:"))
x2=int(input("enter a integer number x2:"))
while True:
    x=x1+x2
    print(x)
    choice=input("Do you want to continue?(y/n):")
    if choice=="y or Y":
        continue
    else:
        print("Have a good day")
        break
    x1 = int(input("enter a integer number x1:"))
    x2 = int(input("enter a integer number x2:"))
#1c=====================================================
#2=====================================================
text="To be, or not to be, that is the question."
number=0
for char in text:
    if char=="t" or char=="T":
        number=number+1
        print("t:",number)
    if char=="o" or char=="O":
        number=number+1
        print("o:",number)
    if char=="e" or char=="E":
        number=number+1
        print("e:",number)
    if char=="i" or char=="I":
        number=number+1
        print("i:",number)
    if char=="b" or char=="B":
        number=number+1
        print("b:",number)
    if char=="a" or char=="A":
        number=number+1
        print("a:",number)
    if char=="n" or char=="N":
        number=number+1
        print("n:",number)
    if char=="s" or char=="S":
        number=number+1
        print("s:",number)

print("total number of alphabets:",number)
#2============================================
#challenge====================================
1. Connect any one more functions in one code.
2. How to write a new code haven't mentioned before.
