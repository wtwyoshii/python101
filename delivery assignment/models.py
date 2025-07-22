class Package:
    def __init__(self, id, weight, destination):
        self.id = id
        self.weight = weight
        self.destination = destination

    def __str__(self):
        return f"Package {self.id} to {self.destination} [{self.weight}pounds]"
    
class DeliveryVan:
    def __init__(self, name, max_capacity):
        self.name = name
        self.max_capacity = max_capacity
        self.inventory = []


    def load_package(self, pkg):
        total_weight = sum(p.weight for p in self.inventory)
        if total_weight + pkg.weight <= self.max_capacity:
            self.inventory.append(pkg)
            return True
        else:
            return False
    
    def deliver(self):
        for pkg in self.inventory:
            print(f"Delivering: {pkg}")
        self.inventory.clear()


    