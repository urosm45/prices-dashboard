import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = "https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/l52h/mm23"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the HTML content of the webpage
    html_content = response.text

    # Print or process the HTML content as needed
    print(html_content)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all table data elements with text alignment set to right
table_data_right = soup.find_all("td", class_="table__data text-right")

# Extract and print the text content of the found elements
for element in table_data_right:
    print(element.get_text())