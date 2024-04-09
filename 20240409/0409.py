#20240409/地震活動彙整_638482837663712970.csv將資料中的地震時間，經度，緯度，規模，深度，位置輸出 並用big5輸出
import csv
import folium

csv_file = '/workspaces/cycu_ai2024/20240409/地震活動彙整_638482837663712970.csv'
output_file = '/workspaces/cycu_ai2024/20240409/output.txt'

with open(csv_file, 'r', encoding='big5') as file:
    reader = csv.reader(file)
    data = list(reader)

with open(output_file, 'w', encoding='big5') as file:
    writer = csv.writer(file)
    writer.writerows(data)

#將csv資料輸出
print(data)

#將資料中的地震時間，經度，緯度，規模，深度，位置利用folium製成地圖
import folium.plugins

# Create a time series map
m = folium.Map(location=[23.5, 121], zoom_start=7)
marker_cluster = folium.plugins.MarkerCluster().add_to(m)
for row in data[1:]:  # Skip the header row
    if row[2] and row[3]:  # Check if the values exist
        try:
            folium.Marker([float(row[3]), float(row[2])], popup=f"經度: {row[2]}, 緯度: {row[3]}, 位置: {row[6]}, 規模: {row[4]}, 深度: {row[5]}").add_to(marker_cluster)
        except ValueError:
            print(f"Cannot convert {row[2]} and {row[3]} to float.")
    else:
        print(f"Missing values at row {data.index(row)}.")

#幫我利用時間製作一個動態地圖
# Add time slider control
folium.plugins.TimestampedGeoJson(
    {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(row[3]), float(row[2])]
                },
                "properties": {
                    "time": row[1],
                    "popup": f"經度: {row[2]}, 緯度: {row[3]}, 位置: {row[6]}, 規模: {row[4]}, 深度: {row[5]}"
                },
            }
            for row in data[1:] if row[2] and row[3]
        ],
    },
    period="P1D",  # Set the time period for each frame
    add_last_point=True,  # Add the last point to the map
).add_to(m)

m.save('/workspaces/cycu_ai2024/20240409/map.html')


