import requests
from bs4 import BeautifulSoup
from config import BASE_URL, HEADERS

def fetch_page(url):
    """
    Sends an HTTP GET request to the target URL with headers.
    Returns the response object if successful, or None if failed.
    """
    try:
        print(f"[*] Fetching page: {url}")
        response = requests.get(url, headers=HEADERS)
        
        # Raise an exception for HTTP error codes (like 404 or 403)
        response.raise_for_status()
        return response.text
        
    except requests.exceptions.RequestException as e:
        print(f"[!] Network or HTTP error occurred: {e}")
        return None

def parse_books(html_content):
    """
    Parses raw HTML content using BeautifulSoup,
    extracts book titles and prices, and returns them as a list of dictionaries.
    """
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, "html.parser")
    books_data = []

    # Find all book article containers on the page
    book_items = soup.find_all("article", class_="product_pod")
    print(f"[*] Found {len(book_items)} items on the page. Parsing...")

    for item in book_items:
        try:
            # Extract title (stored in the 'title' attribute of the <a> tag inside <h3>)
            title = item.find("h3").find("a")["title"]
            
            # Extract raw price string (e.g., "£51.77")
            price_str = item.find("p", class_="price_color").text.strip()
            
            # Clean up the price: remove currency symbol ('£') and convert to float
            clean_price = float(price_str.replace("£", ""))
            
            # Store in a structured dictionary
            books_data.append({
                "Title": title,
                "Price_GBP": clean_price
            })
            
        except AttributeError as e:
            # Handle cases where an expected HTML element might be missing
            print(f"[!] Skipping an item due to missing fields: {e}")
            continue

    return books_data

def scrape_market():
    """
    Main orchestration function for scraper.py
    """
    html = fetch_page(BASE_URL)
    if html:
        return parse_books(html)
    return []