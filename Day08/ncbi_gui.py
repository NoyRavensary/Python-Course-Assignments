import tkinter as tk
from tkinter import ttk, scrolledtext

# Import the modified ncbi module
from ncbi import ncbi_search_and_download

# Function to handle the download button click
def download_data():
    search_term = search_term_entry.get()
    number_of_items = number_entry.get()
    db = db_selector.get()
    file_format = format_selector.get()
    
    if search_term and number_of_items.isdigit():
        file_names = ncbi_search_and_download(search_term, int(number_of_items), db, file_format)
        status_text.config(state=tk.NORMAL)
        status_text.insert(tk.END, f"Downloaded {len(file_names)} files for '{search_term}' in {file_format} format.\n")
        status_text.config(state=tk.DISABLED)
    else:
        status_text.config(state=tk.NORMAL)
        status_text.insert(tk.END, "Invalid input. Please enter a valid search term and number of items.\n")
        status_text.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("NCBI Data Downloader")
root.geometry("500x300")

# Styling
style = ttk.Style()
style.theme_use('clam')

# Custom font
custom_font = ('Helvetica', 11)

# Main frame
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

# Search term
search_term_frame = ttk.Frame(main_frame, padding="3")
search_term_frame.pack(fill=tk.X)
search_term_label = ttk.Label(search_term_frame, text="Search Term:", font=custom_font)
search_term_label.pack(side=tk.LEFT)
search_term_entry = ttk.Entry(search_term_frame, font=custom_font)
search_term_entry.pack(fill=tk.X, expand=True)

# Number of items
number_frame = ttk.Frame(main_frame, padding="3")
number_frame.pack(fill=tk.X)
number_label = ttk.Label(number_frame, text="Number of Items:", font=custom_font)
number_label.pack(side=tk.LEFT)
number_entry = ttk.Entry(number_frame, font=custom_font)
number_entry.pack(fill=tk.X, expand=True)

# Database selector
db_frame = ttk.Frame(main_frame, padding="3")
db_frame.pack(fill=tk.X)
db_label = ttk.Label(db_frame, text="Select Database:", font=custom_font)
db_label.pack(side=tk.LEFT)
db_selector = ttk.Combobox(db_frame, values=["nucleotide", "protein", "genome"], state="readonly", font=custom_font)
db_selector.pack(fill=tk.X, expand=True)

# File format selector
format_frame = ttk.Frame(main_frame, padding="3")
format_frame.pack(fill=tk.X)
format_label = ttk.Label(format_frame, text="Select File Format:", font=custom_font)
format_label.pack(side=tk.LEFT)
format_selector = ttk.Combobox(format_frame, values=["fasta", "genbank", "xml"], state="readonly", font=custom_font)
format_selector.pack(fill=tk.X, expand=True)

# Download button
download_button = ttk.Button(main_frame, text="Download Data", command=download_data)
download_button.pack(pady="10")

# Status messages with scrollbar
status_frame = ttk.Frame(main_frame, padding="3")
status_frame.pack(fill=tk.BOTH, expand=True)
status_text = scrolledtext.ScrolledText(status_frame, state='disabled', height=5, font=custom_font)
status_text.pack(fill=tk.BOTH, expand=True)

# Run the application
root.mainloop()