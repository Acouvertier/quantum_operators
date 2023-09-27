#__mul__ and __rmul__ for Operator class have copied code, can abstract out.

class AddOps(list):

    def __init__(self, *args):
        super(AddOps,self).__init__(*args)

    

class MultOps(tuple):

    def __init__(self,args):
        super(MultOps,self).__init__()




class Operator:

    def __init__(self, hilbert_space, symbol, coefficient=1):
        self.hilbert_space = hilbert_space
        self.symbol = symbol
        self.coefficient = coefficient

    def __repr__(self):
        if self.coefficient != 1: 
            return f"{self.coefficient}*{self.symbol}_{self.hilbert_space}"
        else: 
            return f"{self.symbol}_{self.hilbert_space}"
    
    def __add__(self, other):
        if isinstance(other, Operator) or isinstance(other, MultOps):
            return AddOps([self,other])
        elif isinstance(other, AddOps):
            return AddOps([self, *other])
        else: 
            print("no thanks")

    def __mul__(self, other):
        if isinstance(other, Operator):
            return MultOps([self,other])
        elif isinstance(other,MultOps):
            return MultOps([self,*other])
        elif isinstance(other, AddOps):
            newOps = list(map(lambda x: MultOps([self,x]), other))
            return AddOps(newOps)
        else:
            return Operator(self.hilbert_space, self.symbol, self.coefficient * other)
        
    def __rmul__(self, other):
        if isinstance(other, Operator):
            return MultOps([other,self])
        elif isinstance(other,MultOps):
            return MultOps([*other,self])
        elif isinstance(other, AddOps):
            newOps = list(map(lambda x: MultOps([x,self]), other))
            return AddOps(newOps)
        else:
            return Operator(self.hilbert_space, self.symbol, self.coefficient * other)
        

    
    def is_same_class(self, operator2):
        return type(self) == type(operator2)
    
    def is_same_hilbert(self, operator2):
        return self.hilbert_space == operator2.hilbert_space
    

    

a1 = Operator(1, "a")
a2 = Operator(2, "a")
a3 = Operator(3, "a")
a4 = Operator(4, "a")
a5 = Operator(5, "a")

a1pa2 = a1 + a2

a3ma5 = a3 * a5

print(a1pa2, a3ma5)

print(a1pa2 * a5)

print(a1 * -2j)




