import webbrowser
import pandas as pd

# URL of the webpage
url = 'https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/evvq/mm22'
url1 = 'https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/evup/mm22'

# Open the webpage
webbrowser.open(url)
webbrowser.open(url1)

# Manually input data as a list of lists (each inner list represents a column)
specific_x_values = ['Jan 20', 'Feb 20', 'Mar 20', 'Apr 20', 'May 20', 'Jun 20', 'Jul 20', 'Aug 20', 'Sep 20', 'Oct 20', 'Nov 20', 'Dec 20', 'Jan 21', 'Feb 21', 'Mar 21', 'Apr 21', 'May 21', 'Jun 21', 'Jul 21', 'Aug 21', 'Sep 21', 'Oct 21', 'Nov 21', 'Dec 21', 'Jan 22', 'Feb 22', 'Mar 22', 'Apr 22', 'May 22', 'Jun 22', 'Jul 22', 'Aug 22', 'Sep 22', 'Oct 22', 'Nov 22', 'Dec 22', 'Jan 23', 'Feb 23', 'Mar 23', 'Apr 23', 'May 23', 'Jun 23', 'Jul 23', 'Aug 23', 'Sep 23', 'Oct 23', 'Nov 23', 'Dec 23', 'Jan 24', 'Feb 24', 'Mar 24']
paper_index = [106.3, 106.3, 106.1, 106.3, 106.2, 105.9,  105.9, 105.6, 106.5, 106.6, 106.6, 106.6, 105.8, 105.7, 106.5, 107.8, 109.5, 113.0, 114.4, 115.4, 118.1, 119.2, 121.2, 122.4, 126.3, 127.9, 129.8, 132.7, 136.7, 138.2, 140.5, 141.2, 141.9, 142.4, 142.5, 142.5, 142.8, 142.4, 141.6, 139.4, 137.5, 136.4, 134.2, 133.5, 133.4, 132.6, 132.6, 132.4, 131.5, 130.1, 129.7]
wood_index = [104.0, 103.4, 100.1, 99.6, 99.5, 99.7, 101.3, 101.3, 101.3, 101.8, 100.3, 101.8, 104.5, 106.2, 108.4, 113.2, 116.9, 119.4, 130.2, 143.5, 145.5, 146.7, 146.7, 147.8, 148.8, 149.2, 150.0, 155.9, 158.3, 158.6, 159.4, 159.8, 160.0, 159.8, 159.2, 157.5, 157.4, 158.7, 157.7, 156.7, 156.7, 152.4, 152.1, 151.6, 148.5, 145.8, 144.7, 144.6, 144.6, 151.8, 151.3]

# Convert the list 'fbx_value' to a pandas Series
paper_index_series = pd.Series(paper_index)
wood_index_series = pd.Series(wood_index)

# Calculate percentage change from the last value
latest_value_paper = paper_index_series.iloc[-1]
previous_month_value_paper = paper_index_series.iloc[-2]
last_year_value_paper = paper_index_series.iloc[-13]
monthly_change_paper = ((latest_value_paper - previous_month_value_paper) / previous_month_value_paper) * 100
annual_change_paper = ((latest_value_paper - last_year_value_paper) / last_year_value_paper) * 100

latest_value_wood = wood_index_series.iloc[-1]
previous_month_value_wood = wood_index_series.iloc[-2]
last_year_value_wood = wood_index_series.iloc[-13]
monthly_change_wood = ((latest_value_wood- previous_month_value_wood) / previous_month_value_wood) * 100
annual_change_wood = ((latest_value_wood - last_year_value_wood) / last_year_value_wood) * 100

monthly_change_paper = round(monthly_change_paper,1)
annual_change_paper =  round(annual_change_paper,1)

monthly_change_wood = round(monthly_change_wood,1)
annual_change_wood = round(annual_change_wood,1)

# Print or use the calculated changes as needed
print("Latest value of Paper Index:", paper_index_series.iloc[-1])
print("Monthly Change in Paper Index:", monthly_change_paper)
print("Annual Change in Paper Index:", annual_change_paper)
print("-")
print("Latest value of Wood Index:", wood_index_series.iloc[-1])
print("Monthly Change in Wood Index:", monthly_change_wood)
print("Annual Change in Wood Index:", annual_change_wood)

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Set Arial as the default font family
plt.rcParams['font.family'] = 'Arial'

# Visualize the data
fig, ax = plt.subplots(figsize=(20.59 / 2.54, 10.64 / 2.54)) # Adjust the size as needed
plt.plot(specific_x_values,paper_index, label='Corrugated paper and paperboard and containers of paper and paperboard for domestic market (2015 = 100)', color='#3E71B3')
plt.plot(specific_x_values,wood_index, label='Wooden containers for domestic market (2015 = 100)', color='#5BAA7D')


plt.ylabel('Index', color='#797878', fontsize=8)
plt.title('Packaging', color='#001E60', fontsize=12)
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
plt.ylim(bottom=90)

# Remove minor ticks
plt.tick_params(axis='both', which='both', length=0)

fig.set_size_inches(20.59 / 2.54, 10.64 / 2.54)

# Set the scale of the y-axis to go up by increments of 500
ax.yaxis.set_major_locator(MultipleLocator(10))

# Adjust y-axis limit
max_value = max(max(paper_index), max(wood_index))
plt.ylim(bottom=90, top=max_value + 20)

# Save the figure without extra whitespace
plt.savefig(r'C:\Users\Uros.Milosevic\PycharmProjects\pricesDashboard\-Graphs\paperwood.pdf', bbox_inches='tight', pad_inches=0.1, format="pdf")

plt.show()
