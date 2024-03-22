import numpy as py
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D

def lorenz(x, y, z, r, s=10, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

dt = 0.01
num_steps = 10000

# Need one more for the initial values
xs = py.empty(num_steps + 1)
ys = py.empty(num_steps + 1)
zs = py.empty(num_steps + 1)

# Set initial values
xs[0], ys[0], zs[0] = (0., 1., 1.05)

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point

stringInput = ["Enter a low value of r: ", "Enter a medium value of r: ", "Enter a high value of r: "]
for i in range(3):
    r = float(input(stringInput[i]))
    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], r)
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)

    fig = plt.figure()

    # Plot x-axis
    ax1 = fig.add_subplot(131)
    ax1.plot(range(num_steps + 1), xs)
    ax1.set_xlabel("Time (ms)")
    ax1.set_ylabel("X Axis")
    ax1.set_title("X Axis")

    # Plot y-axis
    ax2 = fig.add_subplot(132)
    ax2.plot(range(num_steps + 1), ys)
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Y Axis")
    ax2.set_title("Y Axis")

    # Plot z-axis
    ax3 = fig.add_subplot(133)

    # Ask user for input for the r variable
    # r = float(input("Enter the value of r: "))

    ax3.plot(range(num_steps + 1), zs)
    ax3.set_xlabel("Time")
    ax3.set_ylabel("Z Axis")
    ax3.set_title("Z Axis")

    # 3D plot
    fig2 = plt.figure()
    ax4 = fig2.add_subplot(111, projection='3d')
    ax4.plot(xs, ys, zs)
    ax4.set_xlabel("X Axis")
    ax4.set_ylabel("Y Axis")
    ax4.set_zlabel("Z Axis")
    ax4.set_title("Lorenz Attractor")

    plt.tight_layout()
    plt.show()
