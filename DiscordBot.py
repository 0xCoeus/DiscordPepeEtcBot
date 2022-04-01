import os 
import discord
import random
from dotenv.main import load_dotenv
from discord.ext import commands


def main():

    bot = commands.Bot(command_prefix = '$')
    load_dotenv()

    @bot.event
    async def on_ready():
        token = os.getenv("DISCORD_TOKEN_ID")
        print('We have logged in as {0.user}'.format(bot))

    @bot.command() 
    async def pepe(ctx):
        path = "C:/Users/nkman/Crypto_Twitter/pepes"
        files = os.listdir(path)
        d = random.choice(files)
        await ctx.channel.send(file=discord.File(f"C:/Users/nkman/Crypto_Twitter/pepes/{d}"))


    bot.run(os.getenv("DISCORD_TOKEN_ID"))

if __name__ == '__main__':
    main()