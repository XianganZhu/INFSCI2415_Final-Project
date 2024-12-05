import pandas as pd
import matplotlib.pyplot as plt

file_path = 'earthquake_data.csv'
earthquake_data = pd.read_csv(file_path)

earthquake_data['date_time'] = pd.to_datetime(earthquake_data['date_time'], errors='coerce')

plt.figure(figsize=(12, 6))
plt.plot(earthquake_data['date_time'], earthquake_data['magnitude'], marker='o', linestyle='-', alpha=0.7)
plt.title('Temporal Trends of Earthquake Magnitudes')
plt.xlabel('Date')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()