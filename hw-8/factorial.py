def factorial(x: int) -> int:
    if x == 0:
        return 1
    elif x < 0:
        raise ValueError("factorial() not defined for negative values")
    elif type(x) is float:
        raise TypeError("'float' object cannot be interpreted as an integer")
    else:
        fact = x
        for i in range(1, x):
            fact *= i
        return fact
