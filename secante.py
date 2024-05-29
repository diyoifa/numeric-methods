import math
def function(x):
    return math.exp(3*x) - 4

def calculate_error(x1, x2):
    return abs(x2 - x1)

def x_intercept(x0, x1):
    return x1 - function(x1)*(x0 - x1)/(function(x0) - function(x1))

def secant_method(x0, x1, error):
    x2 = x_intercept(x0, x1)
    error_calculated = calculate_error(x1, x2)
    while error_calculated > error:
        x0 = x1
        x1 = x2
        x2 = x_intercept(x0, x1)
        error_calculated = calculate_error(x1, x2)
        error_porcentual = error_calculated/x2*100
    return (x2, error_porcentual)
    
def main():
    x0 = float(input("Enter the first value x0: "))
    x1 = float(input("Enter the second value x1: "))
    error = float(input("Enter the error: "))
    
    root, error_porcentual = secant_method(x0, x1, error)
    print("The root is: ", round(root,2))
    print("The error is: ", round(error_porcentual,2),"%")
    
main()
    