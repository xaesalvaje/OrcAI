# search.py - Module for performing automated search using yagooglesearch

import yagooglesearch

def run_search(query, proxy_manager):
    print(f"Running search for query: {query}")
    session = proxy_manager.get_proxied_session()
    
    try:
        # Initialize SearchClient with proxy
        client = yagooglesearch.SearchClient(
            query,
            proxy="socks5h://{proxy_manager.get_proxy()}",  # Add proxy
            max_search_result_urls_to_return=100,  # Max number of search results
            verbosity=5,  # Verbose mode for debugging
            verbose_output=True  # Include rank, title, description, and URL in output
        )
        
        client.assign_random_user_agent()  # Randomize user-agent for realism
        search_results = client.search()  # Perform the search
        
        return search_results
    except Exception as e:
        print(f"Error running search for {query}: {e}")
        return []
