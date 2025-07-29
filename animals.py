class Animal: 
    def __init__(self): 
        self.type = "Animal" 
        self.attributes = [] 


    def show_info(self): 
        print(f"{self.type}: {', '.join(self.attributes)}") 

 

class Mammal(Animal): 
    def __init__(self): 
        super().__init__() 
        self.type = "Mammal" 
        self.attributes = ["warm-blooded", "have hair or fur"] 

 

class WildMammal(Mammal): 
    def __init__(self): 
        super().__init__() 
        self.type = "Wild Mammal" 
        self.attributes += ["live in the wild"] 

 
class DomesticatedMammal(Mammal): 
    def __init__(self): 
        super().__init__() 
        self.type = "Domesticated Mammal" 
        self.attributes += ["tamed", "live with humans"] 

 
class Reptile(Animal): 
    def __init__(self): 
        super().__init__() 
        self.type = "Reptile" 
        self.attributes = ["cold-blooded", "have scales"] 


class Bird(Animal): 
    def __init__(self): 
        super().__init__() 
        self.type = "Bird" 
        self.attributes = ["have feathers", "lay eggs"] 


class Fish(Animal): 
    def __init__(self): 
        super().__init__() 
        self.type = "Fish" 
        self.attributes = ["live in water", "have gills"] 

 

class Amphibian(Animal): 
    def __init__(self): 
        super().__init__() 
        self.type = "Amphibian" 
        self.attributes = ["live in water and on land", "moist skin"] 

 


if __name__ == "__main__": 
    animal_classes = [ 
        WildMammal(), 
        DomesticatedMammal(), 
        Reptile(), 
        Bird(), 
        Fish(), 
        Amphibian() 
    ] 

 

    for animal in animal_classes: 
        animal.show_info() 