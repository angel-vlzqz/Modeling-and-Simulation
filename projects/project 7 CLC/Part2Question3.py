#Angel Velazquez and Jordan Scott
#CST-305 
#Project 7:  2 - Question 3
import numpy as np
import matplotlib.pyplot as plt

# Constants
lambda_ = 1  # Initial arrival rate
mu = 2       # Initial service rate

# Range for scaling factor k
k_values = np.linspace(1, 10, 100)

# Calculations
rho_values = [lambda_ / mu] * len(k_values)  # Utilization is constant
throughput_values = k_values * lambda_
mean_number_in_system = [lambda_ / (mu - lambda_)] * len(k_values)  # E[N] is constant
mean_time_in_system_values = [(lambda_ / (mu - lambda_)) / (k * lambda_) for k in k_values]

# Plotting
plt.figure(figsize=(14, 10))

plt.subplot(221)
plt.plot(k_values, rho_values, label='Utilization (ρ)')
plt.title('Utilization vs. k')
plt.xlabel('k')
plt.ylabel('Utilization')
plt.grid(True)

plt.subplot(222)
plt.plot(k_values, throughput_values, label='Throughput (X)')
plt.title('Throughput vs. k')
plt.xlabel('k')
plt.ylabel('Throughput')
plt.grid(True)

plt.subplot(223)
plt.plot(k_values, mean_number_in_system, label='Mean number in system (E[N])')
plt.title('Mean number in system vs. k')
plt.xlabel('k')
plt.ylabel('Mean number in system')
plt.grid(True)

plt.subplot(224)
plt.plot(k_values, mean_time_in_system_values, label='Mean time in system (E[T])')
plt.title('Mean time in system vs. k')
plt.xlabel('k')
plt.ylabel('Mean time in system')
plt.grid(True)

plt.tight_layout()
plt.show()