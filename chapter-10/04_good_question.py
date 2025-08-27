class Demo:
    a=4; #class attribute

o=Demo()
print(o.a) #print the class attribute

o.a=3 #created a instance(object) attribute
print(o.a) #will this change he class attribute the ans is no but will print the instance attribute

print(Demo.a)