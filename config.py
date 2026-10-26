# Base configuration for MarketPulse Scraper

# Target sandbox URL (Books to Scrape is designed for web scraping practice)
BASE_URL = "http://books.toscrape.com/"

# Standard User-Agent header to mimic a standard web browser request
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# Output file path configuration
OUTPUT_FILE = "data/scraped_products.csv"