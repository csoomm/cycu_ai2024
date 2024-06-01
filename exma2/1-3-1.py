#擷取"C:\Users\Cosmos\Desktop\0601\exma2"中所有名字為2024xxxx.csv的檔案，將其合併成一個檔案，並依照time排序，儲存路徑為C:\Users\Cosmos\Desktop\0601\exma2\20240101_20240430.csv

import pandas as pd
import glob

# Get a list of all CSV files in the directory
csv_files = glob.glob("C:\\Users\\Cosmos\\Desktop\\0601\\exma2\\2024*.csv")

# Read each CSV file and store them in a list
dfs = [pd.read_csv(f) for f in csv_files]

# Concatenate all dataframes in the list
df = pd.concat(dfs, ignore_index=True)

# Sort the dataframe by 'time'
df = df.sort_values('time')

# Save the sorted dataframe to a new CSV file
df.to_csv("C:\\Users\\Cosmos\\Desktop\\0601\\exma2\\20240101_20240430.csv", index=False)
