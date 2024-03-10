import numpy as np
import matplotlib.pyplot as plt

# Bak-Tang-Wiesenfeld sandpile model
def sandpile_model(size):
    grid = np.zeros((size, size), dtype=int)
    grid[size // 2, size // 2] = 1

    while True:
        unstable_cells = np.argwhere(grid >= 4)
        if len(unstable_cells) == 0:
            break

        for cell in unstable_cells:
            x, y = cell
            grid[x, y] -= 4
            if x > 0:
                grid[x - 1, y] += 1
            if x < size - 1:
                grid[x + 1, y] += 1
            if y > 0:
                grid[x, y - 1] += 1
            if y < size - 1:
                grid[x, y + 1] += 1

    return grid

# Forest-fire model
def forest_fire_model(size, p, f):
    grid = np.zeros((size, size), dtype=int)
    grid[size // 2, size // 2] = 1

    while True:
        for i in range(size):
            for j in range(size):
                if grid[i, j] == 1:
                    if np.random.random() < f:
                        grid[i, j] = 2
                elif grid[i, j] == 2:
                    grid[i, j] = 0
                elif grid[i, j] == 0:
                    if np.random.random() < p:
                        grid[i, j] = 1

        if np.sum(grid == 1) == 0:
            break

    return grid

# Sandpile model with a driving force
def sandpile_model_with_driving_force(size, driving_force):
    grid = np.zeros((size, size), dtype=int)
    grid[size // 2, size // 2] = driving_force

    while True:
        unstable_cells = np.argwhere(grid >= 4)
        if len(unstable_cells) == 0:
            break

        for cell in unstable_cells:
            x, y = cell
            grid[x, y] -= 4
            if x > 0:
                grid[x - 1, y] += 1
            if x < size - 1:
                grid[x + 1, y] += 1
            if y > 0:
                grid[x, y - 1] += 1
            if y < size - 1:
                grid[x, y + 1] += 1

    return grid

# Plotting the models
size = 100

plt.subplot(1, 3, 1)
plt.imshow(sandpile_model(size), cmap='hot', interpolation='nearest')
plt.title('Bak-Tang-Wiesenfeld Sandpile Model')

plt.subplot(1, 3, 2)
plt.imshow(forest_fire_model(size, 0.01, 0.1), cmap='hot', interpolation='nearest')
plt.title('Forest-Fire Model')

plt.subplot(1, 3, 3)
plt.imshow(sandpile_model_with_driving_force(size, 10), cmap='hot', interpolation='nearest')
plt.title('Sandpile Model with Driving Force')

plt.tight_layout()
plt.show()
