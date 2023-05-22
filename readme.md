# RSS Feed Discord Bot

## Description:
The RSS Feed Discord Bot is a Discord bot that allows you to follow RSS feeds and receive notifications on Discord when a new post is published on the RSS feed. By default, the bot checks the RSS feed every 10 minutes for the Space.com website.

## Bot commands:
- `!help`: Displays the list of bot commands. (not implemented)
- `!stop`: Manually stops the bot.
- `!start`: Manually starts the bot.
- `!status`: Displays the bot's status.
- `!ping`: Displays the bot's ping.

## Prerequisites:
- Python 3.8 or higher
- A Discord account
- A Discord server

## Installation:
- Download the source code of the Discord RSS Feed bot.
- Install the dependencies using the command `pip install -r requirements.txt`.
- Create a bot application on the [Discord Developers Portal](https://discord.com/developers/applications).
- You need to enable intents under `*YourApplication*/Bot/Privileged Gateway Intents`.
- Add the bot to your Discord server.
- Modify the `config.ini` file and add the required information.
- Run the `main.py` file to start the bot.

## Dependencies:
### Built-in Python dependencies:
- time: The time library is used to manage dates and times.
- configparser: The configparser library is used to read configuration files.

### External dependencies to install:
- discord.py: The Discord.py library allows interaction with the Discord API and the creation of Discord bots in Python.
- feedparser: The feedparser library is used to parse RSS feeds. It allows retrieving data from feed entries.

Make sure to install these dependencies before running the code. You can add them to your `requirements.txt` file using the following commands:

```
discord.py
feedparser
```

Then, you can install all the dependencies at once by using the command `pip install -r requirements.txt`.

## Configuration:
To configure the bot, you need to modify the `sample.config.ini` file and add the following information:
- `token`: Your Discord bot token.
- `channel_id`: The ID of the Discord channel where you want to receive notifications.
- `rss_url`: The URL of the RSS feed you want to follow.
- `check_interval`: The time interval between each RSS feed check (in minutes).
- `bot_prefix`: The prefix you want to use for the bot commands.

Rename the `sample.config.ini` file to `config.ini`.
By default, the bot checks the RSS feed every 10 minutes for the Space.com site. If you want to follow another RSS feed, you need to modify the information in the `config.ini` file. 
Also, modify the message sent by the bot in the `main.py` file:
```python
# Send the message to the Discord channel
message = f"**New post on Space.com!**\nTitle: {title}\nLink: {link}\nSummary: {summary}"
await channel.send(message)
```

### Intents
The bot uses all intents by default, which are required for simple things like displaying the member count or take charge of the commands. 
You need to enable those intents in the [Discord Developers Portal](https://discord.com/developers/applications) 
under `Privileged Gateway Intents`.   
It's possible to reconfigure the requested intents in `main.py` if you don't need them.  
But I'd suggest using all of them for the beginning, especially if you're relatively new to discord.py.  
This will only be an issue if your bot reaches more than 100 servers, then you have to apply for those intents.