import pandas as pd

# Excel file URL
csv_url = "https://assets.publishing.service.gov.uk/media/6603d15d13397a0011e41982/API_csv-21Mar2024i.csv"

# Read Excel file into a DataFrame
df = pd.read_csv(csv_url)

# Display the column names
print(df.columns)

print(df)

import pandas as pd

# Excel file URL
excel_url = "https://assets.publishing.service.gov.uk/media/6603d15d13397a0011e41982/API_csv-21Mar2024i.csv"

# Reverse the order of rows in the DataFrame
flipped_df = df[::-1]

# Reset the index to ensure the row indices are in sequential order
flipped_df = flipped_df.reset_index(drop=True)

#Print the flipped DataFrame
print(flipped_df)

start_index = 7758

# Slice the DataFrame from the specified starting row index to the end
sliced_df = flipped_df.loc[start_index:]

# Filter rows where the 'type' column has the value 'potato'
straightfertilisers_values = sliced_df[sliced_df['category'].str.strip().str.lower() == 'straight_fertilisers']
print(straightfertilisers_values)

specific_x_values = ['Jan 20', 'Feb 20', 'Mar 20', 'Apr 20', 'May 20', 'Jun 20', 'Jul 20', 'Aug 20', 'Sep 20', 'Oct 20', 'Nov 20', 'Dec 20', 'Jan 21', 'Feb 21', 'Mar 21', 'Apr 21', 'May 21', 'Jun 21', 'Jul 21', 'Aug 21', 'Sep 21', 'Oct 21', 'Nov 21', 'Dec 21', 'Jan 22', 'Feb 22', 'Mar 22', 'Apr 22', 'May 22', 'Jun 22', 'Jul 22', 'Aug 22', 'Sep 22', 'Oct 22', 'Nov 22', 'Dec 22', 'Jan 23', 'Feb 23', 'Mar 23', 'Apr 23', 'May 23', 'Jun 23', 'Jul 23', 'Aug 23', 'Sep 23', 'Oct 23', 'Nov 23', 'Dec 23', 'Jan 24']

specific_column = straightfertilisers_values['index']

print(specific_column)

# Convert the list 'fbx_value' to a pandas Series
straight_fertilisers_series = pd.Series(specific_column)

# Calculate percentage change from the last value
latest_value_straight_fertilisers = straight_fertilisers_series.iloc[-1]
previous_month_value_straight_fertilisers = straight_fertilisers_series.iloc[-2]
last_year_value_straight_fertilisers = straight_fertilisers_series.iloc[-13]
monthly_change_straight_fertilisers = ((latest_value_straight_fertilisers - previous_month_value_straight_fertilisers) / previous_month_value_straight_fertilisers) * 100
annual_change_straight_fertilisers = ((latest_value_straight_fertilisers - last_year_value_straight_fertilisers) / last_year_value_straight_fertilisers) * 100

monthly_change_straight_fertilisers = round(monthly_change_straight_fertilisers,1)
annual_change_straight_fertilisers = round(annual_change_straight_fertilisers,1)

# Print or use the calculated changes as needed
print("Latest value for Straight Fertilisers:", straight_fertilisers_series.iloc[-1])
print("Monthly Change Straight Fertilisers:", monthly_change_straight_fertilisers)
print("Annual Change Straight Fertilisers:", annual_change_straight_fertilisers)

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Set Arial as the default font family
plt.rcParams['font.family'] = 'Arial'

# Visualize the data
fig, ax = plt.subplots(figsize=(20.59 / 2.54, 10.64 / 2.54)) # Adjust the size as needed
plt.plot(specific_x_values,specific_column, label='Straight fertilisers (2020=100)', color='#3E71B3')

plt.ylabel('Index Value', color='#797878', fontsize=8)
plt.title('Straight fertilisers', color='#001E60', fontsize=12)
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
plt.ylim(bottom=50)

# Remove minor ticks
plt.tick_params(axis='both', which='both', length=0)

fig.set_size_inches(20.59 / 2.54, 10.64 / 2.54)

# Set the scale of the y-axis to go up by increments of 500
ax.yaxis.set_major_locator(MultipleLocator(50))

# Adjust y-axis limits to accommodate the data
ax.set_ylim(bottom=50, top=specific_column.values.max()+50)

# Save the figure without extra whitespace
plt.savefig(r'C:\Users\Uros.Milosevic\PycharmProjects\pythonProject\-Graphs\straightfertilisers.pdf', bbox_inches='tight', pad_inches=0.1, format="pdf")

plt.show()