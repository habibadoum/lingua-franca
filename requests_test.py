import requests
from bs4 import BeautifulSoup

# Define the URL
url = 'https://www.webonary.org/sango/browse/browse-vernacular-english/?key=sg&letter=b&lang=en'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully retrieved the webpage.")
    
    # Get the content of the webpage
    html_content = response.content
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Example: Extract and print data based on HTML structure
    # Assuming the data of interest is in a specific table or div with a class or id
    data_container = soup.find('div', class_='entry-content')  # Adjust the class or tag as needed
    
    if data_container:
        entries = data_container.find_all('li')  # Adjust the tag as needed
        
        for entry in entries:
            word = entry.find('span', class_='lexeme')  # Adjust the class or tag as needed
            definition = entry.find('span', class_='definition')  # Adjust the class or tag as needed
            
            if word and definition:
                print(f"Word: {word.text.strip()}, Definition: {definition.text.strip()}")
    else:
        print("No data container found. Please check the HTML structure.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
