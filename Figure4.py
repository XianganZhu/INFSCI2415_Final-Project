import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

file_path = 'earthquake_data.csv'
earthquake_data = pd.read_csv(file_path)

latitude = earthquake_data['latitude']
longitude = earthquake_data['longitude']
depth = earthquake_data['depth']
grid_size = 100
lon_bins = np.linspace(longitude.min(), longitude.max(), grid_size)
lat_bins = np.linspace(latitude.min(), latitude.max(), grid_size)
depth_sum = np.zeros((grid_size - 1, grid_size - 1))
count = np.zeros((grid_size - 1, grid_size - 1))

for lat, lon, dep in zip(latitude, longitude, depth):
    lon_idx = np.searchsorted(lon_bins, lon) - 1
    lat_idx = np.searchsorted(lat_bins, lat) - 1
    if 0 <= lon_idx < grid_size - 1 and 0 <= lat_idx < grid_size - 1:
        depth_sum[lon_idx, lat_idx] += dep
        count[lon_idx, lat_idx] += 1

average_depth = np.divide(depth_sum, count, out=np.zeros_like(depth_sum), where=count != 0)

plt.figure(figsize=(16, 10))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_global()
ax.coastlines()
ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')
ax.add_feature(cfeature.OCEAN, facecolor='aqua')
ax.add_feature(cfeature.BORDERS, linestyle=':')
lon_centers = 0.5 * (lon_bins[:-1] + lon_bins[1:])
lat_centers = 0.5 * (lat_bins[:-1] + lat_bins[1:])
lon_grid, lat_grid = np.meshgrid(lon_centers, lat_centers)
heatmap = ax.pcolormesh(
    lon_grid, lat_grid, average_depth.T,
    cmap='viridis', shading='auto', transform=ccrs.PlateCarree()
)
cbar = plt.colorbar(heatmap, orientation='horizontal', pad=0.05)
cbar.set_label('Average Depth (km)')

plt.title('Earthquake Depth Heatmap', fontsize=16)
plt.show()
