import asyncio
import json
import os

from datetime import datetime
from dataclasses import dataclass
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

@dataclass
class Config:
    telegram_bot_token: str
    telegram_group_chat_id: str
    ping_timeout_seconds: int = 20
    ping_ip: str = '8.8.8.8'

class ConfigNotFound(Exception):
    pass

class ConfigIncomplete(Exception):
    pass

try:
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        config = Config(**config)
except FileNotFoundError:
    raise ConfigNotFound(
        f"config.json missing from {os.getcwd()}, " \
        "please follow the instructions in README.md"
    )
except TypeError:
    raise ConfigIncomplete(
        f"config.json in {os.getcwd()} is missing some settings, " \
        "please follow the instructions in README.md"
    )

# Initialize Telegram Bot
bot = Bot(token=config.telegram_bot_token)

# How do we test whether the internet works? By pinging!
def is_internet_on():
    try:
        response = ping(config.ping_ip)
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
                message = f"Internet outage ended. Duration: {outage_duration:.2f} " \
                    f"+- {config.ping_timeout_seconds:.2f} minutes"
                await bot.send_message(chat_id=config.telegram_group_chat_id, text=message)
                connected = True
        else:
            if connected:
                # Internet just went out
                outage_start = datetime.now()
                connected = False

        await asyncio.sleep(config.ping_timeout_seconds)  # Check every 20 seconds

if __name__ == "__main__":
    asyncio.run(main())
