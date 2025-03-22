acc_path = r"C:\Users\adith\Downloads\BITS_CAFETERIA-2025-03-22_11-36-26\Accelerometer.csv"


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
acc_data = pd.read_csv(acc_path)  

# Plot the data
plt.plot(acc_data['time'], acc_data['x'], label='x')    
plt.show()