class Programmer:
    company= "Microsoft"

    def __init__ (self,name,salary,address):
        self.name= name
        self.salary=salary
        self.address=address

        print(f"name of the employee is {self.name} and salary is {self.salary} and address is {self.address}");

employee1= Programmer("avinash",1000000,"jorhat")