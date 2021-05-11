import feedparser
from config import PA, TR, CS, PSW
from datetime import date, datetime


def parser(symbol):
    NewsFeed = feedparser.parse(symbol)
    entry = NewsFeed.entries[1]
    return entry # entry.published_parsed

# TODO: if todays date same as published_parsed, print link :) 
# print(datetime(*parser(PA)[:6]))
print(parser(PA).link)


# print(date.split(' '))