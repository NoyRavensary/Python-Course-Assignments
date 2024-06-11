from Bio import Entrez
import pandas as pd
from datetime import datetime
import os

# Function to perform the search and download
def ncbi_search_and_download(search_term, number_of_items, db="nucleotide", rettype="fasta"):
    Entrez.email = "your_email@example.com"  # Replace with your email
    search_results = Entrez.esearch(db=db, term=search_term, retmax=number_of_items)
    search_results = Entrez.read(search_results)
    ids = search_results["IdList"]
    total_items_found = search_results["Count"]
    
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    
    file_names = []
    for i, id in enumerate(ids, start=1):
        fetch_handle = Entrez.efetch(db=db, id=id, rettype=rettype, retmode="text")
        data = fetch_handle.read()
        fetch_handle.close()
        
        file_name = f"downloads/{search_term}_{i}.{rettype.lower()}"
        with open(file_name, "w") as file:
            file.write(data)
        file_names.append(file_name)
    
    log_search_details(search_term, number_of_items, total_items_found, db, rettype)
    return file_names

# Function to log search details
def log_search_details(search_term, number_of_items, total_items_found, db, rettype):
    log_file = "search_log.csv"
    log_exists = os.path.exists(log_file)
    with open(log_file, "a") as csvfile:
        headers = ["date", "term", "max", "total", "database", "file_format"]
        writer = pd.DataFrame([[datetime.now(), search_term, number_of_items, total_items_found, db, rettype]], columns=headers)
        if not log_exists:
            writer.to_csv(csvfile, index=False)
        else:
            writer.to_csv(csvfile, mode='a', header=False, index=False)