fruits = ["apples", "tomatoes", "mangoes", "watermelons", "blueberries"]
# indexing
print(fruits[-1:-4])
# append
fruits.append("strawberries")
print(fruits[0:])
# replace
fruits[0] = "pears"
print(fruits)
fruits[0:3] = ["oranges", "guava", "dragonfruit"]
print(fruits)
# inserting
fruits.insert(2, "thornmelon")
fruits.insert(5, "green apples")
print(fruits)
# remove
fruits.remove("guava")
fruits.remove(fruits[3])
print(fruits)