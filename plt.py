import matplotlib.pyplot as plt

# Data
iterations = list(range(1, 21))
target_values1 = [
    0.9929, 0.9942, 0.9929, 0.9929, 0.9942, 
    0.9936, 0.9929, 0.9942, 0.9942, 0.9942, 
    0.9949, 0.9949, 0.9923, 0.9929, 0.9923, 
    0.9929, 0.9949, 0.9942, 0.9929, 0.9936
]
prompt_indices1 = [
    50.19, 127.4, 98.09, 80.22, 20.91, 
    6.648, 126.3, 48.89, 127.4, 48.18, 
    19.97, 19.16, 17.89, 46.64, 22.41, 
    129.2, 19.55, 64.38, 63.05, 65.55
]




target_values2 = [
    0.9619, 0.962, 0.962, 0.9625, 0.961, 
    0.9617, 0.9625, 0.9615, 0.9607, 0.9591, 
    0.9607, 0.9616, 0.9612, 0.961, 0.9611, 
    0.9614, 0.9616, 0.9606, 0.9615, 0.961
]

prompt_indices2 = [
    37.45, 95.07, 73.2, 59.87, 15.6, 
    50.95, 59.87, 65.16, 56.78, 61.71, 
    96.37, 94.0, 58.75, 74.28, 72.26, 
    36.49, 38.4, 49.86, 51.88, 92.71
]
target_values3 = [
    0.3352, 0.121, 0.3352, 0.2917, 0.121, 
    0.121, 0.3352, 0.121, 0.121, 0.2917, 
    0.121, 0.121, 0.2917, 0.3352, 0.121, 
    0.121, 0.121, 0.3352, 0.2917, 0.2917
]

prompt_indices3 = [
    37.45, 95.07, 73.2, 59.87, 15.6, 
    46.61, 73.2, 32.54, 40.14, 35.97, 
    70.37, 75.43, 58.25, 56.26, 54.6, 
    57.13, 36.86, 37.77, 55.83, 58.99
]

target_values4 = [
    0.1843, 0.1747, 0.2306, 0.1747, 0.1747, 
    0.2306, 0.1747, 0.2351, 0.2306, 0.1843, 
    0.1747, 0.1843, 0.1747, 0.1843, 0.2351, 
    0.2351, 0.1747, 0.1843, 0.2306, 0.2306
]

prompt_indices4 = [
    50.19, 127.4, 98.09, 80.22, 20.91, 
    98.04, 109.6, 0.0, 6.37, 64.38, 
    36.59, 2.929, 8.105, 5.393, 0.6095, 
    99.39, 100.5, 96.86, 98.88, 1.432
]

target_values5 = [
    0.1747, 0.1753, 0.1747, 0.1747, 0.2351, 
    0.2306, 0.1843, 0.1753, 0.1747, 0.2351, 
    0.1747, 0.2306, 0.2306, 0.2351, 0.2351, 
    0.2351, 0.2351, 0.1843, 0.2306, 0.2306
]

prompt_indices5 = [
    35.58, 90.32, 69.54, 56.87, 14.82, 
    5.559, 13.78, 34.66, 15.18, 89.57, 
    88.27, 31.02, 5.559, 14.65, 89.29, 
    30.63, 30.18, 29.68, 5.079, 4.559
]

target_values = [
    0.121, 0.121, 0.121, 0.121, 0.121, 
    0.2917, 0.2917, 0.121, 0.121, 0.121, 
    0.121, 0.121, 0.121, 0.2917, 0.121, 
    0.121, 0.121, 0.121, 0.121, 0.2917
]

prompt_indices = [
    35.58, 90.32, 69.54, 56.87, 14.82, 
    0.001105, 0.7833, 4.558, 46.23, 79.93, 
    25.2, 63.2, 1.768, 0.3968, 51.56, 
    40.9, 74.74, 85.13, 30.4, 0.6101
]

# Find the maximum target value
max_target = max(target_values)

# Find all iterations with the maximum target value
max_indices = [i for i, value in enumerate(target_values) if value == max_target]

# Plot the data
plt.figure(figsize=(10, 6))

# Plot the line showing target values
plt.plot(iterations, target_values, marker='o', color='blue')

# Highlight the maximum target values with corresponding prompt indices
for i in max_indices:
    plt.annotate({prompt_indices[i]}, 
                 (iterations[i], target_values[i]), 
                 textcoords="offset points", 
                 xytext=(0,5), ha='center', color='red',fontsize=6)

# Remove the axes titles for a clean look
plt.xticks(iterations)
plt.yticks(sorted(set(target_values)))
plt.grid(True)

plt.show()
