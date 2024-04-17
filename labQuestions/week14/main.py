import numpy as np
import matplotlib.pyplot as plt

def lorenz_attractor(x, y, z, sigma, rho, beta):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

# Parameters
sigma = 10.0
rho = 13.0
beta = 8.0 / 3.0

# Initial conditions
x0 = 0.1
y0 = 0.0
z0 = 0.0

# Time step
dt = 0.01
num_steps = 10000

# Arrays to store the results
x_values = np.zeros(num_steps)
y_values = np.zeros(num_steps)
z_values = np.zeros(num_steps)

# Run the simulation
x = x0
y = y0
z = z0
for i in range(num_steps):
    dx, dy, dz = lorenz_attractor(x, y, z, sigma, rho, beta)
    x += dt * dx
    y += dt * dy
    z += dt * dz
    x_values[i] = x
    y_values[i] = y
    z_values[i] = z

# Plot the results
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_values, y_values, z_values)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Lorenz Attractor - Weather Patterns')
plt.show()
