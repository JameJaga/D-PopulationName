import discord
import os

TOKEN = os.environ.get("DISCORD_TOKEN")
PrintChannelID = 662153006787199046

client = discord.Client()
#データベース
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
    GuildName = 'ジャガの部屋　＋' + '('+ str(num) + ')' + 'Members'
    guildname = f'ジャガの部屋　＋{str(num)}Members'
    await guild.edit(name=GuildName)
client.run(TOKEN)
