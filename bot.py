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

# Insert your prefix here
bot = commands.Bot(command_prefix='PREFIX GOES HERE')

print (discord.__version__)

@bot.event
async def on_ready():
    print ("Arc is online")

# ping command
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pong!")

# userinfo command
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    embed = discord.Embed(title)
    await bot.say("Username: {}".format(user.name))
    await bot.say("User ID: {}".format(user.id))
    await bot.say("Status: {}".format(user.status))
    await bot.say("Roles: {}".format(user.roles))
    await bot.say("Join date: {}".format(user.joined_at))

# kick command
@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say("{} has been kicked.".format(user.name))
    await bot.kick(user)

# ban command
@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say("{} has been banned.".format(user.name))
    await bot.ban(user)

# about command
async def about(ctx):
    embed = discord.Embed(title="Bot made by Joshek#1337", description="Hi, I'm Arc, I'm a bot made in Discord.py by my wonderful creator, Joshek.", color=0x35FA00)
    embed.set_footer(text="If you find any bugs, report them to my creator so he can fix them!")
    await bot.say(embed=embed)
    
# server command
async def server(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's the server details", color=0x00ff00)
    embed.set_author(name="Arc")
    embed.add_field(name="Guild Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Guild ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Member count", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

# this is where you insert you token
bot.run("TOKEN GOES HERE")
