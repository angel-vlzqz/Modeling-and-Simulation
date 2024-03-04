#Jordan Scott Angel Velazquez
# CST-305
#Degradation of Data Integrity
#part 1

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#𝑥̇=𝐴(𝑡)𝑥(𝑡)+𝑓(𝑡),𝑤𝑖𝑡ℎ 𝑓(𝑡)=0

# Define A(t) function
def A(t):
    return np.array([[-2, 0, 3],
                     [2, -3, 0],
                     [0, 1, -1]])

# Define f(t) function 
# f(t)=0
def f(t):
    return np.zeros_like(t) 

# Define differential equation
def equation(t, x):
    return np.dot(A(t), x) + f(t)

# Define time span
t_span = (0, 10)

# Define initial conditions
# initial values for x1, x2, x3
# arbitrary values for x1, x2, x3
x0 = [1, 1, 1] 

# Solve the differential equation
sol = solve_ivp(equation, t_span, x0, t_eval=np.linspace(0, 10, 100))

# Plot the solution
plt.plot(sol.t, sol.y[0], label='x1')
plt.plot(sol.t, sol.y[1], label='x2')
plt.plot(sol.t, sol.y[2], label='x3')
plt.xlabel('Time')
plt.ylabel('x')
plt.title('Solution of the system of differential equations')
plt.legend()
plt.grid(True)
plt.show()
