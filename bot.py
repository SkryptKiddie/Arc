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

bot = commands.Bot(command_prefix='arc!')
print (discord.version_info)
print (discord.__version__)
print ("Arc is loading...")

@bot.event
async def on_ready():
    print ("Arc is online")
    
# ping command
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pong! :ping_pong:")
    
# about command
@bot.command(pass_context=True)
async def info(ctx):
    await bot.say("My name is Arc and I am written in Discord.py. I was made by Joshek#1337 over the course of a few weeks. I will be getting more features soon.")
    await bot.say("If you wish to support development, check you the code at https://github.com/JoshekDeveloper/Arc.")

# invite command
@bot.command(pass_context=True)
async def invite(ctx):
    await bot.say("My invite is https://discordapp.com/oauth2/authorize?client_id=417982648749654016&scope=bot&permissions=8 .")
    
# support command
@bot.command(pass_context=True)
async def support(ctx):   
    await bot.say("https://discord.gg/cTMfa56")

# joined command
@bot.command(pass_context=True)
async def joined(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    await bot.say('{0} joined the server at {0.joined_at}'.format(member))
    
# this is where you insert your token
bot.run("Token goes here")
