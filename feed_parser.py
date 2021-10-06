import feedparser
from config import PA, TR, CS, PSW
from datetime import date, datetime


def parser(symbol):
    NewsFeed = feedparser.parse(symbol)
    entry = NewsFeed.entries
    return entry # entry.published_parsed

# TODO: if todays date same as published_parsed, print link :) 
# print(datetime(parser(PA)[:6]))
print(parser(TR))
print(parser(TR).published_parsed)
# https://waylonwalker.com/parsing-rss-python/

# print(date.split(' '))