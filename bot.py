import discord

TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def discord.on_group_join(channel, user)
    name = "ジャガの部屋"
    population = member_count
    Gname = name + pupulation
    guild = client.get_guild(662153006787199046)
    await guild.edit(name=Gname)
async def discord.on_group_remove(channel, user)
    name = "ジャガの部屋"
    population = member_count
    Gname = name + pupulation
    guild = client.get_guild(662153006787199046)
    await guild.edit(name=Gname)
    
client.run(TOKEN)
