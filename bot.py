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
    guild = client.message.guild
    member_count = guild.member_count 
    user_count = sum(1 for member in guild.members if not member.bot)
    bot_count = sum(1 for member in guild.members if member.bot)  
    TextC_count = len(guild.text_channels)
    VoiceC_count = len(guild.voice_channels)
    Role_count = len(guild.roles)
    Region = guild.region
    
    #参加人数
    ChannelName = f'Members:{str(member_count)}'
    VoiceChannel = client.get_channel(665387061750136841)
    await VoiceChannel.edit(name=ChannelName)
    #Openの方
    VoiceChannel = client.get_channel(665387771736621056)
    await VoiceChannel.edit(name=ChannelName)
    
    #ユーザー数
    ChannelName = f'Humans:{str(user_count)}'
    VoiceChannel = client.get_channel(665387186660573206)
    await VoiceChannel.edit(name=ChannelName) 
    
    #ボット数
    ChannelName = f'Bots:{str(bot_count)}'
    VoiceChannel = client.get_channel(665387101164142622)
    await VoiceChannel.edit(name=ChannelName) 
    
    #テキストチャンネル数
    ChannelName = f'TextChannles:{str(TextC_count)}'
    VoiceChannel = client.get_channel(665387508586119198)
    await VoiceChannel.edit(name=ChannelName) 
    
    #ボイスチャンネル数
    ChannelName = f'VoiceChannels:{str(VoiceC_count)}'
    VoiceChannel = client.get_channel(665387575963549741)
    await VoiceChannel.edit(name=ChannelName)
    
    #チャンネル総数
    ChannelName = f'AllChannels:{str(TextC_count + VoiceC_count)}'
    VoiceChannel = client.get_channel(665387403745165333)
    await VoiceChannel.edit(name=ChannelName)
    
    #ロール総数
    ChannelName = f'Roles:{str(Role_count)}'
    VoiceChannel = client.get_channel(665387612453994496)
    await VoiceChannel.edit(name=ChannelName)
    
    #Region
    ChannelName = f'Region:{str(Region)}'
    VoiceChannel = client.get_channel(665387642925613066)
    await VoiceChannel.edit(name=ChannelName)
    
    num = len(guild.members)
    GuildName = f'ジャガの部屋 ＋{str(num)}Members'
    await guild.edit(name=GuildName)
    
    guild = client.get_guild(662153006787199046)
    
    #全チャンネルのメッセージ数を加算。
    msg_count = 0

    for channel in guild.text_channels:
        msgs = await channel.history(limit=None).flatten()
        msg_count += len(msgs)
    #ここで出力
    ChannelName = f'Messages:{str(msg_count)}'
    VoiceChannel = client.get_channel(665387824471736320)
    await VoiceChannel.edit(name=ChannelName)
    #こっちクローズの方。
    ChannelName = f'Messages:{str(msg_count)}'
    VoiceChannel = client.get_channel(665387351928995842)
    await VoiceChannel.edit(name=ChannelName)
    
    
client.run(TOKEN)
