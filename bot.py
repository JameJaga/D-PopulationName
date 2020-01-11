import discord
import os

TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()
num = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):            
    from discord.ext import commands
    guild = message.guild
    member_count = guild.member_count   
    ChannelName = f'Members:{str(member_count)}'
    VoiceChannel = client.get_channel(665387061750136841)
    await VoiceChannel.edit(name=ChannelName)
    VoiceChannel = client.get_channel(665387771736621056)
    await VoiceChannel.edit(name=ChannelName)
    user_count = sum(1 for member in guild.members if not member.bot)
    ChannelName = f'Humans:{str(user_count)}'
    VoiceChannel = client.get_channel(665387186660573206)
    await VoiceChannel.edit(name=ChannelName) 
    bot_count = sum(1 for member in guild.members if member.bot)  
    ChannelName = f'Bots:{str(bot_count)}'
    VoiceChannel = client.get_channel(665387101164142622)
    await VoiceChannel.edit(name=ChannelName) 
    num = len(guild.members)
    GuildName = f'ジャガの部屋 ＋{str(num)}Members'
    await guild.edit(name=GuildName)
client.run(TOKEN)
