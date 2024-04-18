import pandas as pd

# Excel file URL
excel_url = "https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Historical-Data-Monthly.xlsx"

# Read Excel file into a DataFrame
df = pd.read_excel(excel_url, sheet_name="Monthly Prices")

# Display the column names
print(df.columns)

import pandas as pd

# Excel file URL
excel_url = "https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Historical-Data-Monthly.xlsx"

# Specify the columns and rows you want to read
columns_to_read = ["World Bank Commodity Price Data (The Pink Sheet)", "Unnamed: 30", "Unnamed: 32", "Unnamed: 37", "Unnamed: 24"] # Replace with your column names

# Read Excel file into a DataFrame, specifying only the desired columns
df = pd.read_excel(excel_url, sheet_name="Monthly Prices", usecols=columns_to_read)

# Display the DataFrame
print(df)

# Extract rows from the 771st row to the end
specific_rows = df.iloc[725:] # Indexing starts from 0, so 770 corresponds to the 771st row

specific_x_values = ['Jan 20', 'Feb 20', 'Mar 20', 'Apr 20', 'May 20', 'Jun 20', 'Jul 20', 'Aug 20', 'Sep 20', 'Oct 20', 'Nov 20', 'Dec 20', 'Jan 21', 'Feb 21', 'Mar 21', 'Apr 21', 'May 21', 'Jun 21', 'Jul 21', 'Aug 21', 'Sep 21', 'Oct 21', 'Nov 21', 'Dec 21', 'Jan 22', 'Feb 22', 'Mar 22', 'Apr 22', 'May 22', 'Jun 22', 'Jul 22', 'Aug 22', 'Sep 22', 'Oct 22', 'Nov 22', 'Dec 22', 'Jan 23', 'Feb 23', 'Mar 23', 'Apr 23', 'May 23', 'Jun 23', 'Jul 23', 'Aug 23', 'Sep 23', 'Oct 23', 'Nov 23', 'Dec 23', 'Jan 24', 'Feb 24', 'Mar 24']

# Display the specific rows
print(specific_rows)

# Convert the list 'fbx_value' to a pandas Series
maize_series = pd.Series(specific_rows['Unnamed: 30'])
rice_series = pd.Series(specific_rows['Unnamed: 32'])
wheat_series = pd.Series(specific_rows['Unnamed: 37'])
soybeans_series = pd.Series(specific_rows['Unnamed: 24'])

# Calculate percentage change from the last value
latest_value_maize = maize_series.iloc[-1]
previous_month_value_maize = maize_series.iloc[-2]
last_year_value_maize = maize_series.iloc[-13]
monthly_change_maize = ((latest_value_maize - previous_month_value_maize) / previous_month_value_maize) * 100
annual_change_maize= ((latest_value_maize - last_year_value_maize) / last_year_value_maize) * 100

latest_value_rice = rice_series.iloc[-1]
previous_month_value_rice = rice_series.iloc[-2]
last_year_value_rice = rice_series.iloc[-13]
monthly_change_rice = ((latest_value_rice - previous_month_value_rice) / previous_month_value_rice) * 100
annual_change_rice = ((latest_value_rice - last_year_value_rice) / last_year_value_rice) * 100

# Calculate percentage change from the last value
latest_value_wheat = wheat_series.iloc[-1]
previous_month_value_wheat = wheat_series.iloc[-2]
last_year_value_wheat = wheat_series.iloc[-13]
monthly_change_wheat = ((latest_value_wheat - previous_month_value_wheat) / previous_month_value_wheat) * 100
annual_change_wheat= ((latest_value_wheat - last_year_value_wheat) / last_year_value_wheat) * 100

latest_value_soybeans = soybeans_series.iloc[-1]
previous_month_value_soybeans = soybeans_series.iloc[-2]
last_year_value_soybeans = soybeans_series.iloc[-13]
monthly_change_soybeans = ((latest_value_soybeans - previous_month_value_soybeans) / previous_month_value_soybeans) * 100
annual_change_soybeans = ((latest_value_soybeans - last_year_value_soybeans) / last_year_value_soybeans) * 100

monthly_change_maize = round(monthly_change_maize,1)
annual_change_maize = round(annual_change_maize,1)

monthly_change_rice = round(monthly_change_rice,1)
annual_change_rice = round(annual_change_rice,1)

monthly_change_wheat = round(monthly_change_wheat,1)
annual_change_wheat = round(annual_change_wheat,1)

monthly_change_soybeans = round(monthly_change_soybeans,1)
annual_change_soybeans = round(annual_change_soybeans,1)

# Print or use the calculated changes as needed
print("Latest value for Wheat:", wheat_series.iloc[-1])
print("Monthly Change Wheat:", monthly_change_wheat)
print("Annual Change Wheat:", annual_change_wheat)
print("-")
print("Latest value for Maize:", maize_series.iloc[-1])
print("Monthly Change Maize:", monthly_change_maize)
print("Annual Change Maize:", annual_change_maize)
print("-")
print("Latest value for Rice:", rice_series.iloc[-1])
print("Monthly Change Rice:", monthly_change_rice)
print("Annual Change Rice:", annual_change_rice)
print("-")
print("Latest value for Soybeans:", soybeans_series.iloc[-1])
print("Monthly Change Soybeans:", monthly_change_soybeans)
print("Annual Change Soybeans:", annual_change_soybeans)

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Set Arial as the default font family
plt.rcParams['font.family'] = 'Arial'

# Visualize the data
fig, ax = plt.subplots(figsize=(20.59 / 2.54, 10.64 / 2.54)) # Adjust the size as needed
plt.plot(specific_x_values,specific_rows['Unnamed: 30'], label='Maize ($/mt)', color='#3E71B3')
plt.plot(specific_x_values,specific_rows['Unnamed: 32'], label='Rice ($/mt)', color='#5BAA7D')
plt.plot(specific_x_values,specific_rows['Unnamed: 37'], label='Wheat, US HRW ($/mt)', color='#BF7A45')
plt.plot(specific_x_values,specific_rows['Unnamed: 24'], label='Soybeans ($/mt)', color='#001F60')


plt.ylabel('Price, $', color='#797878', fontsize=8)
plt.title('Maize, rice, wheat and soybeans', color='#001E60', fontsize=12)
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
plt.ylim(bottom=100)

# Remove minor ticks
plt.tick_params(axis='both', which='both', length=0)

fig.set_size_inches(20.59 / 2.54, 10.64 / 2.54)

# Set the scale of the y-axis to go up by increments of 500
ax.yaxis.set_major_locator(MultipleLocator(100))

# Adjust y-axis limits to accommodate the data
ax.set_ylim(bottom=100, top=specific_rows[['Unnamed: 30', 'Unnamed: 32', 'Unnamed: 37', 'Unnamed: 24']].values.max() + 100)

# Save the figure without extra whitespace
plt.savefig(r'C:\Users\Uros.Milosevic\PycharmProjects\pythonProject\-Graphs\maizericewheatsoybeans.pdf', bbox_inches='tight', pad_inches=0.1, format="pdf")

plt.show()
