import sys
import os
import numpy as np
import pandas as pd

# Get the directory path of excel_splitter.py
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)

# Append the parent directory to the system path
sys.path.append(parent_dir)

import unittest
from excel_splitter import split_excel_file

class TestExcelSplitter(unittest.TestCase):
    def test_split_excel_file(self):
        # Test splitting a small Excel file into multiple files with row limit
        input_file = os.path.join(current_dir, "Payment Template Consolidate Dated 11-04-2024 Lot 1-EMANDATE.xlsx")  # Update file extension to .xlsx
        output_prefix = "Payment Template Consolidate Dated 11-04-2024 Lot 1-EMANDATE"
        row_limit = 60000
        df = pd.read_excel(input_file)  # read excel file
        split_excel_file(input_file, output_prefix, row_limit)
        # Add assertions to verify that the files are split correctly

if __name__ == "__main__":
    unittest.main()

