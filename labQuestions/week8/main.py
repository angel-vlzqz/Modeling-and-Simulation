import matplotlib.pyplot as plt

# Sample data
time = [1, 2, 3, 4, 5]  # X-axis values representing time
metric1 = [0.8, 0.7, 0.9, 0.6, 0.5]  # Y-axis values for metric 1
metric2 = [0.6, 0.5, 0.7, 0.4, 0.3]  # Y-axis values for metric 2
metric3 = [0.9, 0.8, 0.7, 0.6, 0.5]  # Y-axis values for metric 3

# Plotting the line graph
plt.plot(time, metric1, label='Metric 1', color='red')
plt.plot(time, metric2, label='Metric 2', color='blue')
plt.plot(time, metric3, label='Metric 3', color='green')

# Adding labels and title
plt.xlabel('Time')
plt.ylabel('Data Integrity')
plt.title('Changes in Data Integrity of Storage System')

# Adding legend
plt.legend()

# Displaying the graph
plt.show()
