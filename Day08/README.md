# NCBI Data Downloader GUI

## Description
This application provides a graphical user interface for downloading data from the NCBI databases.
It allows users to specify a search term, the number of items to download, the database to search in, and the file format for the downloaded data.

## Requirements
- Python 3.x
- Biopython
- pandas
- Tkinter (usually comes with Python)

## Setup
1. Ensure you have Python installed on your system.
2. Install the required Python packages by running `pip install -r requirements.txt` in your terminal.

## Usage
To start the application, run `python ncbi_gui.py` from your terminal. Enter your search term, the number of items to download, select the database and file format, and click "Download Data".

## Notes
- The downloaded files will be saved in a `downloads` directory within the same folder as the script.
- A log of your searches will be saved in `search_log.csv`.
