# outage_bot
This is a simple Telegram bot that you can add to a group chat. 

## What does it do?
Whenever your internet connection fails, it will notice and start counting. 
When the outage ends, it will send an automated message telling you that your connection is back, and how long the outage lasted.

## Requirements
You need two things to run it yourself:
1. A telegram bot token (get it from the [BotFather]([url](https://telegram.me/BotFather)))
2. The ID of the group chat you want to add it to ([example]([url](https://www.wikihow.com/Know-Chat-ID-on-Telegram-on-Android)https://www.wikihow.com/Know-Chat-ID-on-Telegram-on-Android))
Add these to a `config.json` file with a similar structure as the `config_example.json` file included in this repository. The `bot.py` script will load it and use it.
