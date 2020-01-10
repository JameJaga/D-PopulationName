import discord
import os

TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    NameBase = 'ジャガの部屋'
    guild = client.get_guild('662153006787199046')
    population = len(guild.members)
    #メモ
    #population = guild.member_count
    GuildName = NameBase + pupulation + 'Members'
    await guild.edit(name=GuildName)
client.run(TOKEN)
