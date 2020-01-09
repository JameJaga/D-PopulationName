import discord
import os

TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    name = 'ジャガの部屋'
    member_count(population)
    Gname = name + pupulation + 'Members')
    guild = client.get_guild(662153006787199046)
    await guild.edit(name=Gname)
async def on_member_remove(member):
    name = 'ジャガの部屋'
    member_count(population)
    Gname = name + pupulation + 'Members')
    guild = client.get_guild(662153006787199046)
    await guild.edit(name=Gname)
    
client.run(TOKEN)
