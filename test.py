# Import necessary libraries
import matplotlib.pyplot as plt
from matplotlib import cm

# Define the data as a list of tuples
data = [(1.0, 1, 1), (0.5, 2, 1), (0.25, 3, 1), (0.125, 1, 2), (0.625, 2, 2), (0.375, 3, 2)]

# Extract the values and coordinates from the data
values = [d[0] for d in data]
x_coords = [d[1] for d in data]
y_coords = [d[2] for d in data]

# Generate the heatmap
fig, ax = plt.subplots()
ax.scatter(x_coords, y_coords, c=values, cmap="viridis")

# Show the plot
plt.show()
