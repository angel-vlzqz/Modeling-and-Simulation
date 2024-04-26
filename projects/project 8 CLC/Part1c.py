#Angel Velazquez and Jordan Scott
#CST-305 
#Project 8:  Part 1 : 1c
import numpy as np
import matplotlib.pyplot as plt

# Function to be integrated
def f(x):
    return np.log(x)

# Function to calculate Riemann sum using the midpoint method
def riemann_sum(f, a, b, n):
    dx = (b - a) / n
    x = np.linspace(a + dx/2, b - dx/2, n)
    return np.sum(f(x) * dx)

# Parameters for the Riemann sum
a, b = 1, np.e  # Limits of integration
n = 1000        # Number of rectangles

# Calculate the Riemann sum
approximation = riemann_sum(f, a, b, n)

# Plotting
X = np.linspace(1, np.e, 400)
Y = f(X)
X_mid = np.linspace(a + (b-a)/(2*n), b - (b-a)/(2*n), n)
Y_mid = f(X_mid)

fig, ax = plt.subplots()
ax.plot(X, Y, 'r', label='ln(x)')
ax.bar(X_mid, Y_mid, width=(b-a)/n, alpha=0.4, color='blue', edgecolor='b', align='center')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
plt.title(f'Riemann Sum Approximation of Integral: {approximation}')
plt.show()