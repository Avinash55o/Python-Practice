def find_greatest():
    a= int(input("enter the no"))
    b= int(input("enter the no"))
    c= int(input("enter the no"))

    if a>b and a>c:
        print("a is the greatest no")
    elif b>a and b>c:
        print("b is the greatest no")
    else:
        print("c is the greatest no")

find_greatest()