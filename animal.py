class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        return "Woof"
    
class Cat(Animal):
    def speak(self):
        return "Meow"
    
dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())
    
