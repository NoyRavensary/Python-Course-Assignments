import sys
import pandas as pd

# Perform the computation
def compute_volume_change(data):
    results = {}
    for mutant in data['mutant'].unique():
        subset = data[data['mutant'] == mutant]
        volume_0 = subset[subset['time'] == 0]['Volume'].values
        volume_90 = subset[subset['time'] == 90]['Volume'].values
        if len(volume_0) == 1 and len(volume_90) == 1:
            change = (volume_90[0] / volume_0[0]) * 100
            results[mutant] = change
    return results

if __name__ == "__main__":
    # Check if a file path is provided
    if len(sys.argv) != 2:
        print("Usage: python computation.py <path_to_excel_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Load the Excel file
    sheet1_data = pd.read_excel(file_path, sheet_name='Sheet1')
    # Calculate computation
    volume_change = compute_volume_change(sheet1_data)
    # Print the results
    print("Volume Change (90/0) * 100 for each mutant:")
    for mutant, change in volume_change.items():
        print(f"{mutant}: {change:.2f}%")
