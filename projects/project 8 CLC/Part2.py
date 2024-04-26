#Angel Velazquez and Jordan Scott
#CST-305 
#Project 8:  Part 2
import numpy as np
import matplotlib.pyplot as plt

# Function to be integrated
def f(x):
    return 0.1*x**2 + 2.2*x +5.0

# Function to calculate Riemann sum using the midpoint method
def riemann_sum(f, a, b, n):
    dx = (b - a) / n
    x = np.linspace(a + dx/2, b - dx/2, n)
    return np.sum(f(x) * dx)

# Parameters for the Riemann sum
a, b = 0, 30  # Limits of integration
n = 1000        # Number of rectangles

# Calculate the Riemann sum
approximation = riemann_sum(f, a, b, n)

# Plotting
X = np.linspace(0, 30, 400)
Y = f(X)
X_mid = np.linspace(a + (b-a)/(2*n), b - (b-a)/(2*n), n)
Y_mid = f(X_mid)

fig, ax = plt.subplots()
ax.plot(X, Y, 'r', label='R(t)')
ax.bar(X_mid, Y_mid, width=(b-a)/n, alpha=0.4, color='blue', edgecolor='b', align='center')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
plt.title(f'Riemann Sum Approximation of ∫0.1x^2 + 2.2x + 5.0dx from {a} to {b} \n Approximation: {approximation}') 
plt.show()