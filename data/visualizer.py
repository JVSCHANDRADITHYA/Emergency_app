acc_path = r"dataset\Accelerometer.csv"
gravity_apth = r"dataset\TotalAcceleration.csv"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

acc_ac_data = pd.read_csv(acc_path)
# Load the data
acc_data = pd.read_csv(gravity_apth)  

# Plot the data
axes, fig = plt.subplots(2, 1, figsize=(10, 10))

fig[0].plot(acc_data['seconds_elapsed'], acc_data['x'], label='x')    
fig[0].plot(acc_data['seconds_elapsed'], acc_data['z'], label='z')    
fig[0].plot(acc_data['seconds_elapsed'], acc_data['y'], label='y')    

acc_ac_data

fig[1].plot(acc_ac_data['seconds_elapsed'], acc_ac_data['x'], label='x')
fig[1].plot(acc_ac_data['seconds_elapsed'], acc_ac_data['z'], label='z')
fig[1].plot(acc_ac_data['seconds_elapsed'], acc_ac_data['y'], label='y')
plt.show()