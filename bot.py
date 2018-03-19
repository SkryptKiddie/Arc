#           _____                    _____                    _____                  
#          /\    \                  /\    \                  /\    \                 
#         /::\    \                /::\    \                /::\    \                
#        /::::\    \              /::::\    \              /::::\    \               
#       /::::::\    \            /::::::\    \            /::::::\    \              
#      /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \             
#     /:::/__\:::\    \        /:::/__\:::\    \        /:::/  \:::\    \            
#    /::::\   \:::\    \      /::::\   \:::\    \      /:::/    \:::\    \           
#   /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/    / \:::\    \          
#  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\  /:::/    /   \:::\    \         
# /:::/  \:::\   \:::\____\/:::/  \:::\   \:::|    |/:::/____/     \:::\____\        
# \::/    \:::\  /:::/    /\::/   |::::\  /:::|____|\:::\    \      \::/    /        
#  \/____/ \:::\/:::/    /  \/____|:::::\/:::/    /  \:::\    \      \/____/         
#           \::::::/    /         |:::::::::/    /    \:::\    \                     
#            \::::/    /          |::|\::::/    /      \:::\    \                    
#            /:::/    /           |::| \::/____/        \:::\    \                   
#           /:::/    /            |::|  ~|               \:::\    \                  
#          /:::/    /             |::|   |                \:::\    \                 
#         /:::/    /              \::|   |                 \:::\____\                
#         \::/    /                \:|   |                  \::/    /                
#          \/____/                  \|___|                   \/____/                 
#                                                                                   
# 
#
# Arc by Joshek

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


bot = commands.Bot(command_prefix='arc!', formatter=None, pm_help=True, description='Writen by Joshek#1337', command_not_found='Invalid command!')
print (discord.version_info)
print (discord.__version__)
print ("Connecting to the Discord API...")

@bot.event
async def on_ready():
    print ("Arc is online")   

# ping command
@bot.command(pass_context=True)
async def ping(ctx):
    embed = discord.Embed(title="Pong! :ping_pong:")
    await bot.say(embed=embed)
    
# invite command
@bot.command(pass_context=True)
async def invite(ctx):
    embed=discord.Embed(title="Invite Arc to your server", url="https://discordapp.com/oauth2/authorize?client_id=417982648749654016&scope=bot&permissions=8", color=0x80ff00)
    embed.set_footer(text="Written by Joshek#1337 in Discord.py")
    await bot.say(embed=embed)  
    
# joined command
@bot.command(pass_context=True)
async def joined(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    await bot.say('{0} joined the server at {0.joined_at}'.format(member))

# about command
@bot.command(pass_context=True)
async def about(ctx):
    embed=discord.Embed(title="About Arc", description="Hi, I'm Arc. I'm a Discord bot. I am under development and will be going offline frequently as I get more features, mainly because my creator can't figure out how a development bot works.", color=0x0080c0)
    embed.add_field(name="GitHub", value="https://github.com/JoshekDeveloper/Arc", inline=True)
    embed.add_field(name="Support", value="https://discord.gg/cTMfa56", inline=True)
    embed.set_footer(text="Written by Joshek#1337 in Discord.py")
    await bot.say(embed=embed)

# this is where you insert you token
bot.run("Token goes here")
