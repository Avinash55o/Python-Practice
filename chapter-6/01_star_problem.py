n= int(input("enter the number: "))
'''
for n=3
  *
 ***
*****  
'''


for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1),end="")
    print("");


print("")
'''
for n=4
*
**
***
****
'''

for i in range(1,n+1):
    print("*" * i, end="")
    print("");

print("")
'''
for n=3
***
* *
***
'''


for i in range(1,n+1):
    if i == 1 or i== n :
        print("*" * n,end="");
    else:
        print(f"*{" " * (n-2)}*",end="");
    print("")   