import telegram
from config import config
# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.

auth = config("dev-config.yaml", "telegram")

def send_message(text: str):
    bot = telegram.Bot(token=auth[0]['botToken'])
    bot.send_message(text=text, chat_id=auth[1]['chatId'])