# outage_bot
This is a simple Telegram bot that you can add to a group chat. 

## What does it do?
Whenever your internet connection fails, it will notice and start counting. 
When the outage ends, it will send an automated message telling you that your connection is back, and how long the outage lasted:

![image](https://github.com/MartijnWitjes/outage_bot/assets/99734480/81aeb20d-0860-4155-b638-c6e3429c66c8)

## Requirements
You need a couple of things things to run it yourself:
1. A python environment with the additional packages `ping3` and `python-telegram-bot`.
2. A telegram bot token (get it from the [BotFather]([url](https://telegram.me/BotFather)))
3. The ID of the group chat you want to add it to ([example]([url](https://www.wikihow.com/Know-Chat-ID-on-Telegram-on-Android)https://www.wikihow.com/Know-Chat-ID-on-Telegram-on-Android))

Add the bot token and group chat ID to a `config.json` file with a similar structure as the `config_example.json` file included in this repository. The `bot.py` script will load it and use it.

Tell python to run `bot.py` and it should work! Happy outage tracking!


