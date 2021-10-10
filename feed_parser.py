# import feedparser
import dateutil.parser
import feedparser
from config import config
from datetime import date, datetime


feeds = config("dev-config.yaml", "feeds")
def collect_news(feeds: list):
    feed = [item for feed in feeds for item in feed.values()]
    feeds = [feedparser.parse(url)['entries'] for url in feed]
    links = []

    for feed in feeds:
        feed.sort(key=lambda x: dateutil.parser.parse(x['published']), reverse=True)
        for data in feed:
            # print(data.keys())
            # links.append(data['link'])
            # print("LINK: " + str(data['link']) + '\n' + "Date Published: " + 
            print(str(data['published']))
            # print(data.keys())
    # return links


collect_news(feeds)


