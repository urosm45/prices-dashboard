import webbrowser
import pandas as pd

# URL of the webpage
url = 'https://terminal.freightos.com/freightos-baltic-index-global-container-pricing-index/'

# Open the webpage
webbrowser.open(url)

# Manually input data as a list of lists (each inner list represents a column)
specific_x_values = ['Jan 20', 'Feb 20', 'Mar 20', 'Apr 20', 'May 20', 'Jun 20', 'Jul 20', 'Aug 20', 'Sep 20', 'Oct 20', 'Nov 20', 'Dec 20', 'Jan 21', 'Feb 21', 'Mar 21', 'Apr 21', 'May 21', 'Jun 21', 'Jul 21', 'Aug 21', 'Sep 21', 'Oct 21', 'Nov 21', 'Dec 21', 'Jan 22', 'Feb 22', 'Mar 22', 'Apr 22', 'May 22', 'Jun 22', 'Jul 22', 'Aug 22', 'Sep 22', 'Oct 22', 'Nov 22', 'Dec 22', 'Jan 23', 'Feb 23', 'Mar 23', 'Apr 23', 'May 23', 'Jun 23', 'Jul 23', 'Aug 23', 'Sep 23', 'Oct 23', 'Nov 23', 'Dec 23', 'Jan 24', 'Feb 24', 'Mar 24']
fbx_value = [1532, 1398, 1369.75, 1453, 1471, 1695.75, 1805.6, 1883.75, 2141.25, 2237, 2343.25, 2895.25, 4037, 4483, 4373.75, 4583.2, 5447.25, 6597.75, 8354.4, 10073.75, 10865.75, 10279.6, 9622.25, 9443.6, 9544.75, 9705.5, 9613, 9205, 8315.75, 7190.25, 6385, 5904.5, 4624.6, 3502, 3093.75, 2270.4, 2199.5, 2010.5, 1558.8,  1499.25, 1446.75, 1358.8, 1293.25, 1501.3925, 1359.714, 1076.2675, 1178.2125, 1283.56, 2909.15, 3390.15, 2917.34]

# Convert the list 'fbx_value' to a pandas Series
fbx_series = pd.Series(fbx_value)

# Calculate percentage change from the last value
latest_value = fbx_series.iloc[-1]
previous_month_value = fbx_series.iloc[-2]
last_year_value = fbx_series.iloc[-13]
monthly_change = ((latest_value - previous_month_value) / previous_month_value) * 100
annual_change = ((latest_value - last_year_value) / last_year_value) * 100

monthly_change = round(monthly_change,1)
annual_change = round(annual_change,1)

# Print or use the calculated changes as needed
print("Latest value:", fbx_series.iloc[-1])
print("Monthly Change:", monthly_change)
print("Annual Change:", annual_change)

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Set Arial as the default font family
plt.rcParams['font.family'] = 'Arial'

# Visualize the data
fig, ax = plt.subplots(figsize=(20.59 / 2.54, 10.64 / 2.54)) # Adjust the size as needed
plt.plot(specific_x_values,fbx_value, label='FBX', color='#3E71B3')

plt.ylabel('Index', color='#797878', fontsize=8)
plt.title('Freightos Baltic Index (FBX): Global Container Freight Index', color='#001E60', fontsize=12)
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
plt.ylim(bottom=1000)

# Remove minor ticks
plt.tick_params(axis='both', which='both', length=0)

fig.set_size_inches(20.59 / 2.54, 10.64 / 2.54)

# Set the scale of the y-axis to go up by increments of 500
ax.yaxis.set_major_locator(MultipleLocator(1000))

# Adjust y-axis limit
max_value = max(fbx_value)
plt.ylim(bottom=1000, top=max_value + 2000)

# Save the figure without extra whitespace
plt.savefig(r'C:\Users\Uros.Milosevic\PycharmProjects\pythonProject\-Graphs\globalcontainerfreightindex.pdf', bbox_inches='tight', pad_inches=0.1, format="pdf")

plt.show()

#check


