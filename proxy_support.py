# proxy_support.py - Adds SOCKS5 proxy support for round-robin usage during searches

import itertools
import requests

class ProxyManager:
    def __init__(self, proxies):
        '''Initialize the proxy manager with a list of proxies.'''
        self.proxies = itertools.cycle(proxies)  # Cycle through proxies indefinitely

    def get_proxy(self):
        '''Return the next proxy in the list.'''
        return next(self.proxies)

    def get_proxied_session(self):
        '''Return a requests session configured to use the next available proxy.'''
        proxy = self.get_proxy()
        session = requests.Session()
        session.proxies = {
            'http': proxy,
            'https': proxy
        }
        return session
