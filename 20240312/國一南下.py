import pandas as pd

# 讀取 CSV 文件
df = pd.read_csv('C:\\Users\\User\\Desktop\\123.csv', encoding='utf-8')

# 過濾出方向欄位為'南向'和'南'的資料
south_data = df[(df['方向'] == '北向')| (df['方向'] == '北')]
highway_date = south_data[south_data['國道名稱'] == '國道3號']


# 統計每個里程數的數量
mileage_count = highway_date['里程'].value_counts()

# 欄位年，月，日，時，分都換成數字
highway_date['年'] = pd.to_datetime(highway_date['事件發生']).dt.year
highway_date['月'] = pd.to_datetime(highway_date['事件發生']).dt.month
highway_date['日'] = pd.to_datetime(highway_date['事件發生']).dt.day
highway_date['時'] = pd.to_datetime(highway_date['事件發生']).dt.hour
highway_date['分'] = pd.to_datetime(highway_date['事件發生']).dt.minute

#將年月日時分合併成一個欄位
highway_date['時間'] = highway_date['年'].astype(str) + '-' + highway_date['月'].astype(str) + '-' + highway_date['日'].astype(str) + ' ' + highway_date['時'].astype(str) + ':' + highway_date['分'].astype(str)

#將時間欄位轉換成日期格式
highway_date['時間'] = pd.to_datetime(highway_date['時間'])

#將時間欄位轉成從julian day 0開始的天數
highway_date['時間'] = (highway_date['時間'] - pd.to_datetime('1970-01-01')).dt.total_seconds()

#輸出highway_date的所有資料
print(highway_date)


# 製作圖表，y軸為里程，x軸為時間
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 設定中文字體
plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.scatter(highway_date['時間'], highway_date['里程'], label='里程', color='gray', s=0.5)  # 將點的大小設定為2
plt.title('國3北上 土木三丙11022329周冠嘉')
plt.xlabel('時間')
plt.ylabel('里程')
plt.xticks(rotation=70)
plt.legend()
plt.tight_layout()
plt.show()







