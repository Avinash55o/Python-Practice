# 5!= 1 x 2 x 3 x 4 x 5

n=int(input("enter the no: "))

# WITH FOR LOOP
product=1
for i in range(1,n+1):
    product= product *i

print(f"the factorial of {n}:",product);


# WITH WHILE LOOP
i=1
product_1=1
while i<=n:
    product_1=product_1 * i
    i += 1;
print(f"the factoial of {n}",product_1)
