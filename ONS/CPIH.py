import webbrowser
import pandas as pd

# URL of the webpage
url = 'https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/l52h/mm23'
url1 = 'https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/l52r/mm23'

# Open the webpage
webbrowser.open(url)
webbrowser.open(url1)

# Manually input data as a list of lists (each inner list represents a column)
specific_x_values = ['Jan 20', 'Feb 20', 'Mar 20', 'Apr 20', 'May 20', 'Jun 20', 'Jul 20', 'Aug 20', 'Sep 20', 'Oct 20', 'Nov 20', 'Dec 20', 'Jan 21', 'Feb 21', 'Mar 21', 'Apr 21', 'May 21', 'Jun 21', 'Jul 21', 'Aug 21', 'Sep 21', 'Oct 21', 'Nov 21', 'Dec 21', 'Jan 22', 'Feb 22', 'Mar 22', 'Apr 22', 'May 22', 'Jun 22', 'Jul 22', 'Aug 22', 'Sep 22', 'Oct 22', 'Nov 22', 'Dec 22', 'Jan 23', 'Feb 23', 'Mar 23', 'Apr 23', 'May 23', 'Jun 23', 'Jul 23', 'Aug 23', 'Sep 23', 'Oct 23', 'Nov 23', 'Dec 23', 'Jan 24', 'Feb 24', 'Mar 24']
uk_food = [103.8, 103.9, 104.1, 104.0, 104.5, 103.9, 103.6, 103.8, 103.0, 103.0, 103.0, 102.4, 103.0, 103.5, 102.6, 103.5, 103.2, 103.5, 103.1, 104.1, 103.9, 104.4, 105.5, 107.0, 107.6, 108.6, 108.7, 110.5, 112.1, 113.8, 116.4, 118.2, 119.4, 121.9, 123.2, 125.2, 125.9, 128.6, 130.1, 132.0, 133.2, 133.6, 133.8, 134.1, 134.2, 134.2, 134.6, 135.3, 134.8, 135.1, 135.2]
uk_non_alcoholic_beverages = [107.2, 107.8, 108.2, 107.0, 108.3, 107.8, 107.5, 107.1,  107.5, 107.3, 105.0, 106.7, 107.6, 105.9, 107.0, 107.0, 106.5, 105.7, 105.8, 107.9, 107.4, 108.0, 108.3, 108.6, 111.1, 112.9, 114.1, 114.2, 116.9, 115.4, 117.6, 118.6, 120.8, 122.6, 124.2, 126.5, 127.5, 130.3, 130.3, 132.5, 133.2, 134.4, 134.0, 136.0, 133.7, 134.7, 135.3, 136.4, 135.6, 136.1, 137.1]
# Convert the list 'fbx_value' to a pandas Series
uk_food_series = pd.Series(uk_food)
uk_non_alcoholic_beverages_series = pd.Series(uk_non_alcoholic_beverages)

# Calculate percentage change from the last value
latest_value_food = uk_food_series.iloc[-1]
previous_month_value_food = uk_food_series.iloc[-2]
last_year_value_food = uk_food_series.iloc[-13]
monthly_change_food = ((latest_value_food - previous_month_value_food) / previous_month_value_food) * 100
annual_change_food = ((latest_value_food - last_year_value_food) / last_year_value_food) * 100

latest_value_drinks = uk_non_alcoholic_beverages_series.iloc[-1]
previous_month_value_drinks = uk_non_alcoholic_beverages_series.iloc[-2]
last_year_value_drinks = uk_non_alcoholic_beverages_series.iloc[-13]
monthly_change_drinks = ((latest_value_drinks - previous_month_value_drinks) / previous_month_value_drinks) * 100
annual_change_drinks = ((latest_value_drinks - last_year_value_drinks) / last_year_value_drinks) * 100

monthly_change_food = round(monthly_change_food,1)
annual_change_food =  round(annual_change_food,1)

monthly_change_drinks = round(monthly_change_drinks,1)
annual_change_drinks = round(annual_change_drinks,1)

# Print or use the calculated changes as needed
print("Latest value of Food Index:", uk_food_series.iloc[-1])
print("Monthly Change in Food Index:", monthly_change_food)
print("Annual Change in Food Index:", annual_change_food)
print("-")
print("Latest value of Drinks Index:", uk_non_alcoholic_beverages_series.iloc[-1])
print("Monthly Change in Drinks Index:", monthly_change_drinks)
print("Annual Change in Drinks Index:", annual_change_drinks)

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Set Arial as the default font family
plt.rcParams['font.family'] = 'Arial'

# Visualize the data
fig, ax = plt.subplots(figsize=(20.59 / 2.54, 10.64 / 2.54)) # Adjust the size as needed
plt.plot(specific_x_values,uk_food, label='UK food (2015 = 100)', color='#3E71B3')
plt.plot(specific_x_values,uk_non_alcoholic_beverages, label='UK non-alcoholic beverages (2015 = 100)', color='#5BAA7D')


plt.ylabel('Index', color='#797878', fontsize=8)
plt.title('UK food and UK non-alcoholic beverages', color='#001E60', fontsize=12)
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
max_value = max(max(uk_food), max(uk_non_alcoholic_beverages))
plt.ylim(bottom=100, top=max_value + 10)

# Save the figure without extra whitespace
plt.savefig(r'C:\Users\Uros.Milosevic\PycharmProjects\pricesDashboard\-Graphs\cpih.pdf', bbox_inches='tight', pad_inches=0.1, format="pdf")

plt.show()
