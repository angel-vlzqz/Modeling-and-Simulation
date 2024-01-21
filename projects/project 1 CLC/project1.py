# Jordan Scott
# Angel Velazquez
# 01/19/2024

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def temperature_model(y, t, h, A):
    # ODE representing the temperature increase per watt
    dydt = 1 / (h * A)
    return dydt

def main():
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
    plt.plot(t, solution, label='Temperature Increase per Watt (Celcius)')
    plt.xlabel('Time (Seconds)')
    plt.ylabel('Temperature Increase per Watt (Celcius)')
    plt.title('Temperature Increase per Watt Over Time (Celcius)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
