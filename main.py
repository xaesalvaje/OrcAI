# orcai.py - Main script for OrcAI Automated Penetration Testing Tool

import time
from search import run_search
from scraper import scrape_data
from utils import validate_data
from dork_library import fetch_dorks, save_dorks_to_file
from proxy_support import ProxyManager

def main():
    print("OrcAI - Automated Data Extraction Tool Starting...")
    
    # Fetch the latest dorks
    dorks = fetch_dorks()
    save_dorks_to_file(dorks)
    
    # Proxy list example (could be passed as arguments)
    proxies = ['socks5://127.0.0.1:9050', 'socks5://127.0.0.1:9051']
    proxy_manager = ProxyManager(proxies)

    # Run searches using dorks
    for dork in dorks:
        print(f"Running search for dork: {dork}")
        search_results = run_search(dork, proxy_manager)
        
        for url in search_results:
            print(f"Scraping data from: {url}")
            scraped_data = scrape_data(url, proxy_manager)
            
            if validate_data(scraped_data):
                print(f"Valid data found and extracted: {scraped_data}")
            else:
                print(f"No valid data found on {url}")
            
            # Wait for some time before the next search
            time.sleep(5)

if __name__ == "__main__":
    main()
