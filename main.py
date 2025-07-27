import discord
from discord.ext import commands

Tks = [
    'token' #input your tokens. starts from 0 to whatever number of token there is. 0 to inf 
]

bot = commands.Bot(command_prefix='!')
C_ID = 510246787450142720 #the channel id. input it here

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    channel = bot.get_channel(C_ID)
    if not channel: return print("Channel not found.")
    print(f'Deleting messages in #{channel.name}')
    async for m in channel.history(limit=None):
        if m.author == bot.user:
            try: await m.delete(); print(f'Deleted: {m.content}')
            except: pass
    print("Done")

bot.run(Tks[0]) #change the number to whatever token you want to use
