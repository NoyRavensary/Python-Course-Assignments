# NCBI Data Downloader
This command-line tool searches for and downloads data from the NCBI nucleotide database based on a given search term. It saves each item in its own file and logs the search details in a CSV file.

# Usage
To use the tool, run the following command in your terminal:

python ncbi.py TERM NUMBER
Replace TERM with the search term you're interested in, and NUMBER with the maximum number of items you want to download.

# Example
bash
python ncbi.py Orchid 3
python ncbi.py cauliflower 7
This will search for "Orchid" and "cauliflower" in the NCBI nucleotide database, download up to 3 and 7 items respectively, and save each item in its own file within a downloads directory. It will also update the search_log.csv file with the details of each search.

