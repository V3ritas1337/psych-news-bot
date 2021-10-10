from feed_parser import collect_news
from config import config
from telegram_client import send_message


feeds = config("dev-config.yaml", "feeds")

message = collect_news(feeds)

for link in message:
    send_message(link)