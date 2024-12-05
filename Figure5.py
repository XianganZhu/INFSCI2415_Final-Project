import pandas as pd
import matplotlib.pyplot as plt

file_path = 'earthquake_data.csv'
earthquake_data = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))
plt.hist(earthquake_data['magnitude'], bins=20, color='blue', alpha=0.6, edgecolor='black')
plt.title('Distribution of Earthquake Magnitudes')
plt.xlabel('Magnitude')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()