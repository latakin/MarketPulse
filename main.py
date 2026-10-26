from scraper import scrape_market
from storage import save_to_csv
from config import OUTPUT_FILE

def main():
    print("[-] Starting MarketPulse Scraper...")
    
    # Step 1: Execute the core scraping logic
    books_data = scrape_market()
    
    # Step 2: Check if data was retrieved and save it
    if books_data:
        print(f"[*] Processing {len(books_data)} records for storage...")
        save_to_csv(books_data, OUTPUT_FILE)
        print("[+] MarketPulse run completed successfully!")
    else:
        print("[!] No data collected. Please check network connection or scraper selectors.")

if __name__ == "__main__":
    main()