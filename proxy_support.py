import itertools
import requests

PROXY_SCRAPE_URL = 'https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport&format=text&protocol=socks5'

class ProxyManager:
    def __init__(self):
        '''Initialize the proxy manager.'''
        self.proxies = self.fetch_proxies()  # Fetch initial proxies

    def fetch_proxies(self):
        '''Fetch fresh SOCKS5 proxies from the ProxyScrape API.'''
        try:
            response = requests.get(PROXY_SCRAPE_URL)
            response.raise_for_status()
            proxies = response.text.strip().split('\n')
            return itertools.cycle(proxies) if proxies else None
        except Exception as e:
            print(f"Error fetching proxies: {e}")
            return None

    def get_proxy(self):
        '''Return the next proxy in the list.'''
        return next(self.proxies) if self.proxies else None

    def get_proxied_session(self):
        '''Return a requests session configured to use the next available SOCKS5 proxy.'''
        proxy = self.get_proxy()
        if not proxy:
            raise Exception("No proxies available")
        session = requests.Session()
        session.proxies = {
            'http': f'socks5h://{proxy}',
            'https': f'socks5h://{proxy}'
        }
        return session
