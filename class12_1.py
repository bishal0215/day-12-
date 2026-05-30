class animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"{self.name}is sleeping.")
    def sleep(self):
        print(f"{self.name}is eating")
class dog(animal):
    def __init__(self, name):
        super().__init__(name)
    def bark(self):
        print(f"{self.name}is barking.")

dog1=dog("aash")
dog1.eat()
dog1.sleep()
dog1.bark()