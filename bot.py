import discord
import os
import sys

TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()
num = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    guild = client.get_guild(662153006787199046)
    num = len(guild.members)
    #メモ

   #num = guild.member_count
    GuildName = 'ジャガの部屋　　' + num + 'Members'
    await guild.edit(name=GuildName)
client.run(TOKEN)
