import dateutil.parser
import feedparser
from dateutil import parser
from datetime import timedelta, datetime
from datetime import date, datetime

def collect_news(feeds: list):
    feed = [item for feed in feeds for item in feed.values()]
    feeds = [feedparser.parse(url)['entries'] for url in feed]
    for feed in feeds:
        feed.sort(key=lambda x: dateutil.parser.parse(x['published']))
        return feed

def parse_links(feed: list):
    links = []
    for data in feed:
        parsed_date = parser.parse(data.published)
        parsed_date = (parsed_date - timedelta(hours=8)).replace(tzinfo=None) # remove timezone offset
        now_date = datetime.utcnow()

        published_20_minutes_ago = now_date - parsed_date < timedelta(minutes=20)
        if published_20_minutes_ago:
             links.append(data['link'])
    return links