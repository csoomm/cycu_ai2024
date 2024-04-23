import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

def download_files(url, save_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all('a'):
        href = link.get('href')
        if href.endswith('/'):  # This is a folder
            folder_name = urllib.parse.urlparse(href).path.rstrip('/').split('/')[-1]
            folder_path = os.path.join(save_path, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            download_files(url + href, folder_path)
        else:  # This is a file
            file_url = url + href
            file_response = requests.get(file_url)
            file_name = urllib.parse.urlparse(file_url).path.split('/')[-1]
            if file_name and os.path.splitext(file_name)[1]:  # Check if file_name is not empty and has a file extension
                with open(os.path.join(save_path, file_name), 'wb') as f:
                    f.write(file_response.content)

base_url = 'https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240422/'
download_files(base_url, 'C:/Users/User/Desktop/資料庫')