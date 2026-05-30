#parent class 
class animal:
    def sound (self):
        print("Animal make sounds")
#child class
class dog(animal):
    def bark(self):
        print('Dog bark')
class cat(animal):
    def mews(self):
        print('cat mews')
#object of the chils class\
d=cat()
d.sound()
d.mews()
c=dog()
c.bark()
a=animal()
a.sound()

class person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print("Name:",self.name)
class student(person):
    def __init__(self,name,grade):
        super() .__init__(name)
        self.grade=grade
    def show_grade(self):
        print("grade:",self.grade)
s1=student("ram","A")
s1.show_name()
s1.show_grade()

#method overiding
class animal:
    def sound(self):
        print("animal sound")
class dog(animal):
    def sound(self):
        print("dog barks")
d=dog()
d.sound()

#multilevel inheritence

class grandparent:
    def house(self):
        print("grand parent house")
class parent(grandparent):
    def car(self):
        print("parent car")
class child(parent):
    def bikes(self):
        print("child bike")
c=child()
c.house()
c.car()
c.bikes()