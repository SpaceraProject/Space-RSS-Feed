import configparser
from discord.ext import commands
from discord import Embed

class CustomHelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        # Read the configuration file
        config = configparser.ConfigParser()
        config.read('config.ini')
        manual = config['setup']['man_bot']
        embed = Embed(title="Help", description=manual, color=0xeee657)
        await self.context.channel.send(embed=embed)
