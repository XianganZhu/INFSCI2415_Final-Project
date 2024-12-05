import pandas as pd
import matplotlib.pyplot as plt

file_path = 'earthquake_data.csv'
earthquake_data = pd.read_csv(file_path)

outer_counts = earthquake_data['tsunami'].value_counts()
outer_labels = ['No Tsunami', 'Tsunami']
outer_percentages = [f"{count / sum(outer_counts) * 100:.1f}%" for count in outer_counts]
tsunami_data = earthquake_data[earthquake_data['tsunami'] == 1]
inner_data = tsunami_data['continent'].value_counts()
inner_values = inner_data.values
inner_labels = inner_data.index.tolist()
outer_colors = ['#4C72B0', '#55A868']
inner_colors = ['#FFA07A', '#FA8072', '#E9967A', '#CD5C5C', '#8B0000'][:len(inner_labels)]
fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(
    outer_counts,
    labels=[f"{label} ({percent})" for label, percent in zip(outer_labels, outer_percentages)],
    colors=outer_colors,
    radius=1,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    startangle=90,
)
wedges, texts = ax.pie(
    inner_values,
    colors=inner_colors,
    radius=0.7,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    startangle=90,
)

plt.legend(
    wedges,
    [f"{label} ({value / inner_data.sum() * 100:.1f}%)" for label, value in zip(inner_labels, inner_values)],
    title="Tsunami by Area",
    loc="center left",
    bbox_to_anchor=(1, 0.5),
)
plt.title('Tsunami Ratios: Overall and by Area', fontsize=16)
plt.show()