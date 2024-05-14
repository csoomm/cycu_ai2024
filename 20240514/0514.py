import pandas as pd

# 讀取 csv 文件
df = pd.read_csv('/workspaces/cycu_ai2024/20240514/M03A.csv')

# 將第1,2,3個列分組，並將第五個列的值相加
df['車流量'] = df.groupby(['Time', 'Door', 'Direction'])['Number'].transform('sum')

#只保留Car colomn為31的資料
df = df[df['Car'] == 31]

#Door colomn只保留第四個到第七個字元
df['Door'] = df['Door'].str[4:7]

#Direction colomn只保留資料為S
df = df[df['Direction'] == 'S']

#將Door colomn轉換為int
df['Door'] = df['Door'].astype(int)

#將colomn Door做遞增的排序
df = df.sort_values(by='Door')

#將colomn 31.0,32.0,41.0,42.0,5.0的數值轉換為int並相加放入新的colomn命名為Number
df['Number'] = df['31'].astype(int) + df['32'].astype(int) + df['41'].astype(int) + df['42'].astype(int) + df['5'].astype(int)


# 儲存結果到新的 csv 文件
df.to_csv('/workspaces/cycu_ai2024/20240514/NewM03A.csv', index=False)

import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import numpy as np

# 讀取 csv 文件
df = pd.read_csv('/workspaces/cycu_ai2024/20240514/NewM03A.csv')

# 刪除重複的行
df = df.drop_duplicates(subset='Door')

# 對 'Door' 列進行排序
df = df.sort_values('Door')

# 創建 cubic spline 插值函數
cs = CubicSpline(df['Door'], df['車流量'])

# 創建 x 軸的值
xnew = np.linspace(df['Door'].min(), df['Door'].max(), 500)

# 繪製圖形
plt.plot(xnew, cs(xnew))
plt.scatter(df['Door'], df['車流量'], color='red')  # 原始數據點
plt.xlabel('Door')
plt.ylabel('車流量')
plt.title('Cubic Spline Interpolation')
plt.show()

# 儲存圖片到/workspaces/cycu_ai2024/20240514
plt.savefig('/workspaces/cycu_ai2024/20240514/0514.png')
