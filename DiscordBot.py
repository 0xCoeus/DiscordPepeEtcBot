import os 
import discord
import random
from dotenv.main import load_dotenv


def main():

    client = discord.Client() 
    load_dotenv()

    @client.event
    async def on_ready():
        token = os.getenv("DISCORD_TOKEN_ID")
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        token = os.getenv("DISCORD_TOKEN_ID")
        if message.content == '$pepe':
          path = "C:/Users/nkman/Crypto_Twitter/pepes"
          files = os.listdir(path)
          d = random.choice(files)
          await message.channel.send(file=discord.File(f"C:/Users/nkman/Crypto_Twitter/pepes/{d}"))


    client.run('OTQyNDY5NDU1NjUxNDMwNTgx.Ygk9FA.KmS0TR2x0__PIClDa0dM09iGagE')