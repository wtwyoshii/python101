def power_fn(n): 

    def power(x): 

        return x ** n 

    return power 


square = power_fn(2) 

cube = power_fn(3) 

 

print(square(4))  

print(cube(2))    