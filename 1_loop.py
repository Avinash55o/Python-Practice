n=int(input("give a no:"))

# simple for loop
for i in range(n):
    print(i)

print()

#define the range
for i in range(1,n+1):
    print(i)

print()
#nested loop
for i in range(n):
    for j in range(i):
        print(j) # values of j will get then you can manipulate it according to the needs

print()

# arithmatic problem
for i in range(n):
    print("2 x",i,i*2)