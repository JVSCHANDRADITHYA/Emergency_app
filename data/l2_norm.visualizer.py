import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
file_path = r"dataset\Accelerometer.csv" # Replace with actual path
df = pd.read_csv(file_path)

# Extract data
time = df.iloc[:, 0]  # First column: Time elapsed
x = df.iloc[:, 1]  # Second column: X-axis acceleration
y = df.iloc[:, 2]  # Third column: Y-axis acceleration
z = df.iloc[:, 3]  # Fourth column: Z-axis acceleration

# Compute L2 norm
l2_norm = np.sqrt(x**2 + y**2 + z**2)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(time, l2_norm, label='L2 Norm of Accelerometer Data', color='b')
plt.xlabel('Time (s)')
plt.ylabel('L2 Norm')
plt.title('Accelerometer L2 Norm Over Time')
plt.legend()
plt.grid()
plt.show()
