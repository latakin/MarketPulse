import csv
import os

def save_to_csv(data_list, output_file):
    """
    Saves a list of dictionaries to a CSV file.
    Automatically creates the target directory if it does not exist.
    """
    if not data_list:
        print("[!] No data provided to save.")
        return

    # Extract directory path from output_file (e.g., "data/" from "data/scraped_products.csv")
    directory = os.path.dirname(output_file)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        print(f"[+] Created missing directory: {directory}")

    # Extract fieldnames dynamically from the keys of the first dictionary item
    fieldnames = data_list[0].keys()

    try:
        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # Write header row
            writer.writeheader()
            
            # Write data rows
            writer.writerows(data_list)
            
        print(f"[+] Successfully saved {len(data_list)} records to {output_file}")
    
    except Exception as e:
        print(f"[!] Error saving file: {e}")