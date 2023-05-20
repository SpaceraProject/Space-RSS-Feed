from discord.ext import commands, tasks
from discord import Intents
import feedparser
import time
import configparser

# Read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')
channel_id = int(config['setup']['channel'])
token = config['setup']['token']
url_feed = config['setup']['rss_url']
interval = int(config['setup']['check_interval'])
prefix = config['setup']['bot_prefix']
manual = config['setup']['man_bot']

intents = Intents.all()
intents.members = True
intents.typing = True
intents.presences = True
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, intents=intents)

# List to store the IDs of the already displayed items
displayed_elements = []


# Startup event
@bot.event
async def on_ready():
    print(f'Connected as {bot.user.name}')
    await check_rss.start()  # Start the scheduled task to check the RSS feed


# Scheduled task to check the RSS feed
@tasks.loop(minutes=interval)
async def check_rss():
    t = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
    print(f"{t} Checking RSS feed...")
    # Read the RSS feed
    feed = feedparser.parse(url_feed)
    # Get the channel object
    channel = bot.get_channel(channel_id)

    # Iterate over the entries in the RSS feed in reverse order (from oldest to newest)
    for entry in feed.entries[::-1]:
        identifier = entry.id

        # Check if the item has already been displayed
        if identifier not in displayed_elements:
            title = entry.title
            link = entry.link
            summary = entry.summary

            # Send the message to the Discord channel
            message = f"**New post on Space.com!**\nTitle: {title}\nLink: {link}\nSummary: {summary}"
            await channel.send(message)

            # Add the identifier of the item to the list of displayed elements
            displayed_elements.append(identifier)
            # If the list contains more than 10 elements, remove the first element
            if len(displayed_elements) > 10:
                displayed_elements.pop(0)


# Command to manually start the checking (for testing)
@bot.command()
async def start(ctx):
    # Check if the task is already running
    if not check_rss.is_running():
        print("Starting RSS feed checking...")
        await ctx.send("RSS feed checking started!")
        await check_rss.start()
    else:
        await ctx.send("RSS feed checking is already running!")


# Command to manually stop the checking
@bot.command()
async def stop(ctx):
    # Check if the task is running
    if check_rss.is_running():
        print("Stopping RSS feed checking...")
        check_rss.cancel()
        await ctx.send("RSS feed checking stopped!")
    else:
        await ctx.send("RSS feed checking is not running!")


@bot.command()
async def status(ctx):
    if check_rss.is_running():
        await ctx.send("RSS feed checking is running!")
    else:
        await ctx.send("RSS feed checking is not running!")


# Error handler
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # Ignore the CommandNotFound error without taking any action


# Run the bot
bot.run(token)
