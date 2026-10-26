# main.py
import shutil
import os
from scraper import scrape_market
from storage import save_to_csv, save_to_json
from config import OUTPUT_CSV, OUTPUT_JSON, PUBLIC_JSON

def main():
    print("[-] Fetching technical job updates in Qatar...")
    jobs = scrape_market()
    
    save_to_csv(jobs, OUTPUT_CSV)
    save_to_json(jobs, OUTPUT_JSON)
    
    # Auto-sync to public directory for React
    os.makedirs("public", exist_ok=True)
    shutil.copy(OUTPUT_JSON, PUBLIC_JSON)
    print(f"[+] Synced data directly to {PUBLIC_JSON}!")

if __name__ == "__main__":
    main()