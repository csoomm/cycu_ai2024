#read csv"C:\Users\Cosmos\Desktop\中原\cycu.ai11022329\20240612\M05A03.csv"
import pandas as pd

df = pd.read_csv("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\M05A03.csv")

#只保留ds為01F0584N,01F0633N,01F0578S,01F0633S的資料
df = df[(df["ds"]=="01F0584N")|(df["ds"]=="01F0633N")|(df["ds"]=="01F0578S")|(df["ds"]=="01F0633S")]
print(df)
