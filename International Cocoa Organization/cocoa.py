import webbrowser
import pandas as pd

# URL of the webpage
url = 'https://www.icco.org/statistics/'

# Open the webpage
webbrowser.open(url)

# Manually input data as a list of lists (each inner list represents a column)
specific_x_values = ['Jan 20', 'Feb 20', 'Mar 20', 'Apr 20', 'May 20', 'Jun 20', 'Jul 20', 'Aug 20', 'Sep 20', 'Oct 20', 'Nov 20', 'Dec 20', 'Jan 21', 'Feb 21', 'Mar 21', 'Apr 21', 'May 21', 'Jun 21', 'Jul 21', 'Aug 21', 'Sep 21', 'Oct 21', 'Nov 21', 'Dec 21', 'Jan 22', 'Feb 22', 'Mar 22', 'Apr 22', 'May 22', 'Jun 22', 'Jul 22', 'Aug 22', 'Sep 22', 'Oct 22', 'Nov 22', 'Dec 22', 'Jan 23', 'Feb 23', 'Mar 23', 'Apr 23', 'May 23', 'Jun 23', 'Jul 23', 'Aug 23', 'Sep 23', 'Oct 23', 'Nov 23', 'Dec 23', 'Jan 24', 'Feb 24', 'Mar 24']
cocoa_values = [2603.07, 2716.21, 2338.47, 2270.24, 2315.82, 2228.63, 2101.74, 2348.68, 2457.9, 2292.06, 2358.18, 2407.2, 2391.41, 2405.44, 2462.47, 2368.33, 2412.86, 2366.23, 2327.1, 2484.31, 2558.09, 2567.57, 2393.33, 2384.98, 2467.36, 2550.94, 2461.38, 2455.35, 2366.62, 2321.78, 2239.58, 2270.57, 2219.69, 2245.01, 2382.32, 2455.8, 2540.99, 2587.36, 2669.13, 2823.42, 2904.32, 3124.22, 3348.39, 3444.08, 3625.34, 3691.61, 4096.16, 4250.17, 4452.6, 5640.09, 7435.43]

# Convert the list 'fbx_value' to a pandas Series
cocoa_values_series = pd.Series(cocoa_values)

# Calculate percentage change from the last value
latest_value = cocoa_values_series.iloc[-1]
previous_month_value = cocoa_values_series.iloc[-2]
last_year_value = cocoa_values_series.iloc[-13]
monthly_change = ((latest_value - previous_month_value) / previous_month_value) * 100
annual_change = ((latest_value - last_year_value) / last_year_value) * 100

monthly_change = round(monthly_change,1)
annual_change = round(annual_change,1)

# Print or use the calculated changes as needed
print("Latest value:", cocoa_values_series.iloc[-1])
print("Monthly Change:", monthly_change)
print("Annual Change:", annual_change)

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Set Arial as the default font family
plt.rcParams['font.family'] = 'Arial'

# Visualize the data
fig, ax = plt.subplots(figsize=(20.59 / 2.54, 10.64 / 2.54)) # Adjust the size as needed
plt.plot(specific_x_values,cocoa_values, label='Cocoa ($/tonne)', color='#3E71B3')

plt.ylabel('Price, $', color='#797878', fontsize=8)
plt.title('Cocoa', color='#001E60', fontsize=12)
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
ax.yaxis.set_major_locator(MultipleLocator(500))

# Adjust y-axis limit
max_value = max(cocoa_values)
plt.ylim(bottom=1000, top=max_value + 500)

# Save the figure without extra whitespace
plt.savefig(r'C:\Users\Uros.Milosevic\PycharmProjects\pythonProject\-Graphs\cocoa.pdf', bbox_inches='tight', pad_inches=0.1, format="pdf")

plt.show()