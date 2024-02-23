# Angel Velazquez, Jordan Scott
import numpy as np
from scipy.integrate import solve_ivp, odeint
import matplotlib.pyplot as plt

#Define the ODE function for the first equation y'' + 4y = x
def odefunc(t, Y):
    y, dydt = Y
    # ODE: y'' + 4y = x
    d2ydt2 = -4 * y + t  
    return [dydt, d2ydt2]

#Define the ODE function for the second equation y'' + y = 4
def odefunc2(y, t):
    return [y[1], 4 - y[0]]

#Set the initial conditions and time span for integration for  equation 1 : 

# Initial conditions: y(0) = 0, y'(0) = 0
# this will be used for  equation 2
y0 = [0, 0]  
# Time span for integration > can be adjust if need upon 
t_span = (0, 10)  
#Integrate the ODE using solve_ivp
sol = solve_ivp(odefunc, t_span, y0, t_eval=np.linspace(t_span[0], t_span[1], 1000))

#Plot the solution using Matplotlib
t = sol.t
y = sol.y[0]


#Plot the solution using Matplotlib
plt.figure(figsize=(8, 6))
plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Solution of y"'' + 4y = x')
plt.grid(True)

#time points for integration for equation two 
# Time span for integration > can be adjust if need upon 
t = np.linspace(0, 10, 500)  

#Integrate the ODE using odeint
solution = odeint(odefunc2, y0, t)

#Extract y(t) from the solution
y = solution[:, 0]
#Plot the solution using Matplotlib
plt.plot(t, y, label='Solution')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.title('Solution of y"'' + y = 4')
plt.grid(True)

#Green's Function section 

# solve the first equation y'' + 4y = x using Green's function
#Define the system of equations for the first equation  y'' + 4y = x
def system(y, x):
    y0, y1 = y
    dydx = [y1, x - 4 * y0]
    return dydx

#Solve the system numerically for a given x value
def solve_system(x_value):
    x_span = np.linspace(0, x_value, 100)  # Range of x values
    y_init = [0, 0]  # Initial conditions: y(0) = 0, y'(0) = 0
    y_solution = odeint(system, y_init, x_span)
    return y_solution[-1, 0]  # Return y(x_value)

# solve the second  equation y'' + y = 4 using Green's function
#Define the system of equations for the second equation  y'' + 4y = x
def system2(y, t, x):
    y0, y1 = y
    dydt = [y1, 4 - y0] if t < x else [y1, 0]  
    return dydt


#solve the system numerically for equation 2
def solve_system2(x_value):
    t_span = np.linspace(0, x_value, 1000)  # Range of t values
    y_init = [0, 0]  # Initial conditions: y(0) = 0, y'(0) = 0
    y_solution = odeint(system2, y_init, t_span, args=(x_value,))
    return y_solution[-1, 0]  # Return y(x_value)

#Calculate the Green's function for a range of x values for equation 1
# Range of x values for plotting
x_values = np.linspace(0, 10, 100)  
green_function_values = [solve_system(x) for x in x_values]

#Plot the Green's function for equation 1
plt.figure(figsize=(8, 6))
plt.plot(x_values, green_function_values, label="Green's function")
plt.xlabel('x')
plt.ylabel("Green's function value")
plt.title('Solution of y"'' + 4y = x')
plt.legend()
plt.grid(True)

#Calculate the Green's function for a range of x values for equation 2
# Range of x values for plotting
x_values = np.linspace(0, 10, 100)  
green_function_values = [solve_system2(x) for x in x_values]

#Plot the Green's function for equation 2
plt.figure(figsize=(8, 6))
plt.plot(x_values, green_function_values, label="Green's function")
plt.xlabel('x')
plt.ylabel("Green's function value")
plt.title('Solution of y"'' + y = 4')
plt.legend()
plt.grid(True)
plt.show()

