# impliment an ODE solver for the Lorenz system

# Python code to implement Runge Kutta method
def t4(k1, k2, k3, k4):
    return (k1 + 2*k2 + 2*k3 + k4)/6

def dydx(x, y):
    return (x + y)
    
def rungeKutta(x0, y0, h):
    k1 = dydx(x0, y0)
    k2 = dydx(x0 + .5*h, y0 + .5*h * k1)
    k3 = dydx(x0 + .5*h, y0 + .5*h * k2)
    k4 = dydx(x0 + h, y0 + h * k3)
    y = y0 + h * t4(k1, k2, k3, k4)
    return y

# Driver method
x0 = 0
y0 = 1
h = 0.1

print('The value of y is:', rungeKutta(x0, y0, h))

