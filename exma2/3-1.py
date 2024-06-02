import os
import requests
import shutil
import tarfile
import pandas as pd

df = pd.read_csv("C:\\Users\\Cosmos\\Desktop\\0601\\exma2\\M05A_20240429_feature.csv")
look = pd.read_csv("C:\\Users\\Cosmos\\Desktop\\0601\\exma2\\look.csv")

import folium

#建立地圖，中心點為台灣的經緯度
m = folium.Map(location=[23.58, 121], zoom_start=7)

#look,csv中有台灣各個高速公路的經緯度，door為門架的編號，lat為緯度，lon為經度，將這些資料加入地圖中
for i in range(len(look)):
    folium.CircleMarker([look["lat"][i], look["lon"][i]], radius=5, color='red', fill=True, fill_color='red').add_to(m)


#time從12384到12671
#利用time的資料，用geojson的方式畫出台灣的高速公路
#將同一列ds df的資料，用線的方式連接起來
#線的顏色依照speed決定，0為紫色,1為紅色,2為黃色,3為橘色,4為綠色

import pandas as pd
import folium


# 選取特定的資料
df = df[(df['time'] >= 12384) & (df['time'] <= 12671)]

# 創建一個新的欄位，該欄位包含從ds到df的線段的geojson表示
df['geojson'] = df.apply(lambda row: {
    "type": "Feature",
    "geometry": {
        "type": "LineString",
        "coordinates": [[look.loc[look['door'] == row['ds'], 'lon'].values[0], look.loc[look['door'] == row['ds'], 'lat'].values[0]], [look.loc[look['door'] == row['df'], 'lon'].values[0], look.loc[look['door'] == row['df'], 'lat'].values[0]]]
    },
    "properties": {
        "time": row['time'],
        "color": {0: 'purple', 1: 'red', 2: 'yellow', 3: 'orange', 4: 'green'}[row['speed']]
    }
}, axis=1)

# 創建一個新的地圖
m = folium.Map(location=[look['lat'].mean(), look['lon'].mean()], zoom_start=13)

# 將所有的線段添加到地圖上
for _, row in df.iterrows():
    folium.GeoJson(row['geojson'], style_function=lambda feature: {
        'color': feature['properties']['color']
    }).add_to(m)

# 顯示地圖
m.save("C:\\Users\\Cosmos\\Desktop\\0601\\exma2\\map.html")