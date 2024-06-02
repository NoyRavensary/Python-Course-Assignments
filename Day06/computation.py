import pandas as pd

# Load the Excel file
file_path = r'C:\Noy Python Course\Day06\11.9_qacA_quant.xlsx'
sheet1_data = pd.read_excel(file_path, sheet_name='Sheet1')

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

volume_change = compute_volume_change(sheet1_data)

# Print the results
print("Volume Change (90/0) * 100 for each mutant:")
for mutant, change in volume_change.items():
    print(f"{mutant}: {change:.2f}%")
