class Calculator:
    def __init__(self,value):
        self.value=value
        
    def Cube(self):
        print(f"cube of the no is: {self.value**3}");
    
    def square(self):      
        print(f"square of the no is: {self.value**2}")

    def square_root(self):
        print(f"square root of the no is: {int(self.value ** 1/2)}")

find= Calculator(4)
find.square()
find.Cube()
find.square_root()
