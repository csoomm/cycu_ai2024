import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 網頁的URL
for hour in range(24):
    url = f"https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240429/{hour:02d}/"
    # 下載的資料夾
    download_folder = "/workspaces/cycu_ai2024/20240430"
    # 獲取網頁的內容
    response = requests.get(url)
    # 解析網頁的內容
    soup = BeautifulSoup(response.text, "html.parser")
    # 找出所有的連結
    links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]
    # 對每一個連結，檢查是否指向一個csv檔案，如果是，則下載檔案並儲存到指定的資料夾
    for link in links:
        if link.endswith('.csv'):
            # 下載檔案
            response = requests.get(link)
            
            # 檔案的名稱
            file_name = os.path.join(download_folder, link.split('/')[-1])
            
            # 儲存檔案
            with open(file_name, 'wb') as f:
                f.write(response.content)

