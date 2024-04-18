import webbrowser
import pandas as pd

# URL of the webpage
url = 'https://tradingeconomics.com/commodity/uk-natural-gas'

# Open the webpage
webbrowser.open(url)


# Manually input data as a list of lists (each inner list represents a column)
specific_x_values = ['Jan 20', 'Feb 20', 'Mar 20', 'Apr 20', 'May 20', 'Jun 20', 'Jul 20', 'Aug 20', 'Sep 20', 'Oct 20', 'Nov 20', 'Dec 20', 'Jan 21', 'Feb 21', 'Mar 21', 'Apr 21', 'May 21', 'Jun 21', 'Jul 21', 'Aug 21', 'Sep 21', 'Oct 21', 'Nov 21', 'Dec 21', 'Jan 22', 'Feb 22', 'Mar 22', 'Apr 22', 'May 22', 'Jun 22', 'Jul 22', 'Aug 22', 'Sep 22', 'Oct 22', 'Nov 22', 'Dec 22', 'Jan 23', 'Feb 23', 'Mar 23', 'Apr 23', 'May 23', 'Jun 23', 'Jul 23', 'Aug 23', 'Sep 23', 'Oct 23', 'Nov 23', 'Dec 23', 'Jan 24', 'Feb 24', 'Mar 24']
uk_gas = [25.34, 22.93, 16.33, 13.87, 8.34, 16.22, 15.64, 28.95, 37, 40.91, 41.68, 55.82, 53.15, 39.79, 46.8, 60.24, 60.68,  85.87, 103.75, 127.71, 251.18, 165.98, 238.31, 170.64, 203.08, 237.78, 299.32, 163.68, 183.71, 248.3, 351.92, 458.9, 352.89, 300.74, 369.65, 186.05, 145.51, 115.54, 118.03, 88.53, 63.53, 91.22, 70.75, 85.73, 105.4, 124.07, 107.13, 80.71, 74.3, 61.58, 68.05]

# Convert the list 'fbx_value' to a pandas Series
uk_gas_series = pd.Series(uk_gas)

# Calculate percentage change from the last value
latest_value = uk_gas_series.iloc[-1]
previous_month_value = uk_gas_series.iloc[-2]
last_year_value = uk_gas_series.iloc[-13]
monthly_change = ((latest_value - previous_month_value) / previous_month_value) * 100
annual_change = ((latest_value - last_year_value) / last_year_value) * 100

monthly_change = round(monthly_change,1)
annual_change = round(annual_change,1)

# Print or use the calculated changes as needed
print("Latest value:", uk_gas_series.iloc[-1])
print("Monthly Change:", monthly_change)
print("Annual Change:", annual_change)


import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Set Arial as the default font family
plt.rcParams['font.family'] = 'Arial'

# Visualize the data
fig, ax = plt.subplots(figsize=(20.59 / 2.54, 10.64 / 2.54)) # Adjust the size as needed
plt.plot(specific_x_values,uk_gas, label='UK gas (£/thm)', color='#3E71B3')

plt.ylabel('Price, £', color='#797878', fontsize=8)
plt.title('UK natural gas', color='#001E60', fontsize=12)
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
plt.ylim(bottom=0)

# Remove minor ticks
plt.tick_params(axis='both', which='both', length=0)

fig.set_size_inches(20.59 / 2.54, 10.64 / 2.54)

# Set the scale of the y-axis to go up by increments of 500
ax.yaxis.set_major_locator(MultipleLocator(100))

# Adjust y-axis limit
max_value = max(uk_gas)
plt.ylim(bottom=0, top=max_value + 100)

# Save the figure without extra whitespace
plt.savefig(r'C:\Users\Uros.Milosevic\PycharmProjects\pythonProject\-Graphs\ukgas.pdf', bbox_inches='tight', pad_inches=0.1, format="pdf")

plt.show()