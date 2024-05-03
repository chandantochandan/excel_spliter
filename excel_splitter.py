import pandas as pd
import numpy as np

def split_excel_file(input_file, output_prefix, row_limit):
    """
    Splits an Excel file into multiple files based on the row limit.

    Args:
    - input_file (str): Path to the input Excel file.
    - output_prefix (str): Prefix for the output file names.
    - row_limit (int): Maximum number of rows per output file.
    """
    # Read the Excel file into a DataFrame
    df = pd.read_excel(input_file)

    # Calculate the number of output files needed
    num_files = (len(df) - 1) // row_limit + 1

    # Split the DataFrame into chunks and write each chunk to a separate file
    for i, chunk in enumerate(np.array_split(df, num_files), start=1):
        output_file = f"{output_prefix}_{i}.xlsx"
        chunk.to_excel(output_file, index=False)
        print(f"Created file: {output_file}")

