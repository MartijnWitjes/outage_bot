import asyncio
import json

from datetime import datetime
from telegram import Bot
from ping3 import ping

# Read the config.json file to get the telegram bot token and telegram group chat id
'''
You can get a bot token by contacting the BotFather on Telegram
Then, get a group chat ID by adding it to your group and then visiting:
https://api.telegram.org/bot<YourBOTToken>/getUpdates
and look for "chat":{"id":-zzzzzzzzzz,
-zzzzzzzzzz is your chat id (with the negative sign).
Put this in a config.json file that follows the structure of the config_example.json file in this repository.
'''

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    bot_token = config['telegram_bot_token']
    group_chat_id = config['telegram_group_chat_id']

# Initialize Telegram Bot
bot = Bot(token=bot_token)

# How do we test whether the internet works? By pinging!
def is_internet_on():
    try:
        response = ping('8.8.8.8')
        return response is not None
    except Exception:
        return False

async def main():
    connected = True
    outage_start = None

    while True:
        if is_internet_on():
            if not connected:
                # Internet just came back
                outage_end = datetime.now()
                outage_duration = (outage_end - outage_start).total_seconds() / 60  # duration in minutes
                message = f"Internet outage ended. Duration: {outage_duration:.2f} minutes"
                await bot.send_message(chat_id=group_chat_id, text=message)
                connected = True
        else:
            if connected:
                # Internet just went out
                outage_start = datetime.now()
                connected = False

        await asyncio.sleep(20)  # Check every 20 seconds

if __name__ == "__main__":
    asyncio.run(main())
