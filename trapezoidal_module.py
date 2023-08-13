# Creating module so that the function trapezoidal can be used in other program

def trapezoidal(f,a,b,n):
    h = float(b-a)/n
    result = 0.5*f(a) + 0.5*f(b)
    for i in range(1,n):
        result += f(a + i*h)
    result *= h
    return result

