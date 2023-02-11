class Constructor:
    def __init__(self, name, arity, contravariants):
        self.name = name
        self.arity = arity
        self.contravariants = contravariants

    def __str__(self):
        return f"Constructor {self.name}--> arity: {self.arity}, contravariants positions: {self.contravariants}, args: {self.contravariants} "

    __repr__ = __str__

class Set_Variables:
    def __init__(self, name, variables):
        self.name = name
        self.variables = variables

    def __str__(self):
        return f"Set of Variables {self.name} --> '{' {self.variables}'}'"

    __repr__ = __str__

class Call:
    def __init__(self, constructor, expressions):
        self.constructor = constructor
        self.expressions = expressions #The args to the constructor

    def __str__(self):
        return f"Call( {self.constructor}, {self.expressions})"

    __repr__ = __str__

class Projection:
    def __init__(self, constructor, set_variables, index):
        self.constructor= constructor
        self.set_variables = set_variables
        self.index = index

    def __str__(self):
        return f"Const name {self.constructor}, set of vars: {self.set_variables}, index: {self.index}"

    __repr__ = __str__

class Expression:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return f"lhs: {self.lhs}, rhs: {self.rhs}"

    __repr__ = __str__

class Node:
    def __init__(self, object):
        self.object = object # The current object of the node. Can be Call/Proj/Set
        self.connections=[]
        self.connections_type=""