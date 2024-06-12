import shutil
url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/"
for m in range(3,4,1):
    if m == 1 or m == 3:
        N=32
    elif m== 2:
        N=30
    elif m== 4:
        N=30
    for d in range(1,N,1):
        print(url+"M05A_2024"+str(m).zfill(2)+str(d).zfill(2)+".tar.gz")
        import requests
        import shutil
        import tarfile
        #定義URL和儲存路徑
        url1 = url+"M05A_2024"+str(m).zfill(2)+str(d).zfill(2)+".tar.gz"
        save_path = "M05A_2024"+str(m).zfill(2)+str(d).zfill(2)+".tar.gz"
        #下載檔案
        response = requests.get(url1, stream=True)
        with open(save_path, "wb") as file:
            shutil.copyfileobj(response.raw, file)
        #儲存路徑，解壓縮，儲存到C:\Users\Cosmos\Desktop\0601\exma2中
        tar = tarfile.open(save_path)
        tar.extractall(r"C:\Users\Cosmos\Desktop\中原\cycu.ai11022329\20240612")
        tar.close()
        #讀取"C:\Users\Cosmos\Desktop\0601\exma2\M05A"中的所有資料夾00到23，將各個資料夾中的csv檔案合併成一個檔案
        import os
        import pandas as pd

        base_dir = "C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\M05A\\2024"+str(m).zfill(2)+str(d).zfill(2)
        output_file = "C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\M05A_2024"+str(m).zfill(2)+str(d).zfill(2)+".csv"

        #讀取資料夾中的所有資料夾
        #將所有csv檔移轉到名為all_csv的資料夾中
        all_csv = []
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if file.endswith(".csv"):
                    all_csv.append(os.path.join(root, file))
        #加入column names
        column_names = ["time", "ds", "df", "type", "speed", "number"]
        for csv in all_csv:
            df = pd.read_csv(csv)
            #複製原本的colomn name命名為colomn_first
            column_first = df.columns
            #將資料往下移動一列
            df = df.shift(periods=1, axis=0)
            #將colomn_first放入第二列
            df.iloc[0] = column_first
            df.columns = column_names
            df.to_csv(csv, index=False)
        #儲存路徑
        output_dir = "C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\all_csv" 
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        #將所有csv檔移轉到名為all_csv的資料夾中
        for csv in all_csv:
            shutil.move(csv, output_dir)
        #合併所有csv檔，依照time排序
        all_csv = []
        for root, dirs, files in os.walk(output_dir):
            for file in files:
                if file.endswith(".csv"):
                    all_csv.append(os.path.join(root, file))
        df = pd.concat([pd.read_csv(csv) for csv in all_csv], ignore_index=True)
        df = df.sort_values(by=["time"])

        #將all_csv存入output_file
        df.to_csv(output_file, index=False)
        
        #刪除資料夾output_dir
        shutil.rmtree(output_dir)
        os.remove(save_path)
        shutil.rmtree(base_dir)
#製作一個csv檔案，命名為M05A202403.csv
output_file = "C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\M05A202403.csv"


all_csv = []
for root, dirs, files in os.walk("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612"):
    for file in files:
        if file.startswith("M05A_2024") and file.endswith(".csv"):
            all_csv.append(os.path.join(root, file))
df = pd.concat([pd.read_csv(csv) for csv in all_csv], ignore_index=True)
df.to_csv("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\M05A202403.csv", index=False)

for root, dirs, files in os.walk("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612"):
    for file in files:
        if file.startswith("M05A_2024") and file.endswith(".csv"):
            os.remove(os.path.join(root, file))
#=======================================================================================================================

#爬雨量
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

#讀取資料夾中為rain_20240301.csv到rain_20240331.csv的檔案，並取出StationId為A2C560的資料放入rain03.csv
for file in os.listdir(base_dir):
    if file.startswith("rain_2024") and file.endswith(".csv"):
        df = pd.read_csv(os.path.join(base_dir, file))
        df = df[(df["StationId"]=="A2C560")|(df["StationId"]=="A0C410")|(df["StationId"]=="C0C700")]
        df.to_csv(output_file, mode='a', index=False, header=False)

    
#======================================================================================================================

#整理雨量
df = pd.read_csv("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\rain03.csv")

#只保留StationId,DateTime,NOW的資料
df = df[["StationId", "DateTime", "NOW"]]

#刪除Now為-998的資料
df = df[df["NOW"] != -998]
#刪除Now為空值的資料
df = df.dropna(subset=["NOW"])



#依照時間順序，若相同DateTime前十個字元相同，則將NOW最大值留下，其餘刪除
df["DateTime"] = df["DateTime"].str[:10]
df = df.groupby(["DateTime"]).agg({"NOW": "max"}).reset_index()\

#若NOW>0，則將NOW改為1，其餘為0
df["NOW"] = df["NOW"].apply(lambda x: 1 if x > 0 else 0)

#儲存檔案
df.to_csv("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\rain03.csv", index=False)

#=======================================================================================================================

#整理車流
#read csv"C:\Users\Cosmos\Desktop\中原\cycu.ai11022329\20240612\M05A03.csv"
import pandas as pd

df = pd.read_csv("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\M05A202403.csv")

#只保留(ds為01F0584N df為01F0557N)(ds為01F0633N df為01F0584N)(ds為01F0578S df為01F0633S)(ds為01F0633S df為01F0664S)的資料
df = df[(df["ds"]=="01F0584N") & (df["df"]=="01F0557N") | (df["ds"]=="01F0633N") & (df["df"]=="01F0584N") | (df["ds"]=="01F0578S") & (df["df"]=="01F0633S") | (df["ds"]=="01F0633S") & (df["df"]=="01F0664S")]


#只保留type為31.0的資料
df = df[df["type"]==31.0]

#刪掉speed欄位
df = df.drop(columns=["speed"])

#新增一個欄位叫date，將time轉換成星期幾放入欄位date，星期一到星期五為1，星期六日為0
df["date"] = pd.to_datetime(df["time"]).dt.dayofweek
df["date"] = df["date"].apply(lambda x: 1 if x < 5 else 0)

#儲存檔案
df.to_csv("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\M05A202403.csv", index=False)

#=======================================================================================================================

#合併車流和雨量

import pandas as pd
car = pd.read_csv("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\M05A202403.csv")
rain = pd.read_csv("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\rain03.csv")

#取rain中DateTime欄位，轉換成YYYY/MM/DD HH:MM:SS格式
rain["DateTime"] = pd.to_datetime(rain["DateTime"]).dt.strftime("%Y/%m/%d %H:%M:%S")

#在car中新增一個欄位叫NOW
car["NOW"] = ""

#對照car的time欄位前十個字和rain中DateTime欄位前十個字，若相同則將rain中的NOleft join到car中
for i in range(len(car)):
    for j in range(len(rain)):
        if car["time"][i][:10] == rain["DateTime"][j][:10]:
            car["NOW"][i] = rain["NOW"][j]
#製作一個新csv檔，名為03.csv


#儲存檔案
car.to_csv("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\03.csv", index=False)

#=======================================================================================================================

#製圖

