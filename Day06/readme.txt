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

1. Ensure you have Python and pandas installed.
2. Place the Excel file in the specified path.
3. Run the provided Python script to see the results.

## Testing

A test script is provided to verify the computation. Run the test script to ensure the calculations are correct.

## Example

For the given data, the script will output the volume change for each mutant as a percentage.
