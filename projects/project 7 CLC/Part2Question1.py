#Angel Velazquez and Jordan Scott
#CST-305 
#Project 7:  2 - Question 1
import numpy as np
import matplotlib.pyplot as plt

# Provided data from the user's table
arrival_times = np.arange(1, 16)  # Since arrivals are every minute
service_durations = np.array([2.22, 1.76, 2.13, 0.14, 0.76, 0.70, 0.47, 
                              0.22, 0.18, 2.41, 0.41, 0.46, 1.37, 0.27, 0.27])

# Initialize variables
service_start_times = np.zeros(len(arrival_times))
exit_times = np.zeros(len(arrival_times))
time_in_queue = np.zeros(len(arrival_times))
customers_in_system = [0, 1, 2, 2, 2, 3, 4, 3, 2, 0, 1, 2, 1, 1, 0]
customers_in_queue = [0,0,1,1,1,2,3,2,1,0,0,1,0,0,0] 

# Assume the system is empty at t = 0
service_start_times[0] = arrival_times[0]
exit_times[0] = arrival_times[0] + service_durations[0]

# Simulate the queue for the rest of the customers
for i in range(1, len(arrival_times)):
    # Service start time is either the arrival time or the exit time of the previous customer, whichever is later
    service_start_times[i] = max(arrival_times[i], exit_times[i-1])
    # Exit time is service start time plus service duration
    exit_times[i] = service_start_times[i] + service_durations[i]
    # Time in queue is the service start time minus the arrival time
    time_in_queue[i] = service_start_times[i] - arrival_times[i]
    # Number in system and in queue can only be calculated once we have all exit times


# Lq calculation (time average number in queue)
total_time = 15.27  # The time that the last customer exits the system
area_under_curve = np.trapz(customers_in_queue, dx=1)  # Trapezoidal approximation
# Let's correct the calculation of Lq and Lq(A)

# To get the total time spent in queue by all customers, we sum the time each customer spends in queue.
total_time_in_queue = np.sum(time_in_queue)

# To get Lq, we divide the total time spent in queue by all customers by the total observation time.
Lq = total_time_in_queue / total_time

# For Lq(A), we need to consider the queue length at the time of each customer's arrival.
# To get Lq(A), we average the queue lengths seen by each arriving customer.
Lq_A = np.mean(customers_in_queue)

print(Lq, Lq_A )


# (1) Customer arrival time as a function of service start time
plt.figure(figsize=(10, 6))
plt.plot(arrival_times, service_start_times, marker='o')
plt.title('Arrival Time vs Service Start Time')
plt.xlabel('Arrival Time (min)')
plt.ylabel('Service Start Time (min)')

# (2) Customer arrival time as a function of exit time
plt.figure(figsize=(10, 6))
plt.plot(arrival_times, exit_times, marker='o', color='green')
plt.title('Arrival Time vs Exit Time')
plt.xlabel('Arrival Time (min)')
plt.ylabel('Exit Time (min)')

# (3) Customer arrival time as a function of time in queue
plt.figure(figsize=(10, 6))
plt.plot(arrival_times, time_in_queue, marker='o', color='red')
plt.title('Arrival Time vs Time in Queue')
plt.xlabel('Arrival Time (min)')
plt.ylabel('Time in Queue (min)')

# (4) Customer arrival time as a function of the number of customers in system
plt.figure(figsize=(10, 6))
plt.plot(arrival_times, customers_in_system, marker='o', color='purple')
plt.title('Arrival Time vs Number in System')
plt.xlabel('Arrival Time (min)')
plt.ylabel('Number in System')

#TODO : 
# (5) Customer arrival time as a function of number of customers in queue
plt.figure(figsize=(10, 6))
plt.plot(arrival_times, customers_in_queue, marker='o', color='brown')
plt.title('Arrival Time vs Number in Queue')
plt.xlabel('Arrival Time (min)')
plt.ylabel('Number in Queue')
plt.show()
