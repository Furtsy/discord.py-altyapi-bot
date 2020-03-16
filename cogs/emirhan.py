from discord.ext import commands
import discord
from random import seçenek
class emirhan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            print(str(message.author)+": "+str(message.content))
        except Exception:
            print(str(message.author)+":")

        if "sa" in message.clean_content.lower():
                await message.channel.send(seçenek(["ALEYKÜM SELAM", "as", "as kardeşim"]))
def setup(bot):
    bot.add_cog(emirhan(bot))