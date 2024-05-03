# A simple example of web scraping using Python's 'requests' and 'BeautifulSoup' libraries to extract information from a webpage

import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
#url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
#url = 'https://fa.wikipedia.org/wiki/%D8%A7%D8%B3%D8%AA%D8%A7%D9%86%E2%80%8C%D9%87%D8%A7_%D9%88_%D9%82%D9%84%D9%85%D8%B1%D9%88%D9%87%D8%A7%DB%8C_%DA%A9%D8%A7%D9%86%D8%A7%D8%AF%D8%A7'
url = 'https://en.wikipedia.org/wiki/Web_scraping'
# Send a GET request to fetch the webpage content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find specific elements on the webpage using BeautifulSoup
    # Example: Extract the title of the webpage
    title = soup.title.string
    print('Title: ', title)

    # Example: Extract the first paragraph of the main content
    first_paragraph = soup.find('p').get_text()

    print('First Paragraph: ', first_paragraph)

    # Example: Extract all the links in the page
    links = soup.find_all('a')
    print('Number of links: ', len(links))

    # Example: Extract the text of a specific section by its ID
    section_id = 'History_and_evolution'
    section_tag = soup.find('span', {'id': section_id})
    if section_tag:
        section = section_tag.find_all_next('p').get_text()
        print('Section:', section)
    else:
        print('Section not found')

else:
    print('Failed to fetch webpage:', response.status_code)