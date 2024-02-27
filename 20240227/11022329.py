#https://news.pts.org.tw/xml/newsfeed.xml
import feedparser

def print_news_titles_and_content(rss_url):
    feed = feedparser.parse(rss_url)
    for newsitem in feed['items']:
        print(newsitem['title'])
        print(newsitem['summary'])
        print("------")

# RSS feed URL
rss_url = "https://news.pts.org.tw/xml/newsfeed.xml"

print_news_titles_and_content(rss_url)

#幫我把帶有YouBike的新聞標題和內文印出來
if __name__ == "__main__":
    rss_url = "https://news.pts.org.tw/xml/newsfeed.xml"
    feed = feedparser.parse(rss_url)
    for newsitem in feed['items']:
        if "YouBike" in newsitem['title']:
            print(newsitem['title'])
            print(newsitem['summary'])
            print("------")

#幫我製成excel檔，檔名為0227作業，並儲存在桌面
if __name__ == "__main__":
    rss_url = "https://news.pts.org.tw/xml/newsfeed.xml"
    feed = feedparser.parse(rss_url)
    for newsitem in feed['items']:
        if "YouBike" in newsitem['title']:
            print(newsitem['title'])
            print(newsitem['summary'])
            print("------")
            import os
            import xlsxwriter
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            workbook = xlsxwriter.Workbook(desktop + '/0227作業.xlsx')
            worksheet = workbook.add_worksheet()
            worksheet.write('A1', newsitem['title'])
            worksheet.write('A2', newsitem['summary'])
            workbook.close()
            