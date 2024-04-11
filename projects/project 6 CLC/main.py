import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

'''PART 1A'''
# Define the Taylor series function
def taylor_series_func(x):
    return 1 - x - (1/3)*x**3 - (1/12)*x**4

# Evaluate at x = 3.5
x_value = 3.5
y_value = taylor_series_func(x_value)

# Visualization setup
x_values = np.linspace(0, 10, 400)  # Range for visualization
y_taylor = taylor_series_func(x_values)

# Plotting the Taylor series approximation
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_taylor, label='Taylor Series Approximation up to n=4')
plt.scatter([x_value], [y_value], color='red')  # Point at x = 3.5
plt.text(x_value, y_value, f'y(3.5) ≈ {y_value:.4f}', verticalalignment='bottom', horizontalalignment='right')
plt.title('Taylor Series Approximation of the Solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)


'''PART 1B'''
# Define the Taylor polynomial function
def taylor_poly_func(x_val):
    return 6 + x_val - 5.5 * (x_val - 3)**2 + 3

# Visualization setup
x_range = np.linspace(0, 6, 400)  # Range for visualization
y_taylor = taylor_poly_func(x_range)

# Plotting the Taylor polynomial approximation
plt.figure(figsize=(10, 6))
plt.plot(x_range, y_taylor, label='Second-order Taylor Polynomial at x=3')
plt.scatter([3], [taylor_poly_func(3)], color='red')  # Point at x = 3
plt.text(3, taylor_poly_func(3), f'y(3) = {taylor_poly_func(3)}', verticalalignment='bottom', horizontalalignment='right')
plt.title('Taylor Polynomial Approximation of the Solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)


'''PART 2'''
# Define the system of ODEs
def system(u, x):
    u1, u2 = u  # u1 = y, u2 = y'
    du1dx = u2  # y' = u2
    du2dx = (x - u1) / (x**2 + 4)  # y'' = (x - y) / (x^2 + 4)
    return [du1dx, du2dx]

# Initial conditions (can adjust based on the problem's specifics)
u0 = [0, 0]  # [y(0), y'(0)]

# X values range
x = np.linspace(0, 10, 200)

# Solve the ODE
sol = odeint(system, u0, x)

# Plotting the solution
plt.figure(figsize=(10, 6))
plt.plot(x, sol[:, 0], label='y(x)')  # y(x) is the first component of the solution
plt.title('Numerical solution of the differential equation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)


'''PART 3'''
def temperature_model(y, t, h, A):
    # ODE representing the temperature increase per watt
    dydt = 1 / (h * A)
    return dydt

# Get user input
h = 100 # when chip is cooled by a a fan
A = float(input("Enter the surface area (square meters) average intel processor chip is .00322: "))

# Initial condition: temperature increase per watt
y0 = 0.0

# Time points
t = np.linspace(0, 10, 100)  # Adjust the time range as needed

# Solve the ODE
solution = odeint(temperature_model, y0, t, args=(h, A))

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, solution, label='Temperature Increase per Watt (Celcius)')
plt.xlabel('Time (Seconds)')
plt.ylabel('Temperature Increase per Watt (Celcius)')
plt.title('Temperature Increase per Watt Over Time (Celcius)')
plt.legend()
plt.grid(True)
plt.show()
