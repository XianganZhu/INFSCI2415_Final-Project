import pandas as pd
import matplotlib.pyplot as plt

file_path = 'earthquake_data.csv'
earthquake_data = pd.read_csv(file_path)

top_countries = earthquake_data['country'].value_counts().head(5)

plt.figure(figsize=(10, 6))
for i, country in enumerate(top_countries.index):
    magnitudes = earthquake_data[earthquake_data['country'] == country]['magnitude']
    plt.scatter([i] * len(magnitudes), magnitudes, alpha=0.7)

plt.xticks(range(len(top_countries)), top_countries.index)
plt.title('Magnitudes by Top 5 Countries')
plt.xlabel('Country')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()