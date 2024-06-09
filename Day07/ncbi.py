import sys
import os
from Bio import Entrez
import pandas as pd
from datetime import datetime

def validate_arguments():
    # Ensure the user has provided the correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python ncbi.py TERM NUMBER")
        sys.exit(1)

def get_search_parameters():
    # Extract the search term and number of items to download from the command line arguments
    search_term = sys.argv[1]
    number_of_items = int(sys.argv[2])
    return search_term, number_of_items

def perform_search(search_term, number_of_items):
    # Perform the search
    search_handle = Entrez.esearch(db="nucleotide", term=search_term, retmax=number_of_items)
    search_results = Entrez.read(search_handle)
    search_handle.close()
    return search_results

def fetch_and_save_items(ids, search_term):
    # Create a directory to save the files if it doesn't exist
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    # Download and save each item
    file_names = []
    for i, id in enumerate(ids, start=1):
        fetch_handle = Entrez.efetch(db="nucleotide", id=id, rettype="fasta", retmode="text")
        data = fetch_handle.read()
        fetch_handle.close()
        
        file_name = f"downloads/{search_term}_{i}.fasta"
        with open(file_name, "w") as file:
            file.write(data)
        file_names.append(file_name)
    return file_names

def log_search_details(search_term, number_of_items, total_items_found):
    # Log the search details in a CSV file
    log_file = "search_log.csv"
    log_exists = os.path.exists(log_file)
    with open(log_file, "a") as csvfile:
        headers = ["date", "term", "max", "total"]
        writer = pd.DataFrame([[datetime.now(), search_term, number_of_items, total_items_found]], columns=headers)
        if not log_exists:
            writer.to_csv(csvfile, index=False)
        else:
            writer.to_csv(csvfile, mode='a', header=False, index=False)

def main():
    validate_arguments()
    search_term, number_of_items = get_search_parameters()
    
    Entrez.email = "noy.ravensary@weizmann.ac.il"
    
    search_results = perform_search(search_term, number_of_items)
    ids = search_results["IdList"]
    total_items_found = search_results["Count"]
    
    file_names = fetch_and_save_items(ids, search_term)
    
    # Print the names of the files saved
    for file_name in file_names:
        print(file_name)
    
    log_search_details(search_term, number_of_items, total_items_found)

if __name__ == "__main__":
    main()