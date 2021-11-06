from dateutil import parser
from datetime import timedelta, datetime
from config import config
import dateutil.parser
import feedparser

def collect_news(feeds: list):
    '''Collects and Organises Feeds fed from config into one decentralised feed for parsing'''
    
    collected_news = []
    
    feed = [item for feed in feeds for item in feed.values()]
    feeds = [feedparser.parse(url)['entries'] for url in feed]
    
    for feed in feeds:
        feed.sort(key=lambda x: dateutil.parser.parse(x['published']))
        collected_news.append(feed)
    
    return collected_news

def parse_links(feeds: list):
    '''Checks date of object found in the decentralised feed
    and if date of object is from past 20 minutes,
    it will add link associated with object to list for Telegram'''
    
    links = []

    for feed in feeds:
        for data in feed:
            parsed_date = parser.parse(data.published)
            parsed_date = (parsed_date - timedelta(hours=8)).replace(tzinfo=None)
            now_date = datetime.utcnow()

            published_20_minutes_ago = now_date - parsed_date < timedelta(minutes=20)
            if published_20_minutes_ago:
                links.append(data['link'])
    
    return links
