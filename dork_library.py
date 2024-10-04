# dork_library.py - Module for maintaining a library of search dorks

import requests
from bs4 import BeautifulSoup

DORKS_URL = 'https://www.exploit-db.com/google-hacking-database'

def fetch_dorks():
    '''Fetches the latest Google dorks from an external source.'''
    try:
        print("Fetching latest dorks...")
        response = requests.get(DORKS_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract dorks from the webpage
        dorks = []
        dork_elements = soup.find_all("tr", class_="dork-entry")
        for elem in dork_elements:
            dork = elem.find("td", class_="description").get_text(strip=True)
            dorks.append(dork)
        
        return dorks
    except Exception as e:
        print(f"Error fetching dorks: {e}")
        return []

def save_dorks_to_file(dorks, file_path="dorks.txt"):
    '''Saves dorks to a file for reuse.'''
    with open(file_path, "w") as f:
        for dork in dorks:
            f.write(dork + "\n")
    print(f"Saved {len(dorks)} dorks to {file_path}.")
