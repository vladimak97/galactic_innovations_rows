# Import the pandas library.
import pandas as pd

# Path to the Excel file.
file_path = '/kaggle/input/galactic-innovations-rows/galactic_innovations_rows.xlsx'

# Read the Excel file.
df = pd.read_excel(file_path, engine='openpyxl')

# Print the contents.
print(df)