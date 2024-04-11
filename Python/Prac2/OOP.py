#Larson Sequeira  Roll No 36  SE CMPN B
class Vehicle: 
    def __init__(self, capacity=100, moves_on = "land"):
        self.capacity = capacity
        self.moves_on = moves_on
    
    #polymorphism
    def moves(self):
        return self.moves_on
    
    #@abstractmethod
    def details(self):
        pass
 
#inheritance
class Boat(Vehicle):
    def __init__(self, name="", capacity=1000):
        super().__init__(capacity, moves_on="Water")
        self.name = name
    
    #polymorphism
    def moves(self):
        return "Water"
    
    def details(self): 
        print(f"Boat: \nName: {self.name} \nCapacity: {self.capacity} \nMoves On: {self.moves_on}")
 
 
 #inheritance
class Car(Vehicle):
    def __init__(self, model="", year=1990, color="black", brand=""):
        super().__init__(self, moves_on="Land")
        self.model = model
        self.year = year
        #Encapsulation
        self.__color = color
        self.brand = brand
    
    #polymorphism
    def moves(self):
        return "Land"
 
    def details(self):
        print(f"Car1: \nModel:{self.model}\nyear:{self.year}\nbrand:{self.brand}", end="\n\n")
 
 
 
mycar1 = Car(model="Innova", year=2010, color="white", brand="Toyota")
mycar1.capacity = 6
mycar1.details()
print(f"Car1: \nModel:{mycar1.model}\nyear:{mycar1.year}\ncolor:{mycar1._Car__color}\nbrand:{mycar1.brand}", end="\n\n")

myBoat = Boat(name="EverGreen", capacity=500)
myBoat.details()