#!/usr/bin/env python3
from feed_parser import collect_news, parse_links
from config import config
from telegram_client import send_message


load_feeds = config("dev-config.yaml", "feeds")

feed = collect_news(load_feeds)
message = parse_links(feed)
print(message)
for link in message:
    # if link is None: -> fix this flow later
    send_message(link)
