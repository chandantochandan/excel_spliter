import sys
import os
import numpy as np
import pandas as pd

# Get the directory path of excel_splitter.py
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)

# Append the parent directory to the system path
sys.path.append(parent_dir)

input_file = os.path.join(current_dir, "Payment Template Consolidate Dated 11-04-2024 Lot 1-EMANDATE.xlsx")
if not os.path.exists(input_file):
    raise FileNotFoundError(f"File '{input_file}' not found.")
