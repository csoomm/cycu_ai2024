import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 讀取 csv 檔案
df = pd.read_csv('/workspaces/cycu_ai2024/20240430/time特徵化.csv')

#colomn Door只保留第四個到第七個字元
df['Door'] = df['Door'].str[1:4]

#colomn Door轉換為int
df['Door'] = df['Door'].astype(int)

#colomn Time做遞增的排序
df = df.sort_values(by='Time')

df['Time'] = df['Time'].astype(int)

#只保留Direction colomn 為S的資料
df = df[df['Direction'] == 'S']

#將colomn 31.0,32.0,41.0,42.0,5.0 的資料轉換成int並相加
df['Number'] = df['31.0'].astype(int) + df['32.0'].astype(int) + df['41.0'].astype(int) + df['42.0'].astype(int) + df['5.0'].astype(int)

#將car colomn的值轉換成int
df['Car'] = df['Car'].astype(int)


#儲存結果到新的 csv 文件，命名為514.csv
df.to_csv('/workspaces/cycu_ai2024/20240430/514.csv', index=False)


#製作圖形，X為Time，Y為Car，Z為Door，利用CubicSpline進行擬合
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import numpy as np

# 讀取 csv 文件
df = pd.read_csv('/workspaces/cycu_ai2024/20240430/514.csv')

#設定x軸為Time，y軸為Door，製成網格
x = np.linspace(df['Time'].min(), df['Time'].max(), num=200)  # 調整 num 以匹配數據點的密度
y = np.linspace(df['Door'].min(), df['Door'].max(), num=200)
x, y = np.meshgrid(x, y)

#將Z設定為Car，進行CubicSpline擬合
from scipy.interpolate import griddata
z = griddata((df['Time'], df['Door']), df['Number'], (x, y), method='cubic')

#畫出3D圖形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, z, cmap='viridis')

#設定坐標軸標籤
ax.set_xlabel('Time')
ax.set_ylabel('Door')
ax.set_zlabel('Car')

#設定顏色條
fig.colorbar(surf)

#製作四個子圖，每個子圖都有不同的視角
fig = plt.figure()

# First subplot
ax1 = fig.add_subplot(221, projection='3d')
surf1 = ax1.plot_surface(x, y, z, cmap='viridis')
ax1.set_xlabel('Time')
ax1.set_ylabel('Door')
ax1.set_zlabel('Car')
ax1.view_init(30, 30)

# Second subplot
ax2 = fig.add_subplot(222, projection='3d')
surf2 = ax2.plot_surface(x, y, z, cmap='viridis')
ax2.set_xlabel('Time')
ax2.set_ylabel('Door')
ax2.set_zlabel('Car')
ax2.view_init(30, 120)

# Third subplot
ax3 = fig.add_subplot(223, projection='3d')
surf3 = ax3.plot_surface(x, y, z, cmap='viridis')
ax3.set_xlabel('Time')
ax3.set_ylabel('Door')
ax3.set_zlabel('Car')
ax3.view_init(30, 210)

# Fourth subplot
ax4 = fig.add_subplot(224, projection='3d')
surf4 = ax4.plot_surface(x, y, z, cmap='viridis')
ax4.set_xlabel('Time')
ax4.set_ylabel('Door')
ax4.set_zlabel('Car')
ax4.view_init(30, 300)

plt.suptitle("11022329")

plt.show()
plt.savefig('/workspaces/cycu_ai2024/20240430/515.png')





