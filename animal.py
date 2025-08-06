class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        return "Woof woof"
    
class Cat(Animal):
    def speak(self):
        return "Meow meow"
    
dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())


    
