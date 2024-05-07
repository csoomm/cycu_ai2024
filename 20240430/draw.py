import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 讀取 csv 檔案
df = pd.read_csv('/workspaces/cycu_ai2024/20240430/time特徵化.csv')

# 創建一個新的欄位 'color'，根據 'speed' 欄位的值來設定顏色
def color(speed):
    if speed > 80:
        return 'green'
    elif 60 < speed <= 80:
        return 'yellow'
    elif 40 < speed <= 60:
        return 'orange'
    elif 20 < speed <= 40:
        return 'red'
    else:
        return 'purple'

df['color'] = df['Speed'].apply(color)

# 創建三維圖
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Time'], df['Door'].apply(lambda x: int(x[:4])), df['31.0'], c=df['color'], s=1)
ax.set_xlabel('Time')
ax.set_ylabel('Door')
ax.set_zlabel('31')

#製作可以旋轉的圖，將圖存成.spt檔
plt.show()
plt.savefig('/workspaces/cycu_ai2024/20240430/3dplot.png')
#儲存圖片

