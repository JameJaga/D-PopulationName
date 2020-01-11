import discord
import os
import sys

TOKEN = os.environ.get("DISCORD_TOKEN")
PrintChannelID = 662153006787199046

client = discord.Client()
#データベース
dburl = URL(os.environ.get("DATABASE_URL"))
host = dburl.host
user = dburl.user
database = dburl.path[1:]
port = dburl.port
password = dburl.password
print('host = ' + str(host))
print('user = ' + str(user))
print('database = ' + str(database))
print('port = ' + str(port))
print('password = ' + str(password))

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
    GuildName = 'ジャガの部屋' + '('+ str(num) + ')' + 'Members'
    await guild.edit(name=GuildName)
client.run(TOKEN)
