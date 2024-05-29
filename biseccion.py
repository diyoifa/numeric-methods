import math
def function(x):
    return math.exp(3*x) - 4

def calculate_error(x1, x2):
    return abs(x2 - x1)

def bisection_method(x0, x1, error):
    x2_prev=0
    error_calculated = 100
    while error_calculated > error:
        x2 = (x0 + x1)/2
        if function(x0)*function(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        error_calculated = calculate_error(x2_prev, x2)
        error_porcentual = error_calculated/x2*100
        x2_prev = x2
    return (x2, error_porcentual)

def main():
    x0 = float(input("Enter the first value x0: "))
    x1 = float(input("Enter the second value x1: "))
    error = float(input("Enter the error: "))
    
    root, error_porcentual = bisection_method(x0, x1, error)
    print("The root is: ", round(root,2))
    print("The error is: ", round(error_porcentual,2),"%")
    
main()