import os
import pandas as pd

base_dir = "C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\M05A"
output_file = "C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\rain03.csv"

#讀取資料夾中為rain_20240301.csv到rain_20240331.csv的檔案
#將所有csv檔移轉到名為all_csv的資料夾中
all_csv = []
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.startswith("rain_2024") and file.endswith(".csv"):
            all_csv.append(os.path.join(root, file))
#將all_csv中的檔案依照colomn name放入rain03.csv
column_names = ['StationId','StationName','CountyName','TownName','StationLatitude','StationLongitude','StationAltitude','DateTime','Past1hr','Past10Min','Past3hr','Past6hr','Past12hr','Past24hr','NOW','Past2days','Past3days']
for csv in all_csv:
    df = pd.read_csv(csv)
    df.columns = column_names
    df.to_csv(output_file, mode='a', header=False, index=False)