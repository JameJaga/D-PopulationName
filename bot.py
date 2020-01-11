import discord
import os

TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()
#データベース
num = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
            
    guild = client.get_guild(662153006787199046)
    
    
    
    from discord.ext import commands

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def count(self,ctx,arg): 
        guild = ctx.guild   
        member_count = guild.member_count   
        ChannelName = f'Members:{str(member_count)}'
        VoiceChannel = client.get_channel(665387061750136841)
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
