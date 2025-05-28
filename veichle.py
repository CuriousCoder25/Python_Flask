#wrong xa 5/27
class veichle:
    def __init__ (self,make,model):
        self.make=make
        self.model=model

class Car(veichle):
    def __init__(self,milage,capacity,make,model):
        self.milage=milage
        self.capacity=capacity

class display(self):
    print(f"Milage:{milage} Capacity")

car=Car("40","10",2027,L973)
car.display()