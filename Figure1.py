import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import pandas as pd

file_path = 'earthquake_data.csv'
earthquake_data = pd.read_csv(file_path)

latitude = earthquake_data['latitude']
longitude = earthquake_data['longitude']
magnitude = earthquake_data['magnitude']

plt.figure(figsize=(16, 10))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_global()
ax.coastlines()
ax.stock_img()
scatter = plt.scatter(longitude, latitude, c=magnitude, cmap='Reds', s=magnitude*10, alpha=0.7, edgecolor='k', transform=ccrs.PlateCarree())
cbar = plt.colorbar(scatter, orientation='horizontal', pad=0.05)
cbar.set_label('Magnitude')
plt.title('Earthquake Locations on World Map', fontsize=16)
plt.show()