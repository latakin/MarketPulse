import re
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

    book_items = soup.find_all("article", class_="product_pod")
    print(f"[*] Found {len(book_items)} items on the page. Parsing...")

    for item in book_items:
        try:
            # Extract title
            title = item.find("h3").find("a")["title"]
            
            # Extract raw price string
            price_str = item.find("p", class_="price_color").text.strip()
            
            # Robust extraction using Regex: grabs only digits and dots (e.g., "51.77")
            match = re.search(r"[\d.]+", price_str)
            if match:
                clean_price = float(match.group())
            else:
                raise ValueError(f"Could not extract numeric price from: {price_str}")
            
            # Store in structured dictionary
            books_data.append({
                "Title": title,
                "Price_GBP": clean_price
            })
            
        except Exception as e:
            print(f"[!] Skipping an item due to parsing error: {e}")
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