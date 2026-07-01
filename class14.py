#polymorphism is an ability in opp to use a common interface for multiple forms data types 
class Animals:
    def speak(self):
        print("animals makes sounds")
class cat(Animals):
    def speak(self):
        print("cat meow")
class birds(Animals):
    def speak(self):
        print("birds chirps")

#demonstration polymorphism 


#inheritance + polymorphism 

class vehicle:
    def move(self):
        print("vehicle is moving")

class car(vehicle):
    def move(self):
        print("car is moving")

class boat(vehicle):
    def move(self):
        print("boat is sailing")
class aeroplane(vehicle):
    def move(self):
        print("Aeroplane is flying")

vehicle = [car(), boat(), aeroplane()]
