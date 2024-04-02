# crawler from rss of central weather agency

import requests
import xml.etree.ElementTree as ET
import json
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import os

import feedparser

# url = https://www.cwa.gov.tw/rss/forecast/36_01.xml
# 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, to 22

for num in range(1, 23):
    #string format with prefix 0 if num < 10
    url = 'https://www.cwa.gov.tw/rss/forecast/36_' + str(num).zfill(2) + '.xml'
    print(url)
    #get xml from url
    response = requests.get(url)
    #parse rss feed
    feed = feedparser.parse(response.content)
    #print titles containing "溫度"
    for entry in feed.entries:
        if "溫度" in entry.title:
            print(entry.title[:3] + entry.title.split("溫度:")[1].split("降雨機率")[0])
        
    print("============================")
