# Problem was that take a three input x,y,z that will be the coordinates of a cube.the coordinates is like 0 =< i =< x, like wise all are same, then there is a fourth input 'n' which say sum of coordinate will not be greater then n mean if the coordinate is 0,0,1 is there 0+0+1!=n then its a coordinate:

# Solve by the list comprehension:

x=int(input("give a no"))
y=int(input("give a no"))
z=int(input("give a no"))
n=int(input("give a no"))

new_list=[ [i, j, k]
          for i in range(x+1) 
          for j in range(y+1) 
          for k in range(z+1) 
          if i+j+k != n]
print(new_list)

print()
# method 2 without the help of list comprehension

final_list=[] # final ans will be in this list
new_list2=[]

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                new_list.append(i)
                new_list.append(j)
                new_list.append(k)

for i in range(0, len(new_list2),3):
    print(i)
    groupe= new_list2[i:i+3]
    final_list.append(groupe)

print(final_list)