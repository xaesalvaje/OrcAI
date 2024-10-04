import requests

def fetch_latest_dorks(proxy_manager):
    url = "https://www.exploit-db.com/google-hacking-database"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    session = proxy_manager.get_proxied_session()  # Use the proxy manager to get a session

    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()
        return response.text  # Return the page content
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"OOps: Something went wrong {err}")

    return None
