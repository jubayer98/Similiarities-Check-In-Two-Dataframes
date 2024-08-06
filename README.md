# Similarities-Check-In-Two-Dataframes

This GitHub repository provides various methods for checking similarities between columns of two Pandas DataFrames, using Python. It includes techniques for exact matches, comparing unordered sets of values, statistical comparisons, and tolerance-based comparisons, as well as performing a left merge to identify matching entries similar to a VLOOKUP function in spreadsheets.

## Features

- **Exact Match**: Check if each element in one column exactly matches the corresponding element in another column.
- **Similar Values (Ignoring Order)**: Verify if both columns contain the same set of values regardless of the order.
- **Statistical Comparison**: Compare the statistical properties (mean, median, standard deviation, etc.) of two columns.
- **Tolerance Based Comparison**: Determine if the values in two columns are approximately equal within a specified tolerance level.
- **VLOOKUP-like Operation**: Use a left merge to join two DataFrames based on a key column and flag rows that have matching entries.

## Getting Started

To use these methods, clone this repository and import the necessary functions into your Python environment. Ensure you have Pandas installed, as it is required to manipulate the DataFrames.

```bash
git clone https://github.com/jubayer98/Similiarities-Check-In-Two-Dataframes.git
cd Similiarities-Check-In-Two-Dataframes
```

## Usage

You can use these functions by importing them into your Python script or notebook. Here are general steps to follow for each method provided in this repository:

1. **Prepare your DataFrames** with the columns you intend to compare.
2. **Choose the comparison method** that suits your definition of "similar".
3. **Apply the method** to check for similarities between the columns.

## Example

Here's a brief example on how to set up your environment and use the exact match method:

```python
import pandas as pd

# Create example DataFrames
df1 = pd.DataFrame({'columnx': [1, 2, 3, 4]})
df2 = pd.DataFrame({'columny': [1, 2, 3, 4]})

# Check if columns are identical
similar = df1['columnx'].equals(df2['columny'])
print(similar)  # Outputs True if all elements match exactly, otherwise False
```

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change. Ensure to update tests as appropriate.
