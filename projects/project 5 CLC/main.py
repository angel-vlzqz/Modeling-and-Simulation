import random
from tqdm import tqdm
import matplotlib.pyplot as plt
# System parameters
storage_size = 1000  # Total storage size in MB
critical_threshold = 0.8  # Critical threshold for storage usage

# File parameters
file_sizes = [10, 20, 30, 40, 50]  # Possible file sizes in MB
file_load_time = 2  # Time taken to load a file in seconds
file_access_time = 1  # Time taken to access a file in seconds
file_save_time = 3  # Time taken to save a file in seconds

# Fragmentation parameters
fragmentation_time = 5  # Time taken to defragment the file system in seconds
fragments_assembly_time = 2  # Time taken to assemble file fragments in seconds

def simulate_file_system():
    # Initialize storage
    storage_used = 0

    # Initialize metrics
    storage_usage = []
    fragmentation_count = 0

    # Simulate file operations
    with tqdm(total=storage_size, desc="Storage Usage") as pbar:
        while True:
            # Check if system is too slow
            if storage_used / storage_size > critical_threshold:
                print("System is too slow!")
                break

            # Generate random file size
            file_size = random.choice(file_sizes)

            # Check if enough space is available
            if storage_used + file_size > storage_size:
                print("Not enough space to save the file!")
                break

            # Update storage usage
            storage_used += file_size

            # Check if defragmentation is needed
            if storage_used / storage_size > critical_threshold:
                print("Defragmenting the file system...")
                # Perform defragmentation
                # ...
                fragmentation_count += 1

            # Update metrics
            storage_usage.append(storage_used)
            pbar.update(file_size)

            # Wait for some time before the next operation
            # ...

    # Display fragmentation count
    print(f"Fragmentation Count: {fragmentation_count}")

    # Plot storage usage graph
    plt.plot(storage_usage)
    plt.xlabel("Time")
    plt.ylabel("Storage Usage")
    plt.title("Storage Usage Over Time")
    plt.show()


# Run the simulation
simulate_file_system()
