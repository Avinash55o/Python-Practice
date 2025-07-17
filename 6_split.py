#Split convert the output to the list
a="567777"
b=a.split()
print(b) #--- o/p ["567777"]

print("gap")

#---
c="1 4 4 555"
d=c.split()
print(d) #--- o/p ['1','4','4','555']


"""x=[3,3,4,4,5,5]
y=x.split()
print(y) #--- error"""

z=list(map(int,d)) # in this first argument it take is funtion in this case its int so it convert them into the int, you can also give str for string

print("its the map string",z)