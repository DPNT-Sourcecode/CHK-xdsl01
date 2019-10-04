# noinspection PyShadowingBuiltins,PyUnusedLocal

"""Where:
 - param[0] = a positive integer between 0-100
 - param[1] = a positive integer between 0-100
 - @return = an Integer representing the sum of the two numbers"""
def compute(x, y):
    #
    if not all([isinstance(x,int),isinstance(y,int)]):
        raise AttributeError("Both args must be an int")
    if x not in range(0,101) or y not in range(0,101):
        raise AttributeError("Both args must be between 0 and 100")
    return x + y
    

print(compute(0,140))