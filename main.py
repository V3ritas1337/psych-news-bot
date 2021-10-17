from feed_parser import collect_news, parse_links
from config import config
from telegram_client import send_message


load_feeds = config("dev-config.yaml", "feeds")

feed = collect_news(feeds)
message = parse_links(feed)
for link in message:
    send_message(link)
