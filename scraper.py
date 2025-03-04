#Saving data to a csv file then importing it into google sheets 

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape(url):
    # Fetch the web page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all book titles and links
    books = []
    for book in soup.find_all('h3'):
        title = book.a['title'].strip()  # Extract the title attribute
        link = book.a['href'].strip()    # Extract the href attribute
        books.append({'title': title, 'link': link})  # Append as a dictionary

    # Create a DataFrame
    df = pd.DataFrame(books)  # This should work if 'books' is a list of dictionaries

    # Save to CSV
    df.to_csv('books.csv', index=False)

# Example usage
scrape('https://books.toscrape.com/')
