import webbrowser
import pandas as pd

# URL of the webpage
url = 'https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/g6si/mm22'
url1 = 'https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/fsp7/ppi'
url2  = 'https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/fsp9/ppi'

# Open the webpage
webbrowser.open(url)
webbrowser.open(url1)
webbrowser.open(url2)

# Manually input data as a list of lists (each inner list represents a column)
specific_x_values = ['Jan 20', 'Feb 20', 'Mar 20', 'Apr 20', 'May 20', 'Jun 20', 'Jul 20', 'Aug 20', 'Sep 20', 'Oct 20', 'Nov 20', 'Dec 20', 'Jan 21', 'Feb 21', 'Mar 21', 'Apr 21', 'May 21', 'Jun 21', 'Jul 21', 'Aug 21', 'Sep 21', 'Oct 21', 'Nov 21', 'Dec 21', 'Jan 22', 'Feb 22', 'Mar 22', 'Apr 22', 'May 22', 'Jun 22', 'Jul 22', 'Aug 22', 'Sep 22', 'Oct 22', 'Nov 22', 'Dec 22', 'Jan 23', 'Feb 23', 'Mar 23', 'Apr 23', 'May 23', 'Jun 23', 'Jul 23', 'Aug 23', 'Sep 23', 'Oct 23', 'Nov 23', 'Dec 23', 'Jan 24', 'Feb 24', 'Mar 24']
output_domestic = [106.1, 106.3, 106.3, 106.1, 106.2, 106.6, 106.6, 106.5, 106.6, 106.2, 106.5, 106.7, 107.3, 107.9, 108.0, 108.6, 109.2, 109.4, 109.6, 109.6, 110.2, 111.0, 111.8, 112.5, 113.7, 114.6, 115.8, 118.2, 120.6, 123.6, 126.0, 126.8, 128.2, 129.5, 130.4, 131.3, 132.4, 132.9, 133.4, 134.3, 134.5, 134.8, 134.5, 133.8, 133.4, 133.3, 133.6, 133.6, 133.5, 133.6, 133.7]
input_domestic = [110.4, 110.8, 110.8, 110.3, 111.5, 111.4, 111.7, 110.9, 111.7, 112.0, 112.5, 113.7, 113.7, 115.4, 117.1, 118.0, 120.3, 118.2, 117.3, 116.7, 117.5, 119.0, 121.3, 124.0, 124.5, 126.0, 127.1, 133.8, 137.0, 139.9, 140.6, 139.6, 141.8, 144.4, 145.1, 146.1, 146.0, 145.4, 146.5, 144.6, 145.2, 142.5, 141.3, 141.0, 140.5, 141.5, 142.3, 143.4, 143.1, 142.7, 142.8]
input_imported = [120.6, 121.3, 123.3, 120.3, 117.8, 116.1, 116.2, 115.8, 117.5, 120.7, 123.2, 123.0, 121.7, 119.3, 118.8, 118.2, 117.9, 117.3, 119.4, 118.7, 120.8, 121.2, 124.8, 126.7, 128.7, 129.7, 132.4, 139.1, 143.2, 144.7, 147.6, 149.3, 156.7, 159.2, 160.3, 160.6, 164.9, 170.2, 172.5, 173.2, 176.7, 170.2, 170.6, 171.0, 171.9, 173.1, 172.1, 172.6, 171.7, 171.0, 169.5]

# Convert the list 'fbx_value' to a pandas Series
output_domestic_series = pd.Series(output_domestic)
input_domestic_series = pd.Series(input_domestic)
input_imported_series = pd.Series(input_imported)

# Calculate percentage change from the last value
latest_value_output_domestic = output_domestic_series.iloc[-1]
previous_month_value_output_domestic = output_domestic_series.iloc[-2]
last_year_value_output_domestic = output_domestic_series.iloc[-13]
monthly_change_output_domestic = ((latest_value_output_domestic - previous_month_value_output_domestic) / previous_month_value_output_domestic) * 100
annual_change_output_domestic = ((latest_value_output_domestic - last_year_value_output_domestic) / last_year_value_output_domestic) * 100

latest_value_input_domestic = input_domestic_series.iloc[-1]
previous_month_value_input_domestic = input_domestic_series.iloc[-2]
last_year_value_input_domestic = input_domestic_series.iloc[-13]
monthly_change_input_domestic = ((latest_value_input_domestic - previous_month_value_input_domestic) / previous_month_value_input_domestic) * 100
annual_change_input_domestic = ((latest_value_input_domestic- last_year_value_input_domestic) / last_year_value_input_domestic) * 100

latest_value_input_imported = input_imported_series.iloc[-1]
previous_month_value_input_imported = input_imported_series.iloc[-2]
last_year_value_input_imported = input_imported_series.iloc[-13]
monthly_change_input_imported = ((latest_value_input_imported - previous_month_value_input_imported) / previous_month_value_input_imported) * 100
annual_change_input_imported = ((latest_value_input_imported - last_year_value_input_imported) / last_year_value_input_imported) * 100

monthly_change_output_domestic = round(monthly_change_output_domestic,1)
annual_change_output_domestic =  round(annual_change_output_domestic,1)

monthly_change_input_domestic = round(monthly_change_input_domestic,1)
annual_change_input_domestic = round(annual_change_input_domestic,1)

monthly_change_input_imported = round(monthly_change_input_imported,1)
annual_change_input_imported = round(annual_change_input_imported,1)

# Print or use the calculated changes as needed
print("Latest value of Domestic Output:", output_domestic_series.iloc[-1])
print("Monthly Change in Domestic Output:", monthly_change_output_domestic)
print("Annual Change in Domestic Output:", annual_change_output_domestic)
print("-")
print("Latest value of Domestic Input:", input_domestic_series.iloc[-1])
print("Monthly Change in Domestic Input:", monthly_change_input_domestic)
print("Annual Change in Domestic Input:", annual_change_input_domestic)
print("-")
print("Latest value of Imported Input:", input_imported_series.iloc[-1])
print("Monthly Change in Imported Input:", monthly_change_input_imported)
print("Annual Change in Imported Input:", annual_change_input_imported)

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Set Arial as the default font family
plt.rcParams['font.family'] = 'Arial'

# Visualize the data
fig, ax = plt.subplots(figsize=(20.59 / 2.54, 10.64 / 2.54)) # Adjust the size as needed
plt.plot(specific_x_values,output_domestic, label='Output prices: food for domestic market (2015 = 100)', color='#3E71B3')
plt.plot(specific_x_values,input_domestic, label='Input prices: domestic food (2015 = 100)', color='#5BAA7D')
plt.plot(specific_x_values,input_imported, label='Input prices: imported food (2015 = 100)', color='#BF7A45')


plt.ylabel('Index', color='#797878', fontsize=8)
plt.title('Input prices (domestic food), input prices (imported food), output prices (food for domestic market)', color='#001E60', fontsize=12)
plt.xticks(rotation=90, fontsize=7, color='#797878') # Rotate x-axis labels by 45 degrees
plt.yticks(fontsize=9, color='#797878')
legend = plt.legend(fontsize=8, labelcolor='#001E60')

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
plt.ylim(bottom=100)

# Remove minor ticks
plt.tick_params(axis='both', which='both', length=0)

fig.set_size_inches(20.59 / 2.54, 10.64 / 2.54)

# Set the scale of the y-axis to go up by increments of 500
ax.yaxis.set_major_locator(MultipleLocator(10))

# Adjust y-axis limit
max_value = max(max(output_domestic), max(input_domestic), max(input_imported))
plt.ylim(bottom=100, top=max_value + 10)

# Save the figure without extra whitespace
plt.savefig(r'C:\Users\Uros.Milosevic\PycharmProjects\pricesDashboard\-Graphs\ppi.pdf', bbox_inches='tight', pad_inches=0.1, format="pdf")

plt.show()
