# Jordan Scott, Angel Velazquez
# 02/04/2024

import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import e
import time

def t4(k1, k2, k3, k4):
    return (k1 + 2*k2 + 2*k3 + k4)/6

def dydx(x, y):
    return y / (e**x - 1)
    
def rungeKutta(x0, y0, h):
    k1 = dydx(x0, y0)
    k2 = dydx(x0 + .5*h, y0 + .5*h * k1)
    k3 = dydx(x0 + .5*h, y0 + .5*h * k2)
    k4 = dydx(x0 + h, y0 + h * k3)
    y = y0 + h * t4(k1, k2, k3, k4)
    return y

# Driver method
h = 0.02
x0 = 1

y0 = 5
print(f'x0: {x0}')

x_values = []
y_values = []

def plot_recursive(x, y, count):
    if count > 980:
        return
    
    print(f'y{count}: {y}')
    print(f'x{count}: {x}')
    print(f'True Solution: {odeint(dydx, y, [x])}\n')
    
    x_values.append(x)
    y_values.append(y)
    
    y_next = rungeKutta(x, y, h)
    x_next = x + h
    
    plot_recursive(x_next, y_next, count + 1)

start_time = time.time()
plot_recursive(x0, y0, 0)
end_time = time.time()

plt.plot(x_values, y_values, 'ro')
plt.show()

computing_time = end_time - start_time
computational_steps = 980  # maximum recursion depth allowed by python

print(f"Computational Steps: {computational_steps}")
print(f"Computing Time: {computing_time} seconds")
