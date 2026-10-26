import csv
import json
import os

def save_to_csv(data_list, output_file):
    """
    Saves a list of dictionaries to a CSV file.
    Automatically creates the target directory if it does not exist.
    """
    if not data_list:
        print("[!] No data provided to save.")
        return

    directory = os.path.dirname(output_file)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    fieldnames = data_list[0].keys()

    try:
        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_list)
        print(f"[+] Successfully saved CSV: {output_file}")
    except Exception as e:
        print(f"[!] Error saving CSV: {e}")

def save_to_json(data_list, output_json_path):
    """
    Saves a list of dictionaries to a JSON file for frontend consumption.
    """
    if not data_list:
        return

    directory = os.path.dirname(output_json_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    try:
        with open(output_json_path, mode="w", encoding="utf-8") as file:
            json.dump(data_list, file, indent=4, ensure_ascii=False)
        print(f"[+] Successfully saved JSON: {output_json_path}")
    except Exception as e:
        print(f"[!] Error saving JSON: {e}")