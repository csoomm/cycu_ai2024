import pandas as pd
import seaborn as sns

df = pd.read_csv("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\03.csv")

#新增一個欄位direction
df["direction"] = ""

#新增一個欄位d，將ds的最後一個字元填入d
df["d"] = df["ds"].str[-1]

#若ds為01F0584N df為01F0557N，NOW=1，在direction填入"中壢內壢北上下雨"
df.loc[(df["ds"]=="01F0584N") & (df["df"]=="01F0557N") & (df["NOW"]==1), "direction"] = "中壢內壢北上下雨"
#若ds為01F0633N df為01F0584N，在direction填入"平鎮中壢北上"
df.loc[(df["ds"]=="01F0633N") & (df["df"]=="01F0584N") & (df["NOW"]==1), "direction"] = "平鎮中壢北上下雨"
#若ds為01F0578S df為01F0633S 在direction填入"內壢中壢南下"
df.loc[(df["ds"]=="01F0578S") & (df["df"]=="01F0633S") & (df["NOW"]==1), "direction"] = "內壢中壢南下下雨"
#若ds為01F0633S df為01F0664S 在direction填入"中壢平鎮南下"
df.loc[(df["ds"]=="01F0633S") & (df["df"]=="01F0664S") & (df["NOW"]==1), "direction"] = "中壢平鎮南下下雨"
#若ds為01F0584N df為01F0557N，NOW=1，在direction填入"中壢內壢北上沒雨"
df.loc[(df["ds"]=="01F0584N") & (df["df"]=="01F0557N") & (df["NOW"]==0), "direction"] = "中壢內壢北上沒雨"
#若ds為01F0633N df為01F0584N，在direction填入"平鎮中壢北上"
df.loc[(df["ds"]=="01F0633N") & (df["df"]=="01F0584N") & (df["NOW"]==0), "direction"] = "平鎮中壢北上沒雨"
#若ds為01F0578S df為01F0633S 在direction填入"內壢中壢南下"
df.loc[(df["ds"]=="01F0578S") & (df["df"]=="01F0633S") & (df["NOW"]==0), "direction"] = "內壢中壢南下沒雨"
#若ds為01F0633S df為01F0664S 在direction填入"中壢平鎮南下"
df.loc[(df["ds"]=="01F0633S") & (df["df"]=="01F0664S") & (df["NOW"]==0), "direction"] = "中壢平鎮南下沒雨"

df["dr"] = ""

#若ds最後一個字元為N，date為1，在dr填入"北上平日"
df.loc[(df["ds"].str[-1]=="N") & (df["date"]==1), "dr"] = "北上平日"
#若ds最後一個字元為N，date為0，在dr填入"北上假日"
df.loc[(df["ds"].str[-1]=="N") & (df["date"]==0), "dr"] = "北上假日"
#若ds最後一個字元為S，date為1，在dr填入"南下平日"
df.loc[(df["ds"].str[-1]=="S") & (df["date"]==1), "dr"] = "南下平日"
#若ds最後一個字元為S，date為0，在dr填入"南下假日"
df.loc[(df["ds"].str[-1]=="S") & (df["date"]==0), "dr"] = "南下假日"

#讀取time欄為倒數五個字，將time和direction相同的資料的number欄位相加
df["number"] = df["number"].astype(int)
df["time"] = df["time"].str[-5:]
df = df.groupby(["time", "direction", "dr", "d"])["number"].sum().reset_index()

#製作圖表，折線圖，x軸為time，y軸為number，匯入d為N的資料，利用direction分分成四條線


import matplotlib.pyplot as plt
sns.set()
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 設定字型為繁體中文
plt.figure(figsize=(20, 10))
sns.lineplot(x="time", y="number", hue="direction", data=df[df["dr"]=="北上平日"])
plt.xlabel("時間")
plt.ylabel("數量")
plt.title("三月平日北上")
plt.legend(title="方向")
plt.savefig("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\03平日北上.png")

sns.set()
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.figure(figsize=(20, 10))
sns.lineplot(x="time", y="number", hue="direction", data=df[df["dr"]=="南下平日"])
plt.xlabel("時間")
plt.ylabel("數量")
plt.title("三月平日南下")
plt.legend(title="方向")
plt.savefig("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\03平日南下.png")

sns.set()
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.figure(figsize=(20, 10))
sns.lineplot(x="time", y="number", hue="direction", data=df[df["dr"]=="北上假日"])
plt.xlabel("時間")
plt.ylabel("數量")
plt.title("三月假日北上")
plt.legend(title="方向")
plt.savefig("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\03假日北上.png")

sns.set()
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.figure(figsize=(20, 10))
sns.lineplot(x="time", y="number", hue="direction", data=df[df["dr"]=="南下假日"])
plt.xlabel("時間")
plt.ylabel("數量")
plt.title("三月假日南下")
plt.legend(title="方向")
plt.savefig("C:\\Users\\Cosmos\\Desktop\\中原\\cycu.ai11022329\\20240612\\03假日南下.png")
