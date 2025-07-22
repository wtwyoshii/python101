class Animal: 

    def speak(self): 

        return "Some sound" 

 
class Dog(Animal): 

    def speak(self): 

        return "Woof!" 



class Cat(Animal): 

    def speak(self): 

        return "Meow!" 


def speak_all(animals): 

    for animal in animals: 

        print(animal.speak()) 

 


animals = [Dog(), Cat(), Dog()] 

speak_all(animals) 