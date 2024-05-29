import math
def function(x):
    return math.exp(3*x) - 4

def derivate(x):
    h = 0.0001
    return (function(x+h) - function(x)) / h

def calculate_error(x1, x2):
    return abs(x2 - x1)

def x_intercept(x0):
    return x0 - function(x0)/derivate(x0)

def newton_raphson_method(x0, error):
    x1 = x_intercept(x0)
    error_calculated = calculate_error(x0, x1)
    while error_calculated > error:
        x0 = x1
        x1 = x_intercept(x0)
        error_calculated = calculate_error(x0, x1)
        error_porcentual = error_calculated/x1*100
    return (x1, error_porcentual)

def main():
    x0 = float(input("Enter the first value x0: "))
    error = float(input("Enter the error: "))
    
    root, error_porcentual = newton_raphson_method(x0, error)
    print("The root is: ", round(root,2))
    print("The error is: ", round(error_porcentual,2),"%")
    
main()

    