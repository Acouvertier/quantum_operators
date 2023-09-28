import functools

class AddOps(list):

    def __init__(self, *args):
        super(AddOps,self).__init__(*args)

    

class MultOps(tuple):

    def __init__(self,args):
        super(MultOps,self).__init__()

    def __repr__(self):
        total_coeff = functools.reduce(lambda a, b: a*b, map(lambda c: c.coefficient ,self))
        total_ops = functools.reduce(lambda a, b: a.__str__() + "*" +b.__str__(), self)
        return f"{total_coeff}*{total_ops}"
    
    def __add__(self, other):
        return Operator.add_op_mult(self,other)


        




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
        
    def __str__(self):
        return f"{self.symbol}_{self.hilbert_space}"

        
    @staticmethod
    def mult_with_op(left_term, right_term, is_op_left):
        if is_op_left:
            term_check = right_term
            op = left_term
        else:
            term_check = left_term
            op = right_term

        if isinstance(term_check, Operator):
            return MultOps([left_term,right_term])
        elif isinstance(term_check, MultOps):
            if is_op_left:
                return MultOps([left_term,*right_term])
            else: 
                return MultOps([*left_term,right_term])
        elif isinstance(term_check, AddOps):
            if is_op_left:
                newOps = list(map(lambda x: MultOps([left_term,x]), right_term))
            else: 
                newOps = list(map(lambda x: MultOps([x,right_term]), left_term))
            return AddOps(newOps)
        else:
            return Operator(op.hilbert_space, op.symbol, op.coefficient * term_check)
        
    @staticmethod
    def add_op_mult(original, add_on):
        if isinstance(add_on, Operator) or isinstance(add_on, MultOps):
            return AddOps([original, add_on])
        elif isinstance(add_on, AddOps):
            return AddOps([original, *add_on])
        else: 
            print("no thanks")

        

    
    def __add__(self, other):
        return Operator.add_op_mult(self,other)

    def __mul__(self, other):
        return Operator.mult_with_op(self, other, True)

    def __rmul__(self, other):
        return Operator.mult_with_op(other, self, False)
    
    def is_same_class(self, operator2):
        return type(self) == type(operator2)
    
    def is_same_hilbert(self, operator2):
        return self.hilbert_space == operator2.hilbert_space
    

    

a1 = Operator(1, "a",1)
a2 = Operator(2, "a", 2)
a3 = Operator(3, "a", 3)
a4 = Operator(4, "a", 4)
a5 = Operator(5, "a", 5)

a1pa2 = a1 + a2

a3ma5 = a3 * a5

print(a1pa2, a3ma5)

print(a1pa2 * a5)

print(a3ma5 * a4)




