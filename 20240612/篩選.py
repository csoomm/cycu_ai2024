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


print(df)
