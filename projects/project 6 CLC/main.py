import math
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

'''PART 1A'''
# Define the symbols
x = sp.symbols('x')
y = sp.Function('y')(x)

# Define the differential equation
diff_eq = sp.Eq(y.diff(x, x) - 2*x*y.diff(x) + x**2*y, 0)

# Solve the differential equation
sol = sp.dsolve(diff_eq, y)

# Define the initial conditions
initial_conditions = {sol.args[1].subs(x, 0): 1, sol.args[1].diff(x).subs(x, 0): -1}

# Calculate the Taylor expansion of y(x) up to n <= 4
taylor_expansion = sol.args[1].series(x, 0, 5).removeO()

# Calculate the value of y at x = 3.5
y_value = taylor_expansion.subs(x, 3.5)

# Print the results
print("Taylor expansion of y(x) up to n <= 4:")
print(taylor_expansion)
print("Value of y at x = 3.5:")
print(y_value)

# Define the original function
def original_function(x):
    return np.sin(x)

# Define the Taylor series approximation
def taylor_series(x, n):
    approximation = 0
    for i in range(n+1):
        approximation += (-1)**i * x**(2*i+1) / math.factorial(2*i+1)
    return approximation

# Define the interval of convergence
x_values = np.linspace(-np.pi, np.pi, 100)

# Plot the original function
plt.figure()
plt.plot(x_values, original_function(x_values), label='Original Function')

# Plot the Taylor series approximations
for n in range(1, 5):
    plt.plot(x_values, taylor_series(x_values, n), label=f'Taylor Series (n={n})')

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.title('Taylor Series Approximation')


'''PART 1B'''

## Define the differential equation for Part 1B
#diff_eq_1b = sp.Eq(y.diff(x, x) - (x - 2)*y.diff(x) + 2*y, 0)
#
## Solve the differential equation
#sol_1b = sp.dsolve(diff_eq_1b, y)
#
## Define the initial conditions for Part 1B
#initial_conditions_1b = {sol_1b.args[1].subs(x, 3): 6, sol_1b.args[1].diff(x).subs(x, 3): 1}
#
## Calculate the Taylor expansion of y(x) up to the second order for Part 1B
#taylor_expansion_1b = sol_1b.args[1].series(x, 3, n=2)
#
## Evaluate the Taylor polynomial at x = 3
#y_3 = taylor_expansion_1b.removeO().subs(x, 3)
#
## Define the Taylor polynomial approximation function for Part 1B
#def taylor_polynomial(x):
#    return y_3
#
## Define the interval of convergence for Part 1B
#x_values_1b = np.linspace(2.5, 3.5, 100)
#
## Plot the original function and the Taylor polynomial for Part 1B
#plt.figure()
#plt.plot(x_values_1b, original_function(x_values_1b), label='Original Function')
#plt.plot(x_values_1b, taylor_polynomial(x_values_1b), label='Second Order Taylor Polynomial (Part 1B)')
#
#plt.xlabel('x')
#plt.ylabel('y')
#plt.legend()
#plt.title('Taylor Polynomial Approximation (Part 1B)')
#plt.show()

'''PART 2'''

# Define the range of x values
x_values = np.linspace(-2, 2, 100)

# Define the coefficients of y'' and y'
coefficient_y_double_prime = x_values**2
coefficient_y_prime = np.zeros_like(x_values)  # Coefficient of y' is always 0

# Plot the coefficients
plt.figure()
plt.plot(x_values, coefficient_y_double_prime, label="Coefficient of y'' (x^2)")
plt.plot(x_values, coefficient_y_prime, label="Coefficient of y' (0)")

# Highlight x = 0
plt.axvline(x=0, color='r', linestyle='--', label="x = 0")

# Add labels and legend
plt.xlabel('x')
plt.ylabel('Coefficient Value')
plt.title('Visualization of Coefficients')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()


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
plt.figure()
plt.plot(t, solution, label='Temperature Increase per Watt (Celcius)')
plt.xlabel('Time (Seconds)')
plt.ylabel('Temperature Increase per Watt (Celcius)')
plt.title('Temperature Increase per Watt Over Time (Celcius)')
plt.legend()
plt.grid(True)
plt.show()

