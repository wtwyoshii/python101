import math
import camelcase
from classtesting import Animal
from problem2 import max_sum_k
# finds square root of whatever number is equal to "number"
number = 16

square_root = math.sqrt(number) 

print(square_root)
# max sum
nums = [2, 1, 5, 1, 3, 2]
k = 4
result = max_sum_k(nums, k)
print(result)

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))

Animal.set_species("cat_species")

import math as OGmathlibrary
number1 = 25
square_root = OGmathlibrary.sqrt(number1)
print(square_root)
from classtesting import Animal as OGanimal
OGanimal.set_species("dog_species")
from problem2 import max_sum_k as max_sum
nums = [2, 1, 5, 1, 3, 2]
k = 5
result = max_sum(nums, k)
print(result)

