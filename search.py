# search.py - Module for performing automated search using yagooglesearch

from yagooglesearch import search

def run_search(query, proxy_manager):
    print(f"Running search for query: {query}")
    session = proxy_manager.get_proxied_session()
    
    try:
        search_results = search(query, num_results=10, session=session)  # Retrieve top 10 results with proxy session
        return search_results
    except Exception as e:
        print(f"Error running search for {query}: {e}")
        return []
