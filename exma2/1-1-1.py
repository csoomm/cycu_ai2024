import requests
import shutil
import tarfile

# 定義 URL 和儲存路徑
url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/M05A_20240101.tar.gz"
save_path = "M05A_20240101.tar.gz"

# 下載檔案
response = requests.get(url, stream=True)
with open(save_path, "wb") as file:
    shutil.copyfileobj(response.raw, file)

#儲存路徑，解壓縮，儲存到C:\Users\Cosmos\Desktop\0601\exma2中
tar = tarfile.open(save_path)
tar.extractall(r"C:\Users\Cosmos\Desktop\0601\exma2")
tar.close()

#讀取"C:\Users\Cosmos\Desktop\0601\exma2\M05A"中的所有資料夾00到23，將各個資料夾中的csv檔案合併成一個檔案
import os
import pandas as pd

base_dir = "C:\\Users\\Cosmos\\Desktop\\0601\\exma2\\M05A\\20240101"
output_file = "C:\\Users\\Cosmos\\Desktop\\0601\\exma2\\M05A_20240101.csv"

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
output_dir = "C:\\Users\\Cosmos\\Desktop\\0601\\exma2\\all_csv" 
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

#儲存路徑，以csv的形式儲存
output_file = "C:\\Users\\Cosmos\\Desktop\\0601\\exma2\\M05A_20240101.csv"
df.to_csv(output_file, index=False)

#刪除空資料夾
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
if os.path.exists("C:\\Users\\Cosmos\\Desktop\\0601\\exma2\\M05A"):
    shutil.rmtree("C:\\Users\\Cosmos\\Desktop\\0601\\exma2\\M05A")
print("Done")


    






