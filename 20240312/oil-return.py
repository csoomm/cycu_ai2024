import requests
from bs4 import BeautifulSoup
import pandas as pd

# 抓取網頁內容
url = "https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx"
response = requests.get(url)

# 解析網頁內容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到所有的表格
tables = soup.find_all('table')

# 將每個表格轉換為 DataFrame
dfs = [pd.read_html(str(table))[0] for table in tables]

# dfs 是一個包含兩個 DataFrame 的列表
df1 = dfs[0]  # 第一個 DataFrame
df2 = dfs[1]  # 第二個 DataFrame

#只保留前五欄位的資料
import matplotlib.pyplot as plt

df2 = df2.iloc[:, :5]

#去除NaN的資料
df2 = df2.dropna()
print(df2)

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 設定字型為繁體中文
plt.plot(df2['調價日期'][::-7], df2['無鉛汽油92'][::-7], label='92無鉛', color='red')
plt.plot(df2['調價日期'][::-7], df2['無鉛汽油95'][::-7], label='95無鉛', color='blue')
plt.plot(df2['調價日期'][::-7], df2['無鉛汽油98'][::-7], label='98無鉛', color='green')
plt.plot(df2['調價日期'][::-7], df2['超級/高級柴油'][::-7], label='超級柴油', color='black')
plt.title('油價走勢')
plt.xlabel('日期')
plt.ylabel('油價')
plt.xticks(rotation=70)
plt.legend()
plt.show()

#https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil2019.aspx
# 抓取網頁內容
response = requests.get("https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil2019.aspx")

# 解析網頁內容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到所有的表格
tables = soup.find_all('table')

# 將每個表格轉換為 DataFrame
dfs = [pd.read_html(str(table))[0] for table in tables]

# dfs 是一個包含兩個 DataFrame 的列表
df3 = dfs[0]  # 第一個 DataFrame
df4 = dfs[1]  # 第二個 DataFrame

#只保留前五欄位的資料
df4 = df4.iloc[:, :5]

#去除NaN的資料
df4 = df4.dropna()
print(df4)

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 設定字型為繁體中文

df = pd.concat([df2, df4])
print(df)

plt.plot(df['調價日期'][::-7], df['無鉛汽油92'][::-7], label='92無鉛', color='red')
plt.plot(df['調價日期'][::-7], df['無鉛汽油95'][::-7], label='95無鉛', color='blue')
plt.plot(df['調價日期'][::-7], df['無鉛汽油98'][::-7], label='98無鉛', color='green')
plt.plot(df['調價日期'][::-7], df['超級/高級柴油'][::-7], label='超級柴油', color='black')
plt.title('油價走勢')
plt.xlabel('日期')
plt.ylabel('油價')
plt.xticks(rotation=70)
plt.legend()
plt.show()

#將資料存成csv檔存入C:\Users\User\Desktop\0305\cycu_ai2024\20240305
df.to_csv('C:/Users/User/Desktop/0312/cycu_ai2024/20240312/oilFINAL.csv', index=False, encoding='utf-8-sig')