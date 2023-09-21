

class AddOps(list):

    def __init__(self):
        pass

class MultOps(tuple):

    def __init__(self):
        pass




class Operator:

    def __init__(self, hilbert_space, symbol, coefficient=1):
        self.hilbert_space = hilbert_space
        self.symbol = symbol
        self.coefficient = coefficient

    def __repr__(self):
        return f"{self.symbol}_{self.hilbert_space}"
    
    def __add__(self, other):
        return AddOps([self,other])
    
    def is_same_class(self, operator2):
        return type(self) == type(operator2)
    
    def is_same_hilbert(self, operator2):
        return self.hilbert_space == operator2.hilbert_space
    

    

a1 = Operator(1, "a")
a2 = Operator(2, "a")

print(a1.is_same_class(a2))
print(a1.is_same_hilbert(a2))



