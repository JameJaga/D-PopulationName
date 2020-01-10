import discord
import os
import sys

TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()
pupulation = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    guild = client.get_guild(662153006787199046)
    #population = len(guild.members)
    #メモ

    pupulation = guild.member_count
    GuildName = 'ジャガの部屋' + ' ('+ str(population) + ')' + 'Members'
    await guild.edit(name=GuildName)
client.run(TOKEN)
