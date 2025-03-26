import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate synthetic time-series data for CLLC converter (voltage, current, frequency)
np.random.seed(42)

# Time steps
time_steps = 1000

# Simulate time values (e.g., in seconds)
time = np.arange(time_steps)

# Simulate voltage (voltage might fluctuate over time)
voltage = 100 + 10 * np.sin(0.01 * time) + np.random.normal(0, 2, time_steps)

# Simulate current (current could also fluctuate, dependent on the voltage)
current = 10 + 0.5 * np.cos(0.02 * time) + np.random.normal(0, 1, time_steps)

# Simulate frequency (frequency can be controlled or vary based on certain factors)
frequency = 50 + 2 * np.sin(0.015 * time) + np.random.normal(0, 0.5, time_steps)

# Combine into a DataFrame
data = pd.DataFrame({
    'time': time,
    'voltage': voltage,
    'current': current,
    'frequency': frequency
})

# Plot the data
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(time, voltage, label='Voltage')
plt.legend()
plt.title('Voltage vs Time')

plt.subplot(3, 1, 2)
plt.plot(time, current, label='Current', color='orange')
plt.legend()
plt.title('Current vs Time')

plt.subplot(3, 1, 3)
plt.plot(time, frequency, label='Frequency', color='green')
plt.legend()
plt.title('Frequency vs Time')

plt.tight_layout()
plt.show()

# Save the generated data
data.to_csv('cllc_converter_data.csv', index=False)
