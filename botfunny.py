import discord
import os
from tronalddump import api, parse
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()
trump = api.TronaldDumpAPI()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('>help for help'))

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    if message.content.startswith('>help'):
        await message.channel.send('''
            Tronald Dump, A Discord Bot for some of Donald Trumps worst quotes.
            Run >quote to recive a quote from the bot.
            It uses the Tronald Dump api https://TronaldDump.io to recive the quotes.
            The bot is written in python.
            More features will be added eventually in the future.
            GitHub: https://github.com/chimpdev2/tronald-dump-discord-bot
            Made by wesh#0870 on discord, Dm me for any issues.
            Thanks for using!
            (the creator wesh#0870 does not support Donald Trump in any right,
            this bot should only be taken as a joke to make fun of Donald Trump)
            ''')
    
    if message.content.startswith('>quote'):
        quote = trump.random_quote()
        parsed = parse.Parser(quote)
        await message.channel.send(parsed.value())
        await message.channel.send("-Donald Trump")
        await message.channel.send(parsed.date_appeared())

TOKEN = os.getenv("TOKEN")
client.run(TOKEN)
