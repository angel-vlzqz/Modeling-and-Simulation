# Jordan Scott, Angel Velazquez
# 02/04/2024

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import e
import time

def t4(k1, k2, k3, k4):
    return (k1 + 2*k2 + 2*k3 + k4)/6

def dydx(x, y):
    return y / (e**x - 1)

def dydx2(y, x):
    return y / (e**x - 1)

def rungeKutta(x0, y0, h):
    k1 = dydx(x0, y0)
    k2 = dydx(x0 + .5*h, y0 + .5*h * k1)
    k3 = dydx(x0 + .5*h, y0 + .5*h * k2)
    k4 = dydx(x0 + h, y0 + h * k3)
    y = y0 + h * t4(k1, k2, k3, k4)
    return y

if __name__ == "__main__":
    # Driver method
    h = 0.02
    x0 = 1
    y0 = 5
    x_values = []
    y_values = []
    x_odeint = np.linspace(x0, 20, 1000)
    y_odeint = odeint(dydx2, y0, x_odeint)

    start_time = time.time()
    
    for count in range(980):
        print(f'y{count}: {y0}')
        print(f'x{count}: {x0}')
        print(f'True Solution: {odeint(dydx, y0, [x0])}\n')
        
        x_values.append(x0)
        y_values.append(y0)
        
        y0 = rungeKutta(x0, y0, h)
        x0 += h
    
    end_time = time.time()
    
    computing_time = end_time - start_time
    computational_steps = count + 1
    
    print(f"Computational Steps: {computational_steps}")
    print(f"Computing Time: {computing_time} seconds")
    
    
    # initialize the graph
    figure, axis = plt.subplots(1, 3, sharey=True)
    axis[0].plot(x_values, y_values, 'r-', label='Runge-Kutta')
    axis[0].set_title('Runge-Kutta')
    axis[1].plot(x_odeint, y_odeint, 'b-', label='Odeint')
    axis[1].set_title('Odeint True Solution')
    
    axis[2].plot(x_values, y_values, 'r-', label='Runge-Kutta')
    axis[2].plot(x_odeint, y_odeint, 'b-', label='Odeint')
    axis[2].set_title('Runge-Kutta & Odeint')
    
    plt.show()
    