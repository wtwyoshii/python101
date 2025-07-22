class Coffee:
    def cost(self):
        raise NotImplementedError()
    def description(self):
        raise NotImplementedError()

class SimpleCoffee(Coffee):
    def cost(self):
        return 2.0
    def description(self):
        return "Simple Coffee"

class CoffeeDecorator(Coffee):
    def init(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost()
    
    def description(self):
        return self.coffee.description()

class Milk(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.5

    def description(self):
        return self._coffee.description( + ",Milk")
    
class Sugar(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.2


    def description(self):
        return self._coffee.description() + ",Sugar"
    
class WhippedCream(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.7
    
    def description(self):
        return self._coffee.description() + ",Whipped Cream"
    
coffee = SimpleCoffee
print(coffee.description(), "-", coffee.cost())


