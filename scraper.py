import requests
from bs4 import BeautifulSoup
from utils import validate_data
import os

def save_validated_content(url, content, folder_path="validated_documents"):
    '''Save the validated content from a URL into a text file for future reference.'''
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename = os.path.join(folder_path, f"{url.replace('https://', '').replace('http://', '').replace('/', '_')}.txt")
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"URL: {url}\n\n")
        file.write(content)
    
    print(f"Saved validated content to {filename}.")

def scrape_data(url, proxy_manager):
    '''Fetch and scrape data from a given URL using proxy support, and save if validated.'''
    print(f"Fetching URL: {url}")
    session = proxy_manager.get_proxied_session()
    
    try:
        response = session.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        page_text = soup.get_text()
        
        if validate_data(page_text):
            print(f"Valid data found at: {url}")
            save_validated_content(url, page_text)
        else:
            print(f"No valid data found on {url}")
        
        return page_text
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""
