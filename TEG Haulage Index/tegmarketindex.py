import webbrowser
import pandas as pd

# URL of the webpage
url = 'https://transportexchangegroup.com/road-transport-price-index/'

# Open the webpage
webbrowser.open(url)

# Manually input data as a list of lists (each inner list represents a column)
specific_x_values = ['Jan 20', 'Feb 20', 'Mar 20', 'Apr 20', 'May 20', 'Jun 20', 'Jul 20', 'Aug 20', 'Sep 20', 'Oct 20', 'Nov 20', 'Dec 20', 'Jan 21', 'Feb 21', 'Mar 21', 'Apr 21', 'May 21', 'Jun 21', 'Jul 21', 'Aug 21', 'Sep 21', 'Oct 21', 'Nov 21', 'Dec 21', 'Jan 22', 'Feb 22', 'Mar 22', 'Apr 22', 'May 22', 'Jun 22', 'Jul 22', 'Aug 22', 'Sep 22', 'Oct 22', 'Nov 22', 'Dec 22', 'Jan 23', 'Feb 23', 'Mar 23', 'Apr 23', 'May 23', 'Jun 23', 'Jul 23', 'Aug 23', 'Sep 23', 'Oct 23', 'Nov 23', 'Dec 23', 'Jan 24', 'Feb 24', 'Mar 24']
teg_market_index = [101.2, 97.7, 99.1, 98.1,  98.2, 98.1, 99, 101.6, 103.2,  103.6,  102.7, 109.9, 100.8, 98.7, 101.4, 109.6, 112.5, 118.4, 121, 124.2, 129.6, 128.2, 126.3, 130.3, 116.8, 110.1, 112.2, 117.5, 117.8, 122, 122.9, 123.3, 126.8, 126.8, 123.6, 130.5, 118.7, 114.8, 115.3, 118.4, 119.2, 122.3, 119.7, 119.4, 123.3, 120.5, 122.2, 127, 116.2, 114.7, 117.7]
courier_vehicles = [102.1, 98.9, 100.8, 106.3, 103, 102.9, 101, 104, 105, 105.1, 103.2, 110.7, 103.3, 101.6, 102.6, 109, 111.7, 117, 119.6, 120.8, 124.7, 123.5, 122.1, 126, 115.7, 110.5, 113.3, 118.7, 119.6, 124.9, 128.3, 128.2, 131.4, 128.6, 129.2, 136.9, 126.1, 121.6, 120.7, 123.1, 123.4, 125.9, 124.9, 124, 127.4, 125.5, 128, 132.8, 122.5, 119.2, 121.7]
haulage_vehicles = [99.7, 96, 96.9, 89.9, 93.2, 93.2, 96.9, 98.7, 100.8, 101.6, 102.2, 108.8, 97.8, 95.5, 100.2, 110.4, 113.7, 120.4, 123, 129.4, 137.3, 135.1, 132.3, 136.8, 118.2, 109.5, 110.9, 116.1, 115.6, 118.5, 116.8, 117.8, 121.2, 118.8, 116.9, 122, 110.4, 107.2, 109.5, 113.4, 114.8, 118.1, 113.9, 114.3, 118.4, 114.9, 115.4, 120.1, 109.7, 111.5, 113.5]

# Convert the list 'fbx_value' to a pandas Series
teg_market_index_series = pd.Series(teg_market_index)

# Calculate percentage change from the last value
latest_value = teg_market_index_series.iloc[-1]
previous_month_value = teg_market_index_series.iloc[-2]
last_year_value = teg_market_index_series.iloc[-13]
monthly_change = ((latest_value - previous_month_value) / previous_month_value) * 100
annual_change = ((latest_value - last_year_value) / last_year_value) * 100

monthly_change = round(monthly_change,1)
annual_change =  round(annual_change,1)

# Print or use the calculated changes as needed
print("Latest value:", teg_market_index_series.iloc[-1])
print("Monthly Change:", monthly_change)
print("Annual Change:", annual_change)

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Set Arial as the default font family
plt.rcParams['font.family'] = 'Arial'

# Visualize the data
fig, ax = plt.subplots(figsize=(20.59 / 2.54, 10.64 / 2.54)) # Adjust the size as needed
plt.plot(specific_x_values,teg_market_index, label='TEG Market Index (Jan 2019 = 100)', color='#3E71B3')
plt.plot(specific_x_values,courier_vehicles, label='Courier Vehicles (Jan 2019 = 100)', color='#5BAA7D')
plt.plot(specific_x_values,haulage_vehicles, label='Haulage Vehicles (Jan 2019 = 100)', color='#BF7A45')


plt.ylabel('Index', color='#797878', fontsize=8)
plt.title('UK Haulage', color='#001E60', fontsize=12)
plt.xticks(rotation=90, fontsize=7, color='#797878') # Rotate x-axis labels by 45 degrees
plt.yticks(fontsize=9, color='#797878')
plt.legend(fontsize=8)

# Add horizontal gridlines
plt.grid(axis='y', linestyle='-', color='#D9D9D9')

# Get the axes object
ax = plt.gca()

# Remove the top and right spines (lines) of the box
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Remove the line of the y-axis
ax.spines['left'].set_color('none')

# Change the color of the x-axis line
ax.spines['bottom'].set_color('#D9D9D9')

# Set bottom value of y-axis to 0
plt.ylim(bottom=80)

# Remove minor ticks
plt.tick_params(axis='both', which='both', length=0)

fig.set_size_inches(20.59 / 2.54, 10.64 / 2.54)

# Set the scale of the y-axis to go up by increments of 500
ax.yaxis.set_major_locator(MultipleLocator(10))

# Adjust y-axis limit
max_value = max(max(teg_market_index), max(courier_vehicles), max(haulage_vehicles))
plt.ylim(bottom=80, top=max_value + 10)

# Save the figure without extra whitespace
plt.savefig(r'C:\Users\Uros.Milosevic\PycharmProjects\pythonProject\-Graphs\tegmarketindex.pdf', bbox_inches='tight', pad_inches=0.1, format="pdf")

plt.show()
