import pandas as pd

file = 'C:\data\lijst.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse(xl.sheet_names[0])

print(df1.get_values())
