# Excel Data Computation

This project performs a computation on an Excel file containing data about different mutants and their volumes measured at different time points.

## Data Description

The Excel file contains the following columns:
- `mutant`: The type of mutant.
- `time`: The time point at which the volume was measured.
- `Lane #`: The lane number (not used in the computation).
- `Band #`: The band number (not used in the computation).
- `Volume`: The volume measurement.

## Computation

The script performs the following computation for each mutant:
1. Calculates the ratio of the volume at time 90 to the volume at time 0.
2. Multiplies this ratio by 100 to get the percentage change.

## How to Run

To run the computation script, follow these steps:

1. Ensure you have Python and pandas installed. You can install pandas using the command `pip install pandas`.
2. Use the command line to navigate to the directory containing the script.
3. Run the script by providing the path to your Excel file as an argument. For example:
   ```
   python computation.py path_to_your_excel_file.xlsx
   ```
   Replace `path_to_your_excel_file.xlsx` with the actual path to your Excel file.

## Testing

A test script is provided to verify the computation. To run the tests, follow these steps:

1. Ensure you have `pytest` installed. If not, you can install it using the command `pip install pytest`.
2. Use the command line to navigate to the directory containing the test script.
3. Run the test script using pytest. For example:
   ```
   pytest computation_test.py
   ```
   This command will execute the test script and verify that the computation is performed correctly.
    
## Example

For the given data, the script will output the volume change for each mutant as a percentage.