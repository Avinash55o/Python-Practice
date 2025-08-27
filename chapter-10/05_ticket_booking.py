import random
class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"Train is booked in {self.trainNo} from {fro} to {to}")

    def train_status(self):
        print(f"Train no {self.trainNo} is running on time")
    
    def train_fare(self,fro, to):
        print(f"Your train ticket fare {fro} to {to} is: {random.randint(222,6666)}")
        

a=Train(12343241)

a.book("jorhat","guwahati")
a.train_fare("jorhat","guwahati")

