#class innitialization with default  init

class Pet:
    def speak(self):
        print("sound made")
        # return ("pet spoke")

Rasmus = Pet()
Rasmus.name = "Rasmus"
print(Rasmus.name)
print(Rasmus.speak())

#simple class to represent a dog with modified init 
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age  = age       
    
    def speak(self):
        return f"{self.name} says woof! woof!"
    
Koba = Dog("Koba", "Great Dane", 3)
Koba.age = 4
print(Koba.speak())
print(Koba.age)

class Cat:
    pass

class Rat:
    pass

