storedValue1 = None
storedValue2 = None
storedValue3 = None

def final(Value1, Value2, Value3):
    if Value2 == "+":
        return Value1 + Value3
    elif Value2 == "-":
        return Value1 - Value3
    elif Value2 == "*":
        return Value1 * Value3
    elif Value2 == "/":
        return Value1 // Value3 

def number(n, operation=None):
    return n if operation is None else operation(n)
    
def zero(op=None): 
    return number(0, op)
def one(op=None): 
    return number(1, op)
def two(op=None): 
    return number(2, op)
def three(op=None): 
    return number(3, op)
def four(op=None): 
    return number(4, op)
def five(op=None): 
    return number(5, op)
def six(op=None): 
    return number(6, op)
def seven(op=None): 
    return number(7, op)
def eight(op=None): 
    return number(8, op)
def nine(op=None): 
    return number(9, op)

# Operator functions (return functions to apply to numbers)
def plus(y): return lambda x: final(x, "+", y)
def minus(y): return lambda x: final(x, "-", y)
def times(y): return lambda x: final(x, "*", y)
def divided_by(y): return lambda x: final(x, "/", y)
