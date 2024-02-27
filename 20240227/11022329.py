print("Hello World")

#https://news.pts.org.tw/xml/newsfeed.xml 

import feedparser

def print_news_titles(rss_url):
    feed = feedparser.parse(rss_url)
    for newsitem in feed['items']:
        print(newsitem['title'])

# RSS feed URL
rss_url = "https://news.pts.org.tw/xml/newsfeed.xml"

print_news_titles(rss_url)
