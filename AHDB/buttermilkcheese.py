import pandas as pd

# Excel file URL
excel_url = "https://projectblue.blob.core.windows.net/media/Default/Market%20Intelligence/dairy/Images/Prices/Wholesale%20prices/UK%20wholesale%20prices-8.xlsx"

# Read Excel file into a DataFrame
df = pd.read_excel(excel_url, sheet_name="UK wholesale prices")

# Display the column names
print(df.columns)

import pandas as pd

# Excel file URL
excel_url = "https://projectblue.blob.core.windows.net/media/Default/Market%20Intelligence/dairy/Images/Prices/Wholesale%20prices/UK%20wholesale%20prices-8.xlsx"

# Specify the columns and rows you want to read
columns_to_read = ["Unnamed: 1", "Unnamed: 4", "Unnamed: 6", "Unnamed: 8"] # Replace with your column names

# Read Excel file into a DataFrame, specifying only the desired columns
df = pd.read_excel(excel_url, sheet_name="UK wholesale prices", usecols=columns_to_read)

# Display the DataFrame
print(df)

# Extract rows from the 771st row to the end
specific_rows = df.iloc[241:292] # THIS WILL NEED ADJUSTING EVERY TIME

specific_x_values = ['Jan 20', 'Feb 20', 'Mar 20', 'Apr 20', 'May 20', 'Jun 20', 'Jul 20', 'Aug 20', 'Sep 20', 'Oct 20', 'Nov 20', 'Dec 20', 'Jan 21', 'Feb 21', 'Mar 21', 'Apr 21', 'May 21', 'Jun 21', 'Jul 21', 'Aug 21', 'Sep 21', 'Oct 21', 'Nov 21', 'Dec 21', 'Jan 22', 'Feb 22', 'Mar 22', 'Apr 22', 'May 22', 'Jun 22', 'Jul 22', 'Aug 22', 'Sep 22', 'Oct 22', 'Nov 22', 'Dec 22', 'Jan 23', 'Feb 23', 'Mar 23', 'Apr 23', 'May 23', 'Jun 23', 'Jul 23', 'Aug 23', 'Sep 23', 'Oct 23', 'Nov 23', 'Dec 23', 'Jan 24', 'Feb 24', 'Mar 24']

# Display the specific rows
print(specific_rows)

# Convert the list 'fbx_value' to a pandas Series
butter_series = pd.Series(specific_rows['Unnamed: 4'])
milk_series = pd.Series(specific_rows['Unnamed: 6'])
cheese_series = pd.Series(specific_rows['Unnamed: 8'])

# Calculate percentage change from the last value
latest_value_butter = butter_series.iloc[-1]
previous_month_value_butter = butter_series.iloc[-2]
last_year_value_butter = butter_series.iloc[-13]
monthly_change_butter = ((latest_value_butter - previous_month_value_butter) / previous_month_value_butter) * 100
annual_change_butter= ((latest_value_butter - last_year_value_butter) / last_year_value_butter) * 100

latest_value_milk = milk_series.iloc[-1]
previous_month_value_milk = milk_series.iloc[-2]
last_year_value_milk = milk_series.iloc[-13]
monthly_change_milk = ((latest_value_milk - previous_month_value_milk) / previous_month_value_milk) * 100
annual_change_milk = ((latest_value_milk - last_year_value_milk) / last_year_value_milk) * 100

# Calculate percentage change from the last value
latest_value_cheese = cheese_series.iloc[-1]
previous_month_value_cheese = cheese_series.iloc[-2]
last_year_value_cheese = cheese_series.iloc[-13]
monthly_change_cheese = ((latest_value_cheese - previous_month_value_cheese) / previous_month_value_cheese) * 100
annual_change_cheese= ((latest_value_cheese - last_year_value_cheese) / last_year_value_cheese) * 100

monthly_change_butter = round(monthly_change_butter,1)
annual_change_butter = round(annual_change_butter,1)

monthly_change_milk = round(monthly_change_milk,1)
annual_change_milk = round(annual_change_milk,1)

monthly_change_cheese = round(monthly_change_cheese,1)
annual_change_cheese =  round(annual_change_cheese,1)


# Print or use the calculated changes as needed
print("Latest value for Cheese:", cheese_series.iloc[-1])
print("Monthly Change Cheese:", monthly_change_cheese)
print("Annual Change Cheese:", annual_change_cheese)
print("-")
print("Latest value for Butter:", butter_series.iloc[-1])
print("Monthly Change Butter:", monthly_change_butter)
print("Annual Change Butter:", annual_change_butter)
print("-")
print("Latest value for Milk:", milk_series.iloc[-1])
print("Monthly Change Milk:", monthly_change_milk)
print("Annual Change Milk:", annual_change_milk)

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Set Arial as the default font family
plt.rcParams['font.family'] = 'Arial'

# Visualize the data
fig, ax = plt.subplots(figsize=(20.59 / 2.54, 10.64 / 2.54)) # Adjust the size as needed
plt.plot(specific_x_values,specific_rows['Unnamed: 4'], label='Butter (unsalted) (£/tonne)', color='#3E71B3')
plt.plot(specific_x_values,specific_rows['Unnamed: 6'], label='Skimmed milk powder (£/tonne)', color='#5BAA7D')
plt.plot(specific_x_values,specific_rows['Unnamed: 8'], label='Mild cheddar (£/tonne)', color='#BF7A45')


plt.ylabel('Price, £', color='#797878', fontsize=8)
plt.title('Butter, mild cheddar and skimmed milk powder', color='#001E60', fontsize=12)
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

# Adjust y-axis limits to accommodate the data
ax.set_ylim(bottom=1000, top=specific_rows[['Unnamed: 4', 'Unnamed: 6', 'Unnamed: 8']].values.max() + 1000)

# Save the figure without extra whitespace
plt.savefig(r'C:\Users\Uros.Milosevic\PycharmProjects\pricesDashboard\-Graphs\buttermilkcheese.pdf', bbox_inches='tight', pad_inches=0.1, format="pdf")

plt.show()
