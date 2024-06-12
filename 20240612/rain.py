import requests
from bs4 import BeautifulSoup
#'StationId','StationName','CountyName','TownName','StationLatitude','StationLongitude','StationAltitude','DateTime','Past1hr','Past10Min','Past3hr','Past6hr','Past12hr','Past24hr','NOW','Past2days','Past3days'
#建立一個空的csv檔，命名為rain03.csv，放入C:\Users\Cosmos\Desktop\中原\cycu.ai11022329\20240612
import csv
with open("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\rain03.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['StationId','StationName','CountyName','TownName','StationLatitude','StationLongitude','StationAltitude','DateTime','Past1hr','Past10Min','Past3hr','Past6hr','Past12hr','Past24hr','NOW','Past2days','Past3days'])



first_chars = ['A']
second_chars = ['x', 'y', 'z', '0', '1', '2', '3', '4', '5']
n=1

for first_char in first_chars:
     for second_char in second_chars:
        url = f"https://history.colife.org.tw/?r=/download&path=L%2Bawo%2BixoS%2FkuK3lpK7msKPosaHnvbJf6Zuo6YeP56uZLzIwMjQwMy9yYWluXzIwMjQwMz({first_char}{second_char})LnppcA%3D%3D"
        response = requests.get(url)
        # process the response here
        #下載url中的zip檔
        import requests
        import shutil
        import zipfile
        #定義URL和儲存路徑
        url1 = url
        save_path = "20240612"+str(n).zfill(2)+first_char+second_char+".zip"
        #下載檔案
        response = requests.get(url1, stream=True)
        with open(save_path, "wb") as file:
            shutil.copyfileobj(response.raw, file)
        #儲存路徑，解壓縮，儲存到C:\Users\Cosmos\Desktop\中原\cycu.ai11022329\20240612中
        with zipfile.ZipFile(save_path, 'r') as zip_ref:
            zip_ref.extractall("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\M05A")
        #刪除zip檔
        import os
        os.remove(save_path)
            
first_chars = ['E', 'I']
second_chars = ['w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5']

for first_char in first_chars:
    for second_char in second_chars:
        url = f"https://history.colife.org.tw/?r=/download&path=L%2Bawo%2BixoS%2FkuK3lpK7msKPosaHnvbJf6Zuo6YeP56uZLzIwMjQwMy9yYWluXzIwMjQwMz({first_char}{second_char})LnppcA%3D%3D"
        response = requests.get(url)
        # process the response here
        import requests
        import shutil
        import zipfile
        #定義URL和儲存路徑
        url1 = url
        save_path = "20240612"+str(n).zfill(2)+first_char+second_char+".zip"
        #下載檔案
        response = requests.get(url1, stream=True)
        with open(save_path, "wb") as file:
            shutil.copyfileobj(response.raw, file)
        #儲存路徑，解壓縮，儲存到C:\Users\Cosmos\Desktop\中原\cycu.ai11022329\20240612中
        with zipfile.ZipFile(save_path, 'r') as zip_ref:
            zip_ref.extractall("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\M05A")
        #刪除zip檔
        import os
        os.remove(save_path)



first_chars = ['M']
second_chars = ['w', 'x']

for first_char in first_chars:
    for second_char in second_chars:
        url = f"https://history.colife.org.tw/?r=/download&path=L%2Bawo%2BixoS%2FkuK3lpK7msKPosaHnvbJf6Zuo6YeP56uZLzIwMjQwMy9yYWluXzIwMjQwMz({first_char}{second_char})LnppcA%3D%3D"
        response = requests.get(url)
        # process the response here
        import requests
        import shutil
        import zipfile
        #定義URL和儲存路徑
        url1 = url
        save_path = "20240612"+str(n).zfill(2)+first_char+second_char+".zip"
        #下載檔案
        response = requests.get(url1, stream=True)
        with open(save_path, "wb") as file:
            shutil.copyfileobj(response.raw, file)
        #儲存路徑，解壓縮，儲存到C:\Users\Cosmos\Desktop\中原\cycu.ai11022329\20240612中
        with zipfile.ZipFile(save_path, 'r') as zip_ref:
            zip_ref.extractall("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\M05A")
        #刪除zip檔
        import os
        os.remove(save_path)

#將名為rain_2024****.csv的檔案依照colomn name放入rain03.csv
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
將all_csv中的檔案依照colomn name放入rain03.csv
column_names = ['StationId','StationName','CountyName','TownName','StationLatitude','StationLongitude','StationAltitude','DateTime','Past1hr','Past10Min','Past3hr','Past6hr','Past12hr','Past24hr','NOW','Past2days','Past3days']
for csv in all_csv:
    df = pd.read_csv(csv)
    df.columns = column_names
    df.to_csv(output_file, mode='a', header=False, index=False)
    

