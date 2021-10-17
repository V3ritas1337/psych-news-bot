import dateutil.parser
import feedparser
from dateutil import parser
from datetime import timedelta, datetime
from config import config
from datetime import date, datetime

feeds = config("dev-config.yaml", "feeds")

def collect_news(feeds: list):
    feed = [item for feed in feeds for item in feed.values()]
    feeds = [feedparser.parse(url)['entries'] for url in feed]
    for feed in feeds:
        feed.sort(key=lambda x: dateutil.parser.parse(x['published']))
        return feed

def parse_date(feed: list):
    for data in feed:
        parsed_date = parser.parse(data.published)
        parsed_date = (parsed_date - timedelta(hours=8)).replace(tzinfo=None) # remove timezone offset
        now_date = datetime.utcnow()

        published_20_minutes_ago = now_date - parsed_date < timedelta(minutes=20)
        if published_20_minutes_ago:
            send_message(entry.links[0].href)
            print(data.links[0].href)
        # print("LINK: " + str(data['link']) + '\n' + "Date Published: " + str(data['published']))
        print(parsed_date)
        print(now_date)
        print(published_20_minutes_ago)




            # print(data.keys())
            # links.append(data['link'])
            # print("LINK: " + str(data['link']) + '\n' + "Date Published: " + str(data['published']))
            # print(data.keys())
    # return links