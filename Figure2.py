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
tsunami = earthquake_data[earthquake_data['tsunami'] == 1]
non_tsunami = earthquake_data[earthquake_data['tsunami'] == 0]
plt.scatter(tsunami['longitude'], tsunami['latitude'], c='red', s=50, alpha=0.7, label='Tsunami', edgecolor='k', transform=ccrs.PlateCarree())
plt.scatter(non_tsunami['longitude'], non_tsunami['latitude'], c='blue', s=20, alpha=0.5, label='No Tsunami', edgecolor='k', transform=ccrs.PlateCarree())
plt.legend(loc='lower left')
plt.title('Tsunami-Triggered vs Non-Tsunami Earthquakes', fontsize=16)
plt.show()
