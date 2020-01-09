import discord
import os

TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    name = 'ジャガの部屋'
    population = guild.member_count
    Gname = name + pupulation + 'Members'
    guild = client.get_guild(662153006787199046)
    await guild.edit(name=Gname)
client.run(TOKEN)
