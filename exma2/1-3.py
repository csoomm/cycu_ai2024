import pandas as pd
H=0
for i in range(1,5,1):
    if i == 1 or i == 3:
        H=32
    elif i == 2:
        H=30
    elif i == 4:
        H=31
    for j in range(1,H,1):
        # Load the CSV file
        df = pd.read_csv("C:\\Users\\Cosmos\\Desktop\\0601\\exma2\\M05A_2024"+str(i).zfill(2)+str(j).zfill(2)+".csv")

        #篩選出time ds df 皆相同的橫列合併，新增欄位num31,num32,num41,num42,num5，將相同time ds df的number依照type分類，分別放入num31,num32,num41,num42,num5
        df["num31"] = df["number"][(df["type"] == 31.0)]
        df["num32"] = df["number"][(df["type"] == 32.0)]
        df["num41"] = df["number"][(df["type"] == 41.0)]
        df["num42"] = df["number"][(df["type"] == 42.0)]
        df["num5"] = df["number"][(df["type"] == 5.0)]

        #排序 time ds df
        df = df.sort_values(by=["time", "ds", "df"])


        #將相同time ds df的橫列取出，如果type不同，則將num31,num32,num41,num42,num5填入type為31.0的橫列
        df["num31"] = df["num31"].fillna(method="ffill")
        df["num32"] = df["num32"].fillna(method="ffill")
        df["num41"] = df["num41"].fillna(method="ffill")
        df["num42"] = df["num42"].fillna(method="ffill")
        df["num5"] = df["num5"].fillna(method="ffill")

        #保留type為31.0的橫列
        df = df[df["type"] == 31.0]

        #刪除colomn type
        df = df.drop(columns=["type"])
        #刪除colomn number
        df = df.drop(columns=["number"])

        #放入csv檔，儲存路徑為C:\Users\Cosmos\Desktop\0601\exma2\M05A_2024xx.csv
        df.to_csv("C:\\Users\\Cosmos\\Desktop\\0601\\exma2\\2024"+str(i).zfill(2)+str(j).zfill(2)+".csv", index=False)


