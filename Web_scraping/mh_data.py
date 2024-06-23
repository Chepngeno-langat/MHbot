import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to get page content
def get_page_content(url):
    response = requests.get(url)
    return response.content

# Function to parse page content
def parse_page_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    title = soup.find('h1', class_='entry-title').text.strip()
    threads = soup.find_all('div', class_='inside-article')
    data = []

    for thread in threads:
        block_title = thread.find_all('h2', class_='wp-block-heading').text().strip()
        block_content = thread.find('p').text().strip()
