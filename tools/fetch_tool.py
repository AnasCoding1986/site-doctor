import httpx

def fetch_page(url: str) -> str:
    """
    Fetch raw HTML from a given URL.
    
    Args:
        url: Website URL to fetch (e.g., 'https://example.com')
    
    Returns:
        Raw HTML string of the page
    """
    try:
        response = httpx.get(url, timeout=10.0, follow_redirects=True)
        response.raise_for_status()
        return response.text
    except httpx.TimeoutException:
        return f"Error: Request timeout for {url}"
    except httpx.HTTPError as e:
        return f"Error: Failed to fetch {url}. {str(e)}"
    except Exception as e:
        return f"Error: Unexpected error fetching {url}. {str(e)}"