class MathOps: 

    count = 0 


    @staticmethod 

    def add_num(a, b): 

        MathOps.count += 1 

        return a + b 


    @classmethod 

    def get_count(cls): 

        return cls.count 



print(MathOps.add_num(5, 3)) 

print(MathOps.get_count()) 

