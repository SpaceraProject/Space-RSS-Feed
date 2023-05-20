import configparser
from discord.ext import commands

class CustomHelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        # Read the configuration file
        config = configparser.ConfigParser()
        config.read('config.ini')
        manual = config['setup']['man_bot']
        await self.context.channel.send(manual)
