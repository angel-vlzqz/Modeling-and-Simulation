#Jordan Scott Angel Velazquez
# CST-305
#Degradation of Data Integrity
#part 2

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Creating an array of t values
t_values = np.linspace(-0.5, 1.5, 1000)

# creating the plot
plt.figure(figsize=(10, 7))

# Plot e^(-5t) and -e^(-5t) for comparison to the image
plt.plot(t_values, np.exp(-5*t_values), label="e^(-5t)")
plt.plot(t_values, -np.exp(-5*t_values), label="-e^(-5t)")

# Adding the  labels and title
plt.xlabel('t')
plt.ylabel('Function Value')
plt.title('x(t) = e^(At)*C')
plt.legend()

# Show a grid
plt.grid(True)

# Showing the e^(At)*C the graph
plt.show()