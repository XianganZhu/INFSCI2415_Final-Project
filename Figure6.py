import pandas as pd
import matplotlib.pyplot as plt

file_path = 'earthquake_data.csv'
earthquake_data = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))
colors = earthquake_data['tsunami'].map({0: 'blue', 1: 'red'})
sizes = earthquake_data['sig'] / 50  # Normalize for better visibility
plt.scatter(earthquake_data['magnitude'], earthquake_data['depth'], c=colors, s=sizes, alpha=0.6)
plt.title('Depth vs Magnitude (Color: Tsunami)')
plt.xlabel('Magnitude')
plt.ylabel('Depth (km)')
plt.grid(True)
plt.show()