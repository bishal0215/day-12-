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

