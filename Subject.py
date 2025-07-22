class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)
    
    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Observer received update: {message}")

lemonade_stand = Subject()

customer1 = Observer()
customer2 = Observer()

lemonade_stand.subscribe(customer1)
lemonade_stand.subscribe(customer2)

lemonade_stand.notify("New flavor, Strawberry Lemonade")

lemonade_stand.unsubscribe(customer1)

lemonade_stand.notify("Price change: $1.50 per cup")
       
