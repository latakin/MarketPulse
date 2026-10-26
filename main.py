from scraper import scrape_market
from storage import save_to_csv, save_to_json
from config import OUTPUT_FILE

def main():
    print("[-] Starting MarketPulse Scraper...")
    
    # Step 1: Execute scraping logic
    books_data = scrape_market()
    
    # Step 2: Save to both CSV and JSON formats
    if books_data:
        print(f"[*] Processing {len(books_data)} records for storage...")
        
        # Save CSV (for data analysis or spreadsheet use)
        save_to_csv(books_data, OUTPUT_FILE)
        
        # Save JSON (for your React frontend to read)
        json_output_path = OUTPUT_FILE.replace(".csv", ".json")
        save_to_json(books_data, json_output_path)
        
        print("[+] MarketPulse run completed successfully!")
    else:
        print("[!] No data collected.")

if __name__ == "__main__":
    main()