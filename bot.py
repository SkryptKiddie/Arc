# Arc by Joshek
# Written in Discord.py

import discord
import asyncio
import time
import logging
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='arc!', formatter=None, pm_help=True, description="Hi, I'm Arc. These are my commands. If you find any bugs, please DM Joshek#1337.", CommandNotFound="Invalid command!", owner_id= "372931332239654912")
print (discord.version_info) # prints discord.py version
print (discord.__version__) # prints discord.py version
print ("Arc v2.3.1") # current bot version
print ("Connecting and loading...")

@bot.event
async def on_ready():
    print ("Arc is online.") # bot is online and listening

# about command
@bot.command(pass_context=True)
async def about(ctx):
    """Information about the bot."""
    embed=discord.Embed(title="About Arc", description="Hello there :wave:, Iâ€™m Arc. Iâ€™m here to make your Discord server better with utilitarian features and moderation. Here are some links to where you can find out more about me!", color=0x0080c0)
    embed.set_thumbnail(url="https://joshek.xyz/arc/arc.png")
    embed.add_field(name="Support", value="https://discord.gg/cTMfa56", inline=True)
    embed.add_field(name="Website", value="https://joshek.xyz/arc", inline=True)
    embed.add_field(name="Donate", value="https://ko-fi.com/joshek", inline=True)
    embed.set_footer(text="Written by Joshek#1337 in Discord.py")
    await bot.say(embed=embed)
    print ("User ran about")

# update log
@bot.command(pass_context=True)
async def updates(ctx):
    """Update log."""
    embed=discord.Embed(title="Version 2.4.0", color=0xff8040)
    embed.set_thumbnail(url="https://joshek.xyz/arc/arc.png")
    embed.set_author(name="Update log")
    embed.add_field(name="Updated moderation system.", value="Moderation commands now work by permissions.", inline=True)
    embed.add_field(name="Added low-level logging.", value="Internal change.", inline=True)
    embed.add_field(name="emoved quickstart.", value="No longer required.", inline=True)
    embed.set_thumbnail(url="https://joshek.xyz/Arc.png")
    embed.set_footer(text="New features are always being added.")
    await bot.say(embed=embed)
    print ("User ran updates")

# donate commmand
@bot.command(pass_context = True)
async def donate(ctx):
    """Links to donate to the development."""
    embed=discord.Embed(title="Buy me a coffee.", url="https://ko-fi.com/joshek", description="Help support the development of Arc.", color=0xff0000)
    embed.set_thumbnail(url="https://joshek.xyz/arc/arc.png")
    embed.set_author(name="Donate.")
    embed.set_footer(text="I'll always host Arc, but donations help me.")
    await bot.say(embed=embed)
    print ("User ran donations")


# ping command
@bot.command(pass_context=True)
async def ping(ctx):
    """Ping the bot."""
    embed = discord.Embed(title="Pong! :ping_pong:", color=0x8080ff)
    await bot.say(embed=embed)
    print ("User ran ping")
    
# invite command
@bot.command(pass_context=True)
async def invite(ctx):
    """Invite link for the bot."""
    embed=discord.Embed(title="Invite Arc to your server.", url="https://discordapp.com/oauth2/authorize?client_id=417982648749654016&scope=bot&permissions=8", color=0x80ff00)
    embed.set_thumbnail(url="https://joshek.xyz/arc/arc.png")
    embed.set_footer(text="Add Arc to your server (requires manage server permissions)")
    await bot.say(embed=embed) 
    print ("User ran invite")

# botsay command
@bot.command(pass_context=True)
async def say(ctx, arg):
    """Speak as the bot."""
    await bot.say(arg)
    print ("User ran botsay")

# serverinfo command
@bot.command(pass_context=True)
async def serverinfo(ctx):
    """Displays server information."""
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's the server details.", color=0x00ff00)
    embed.add_field(name="Server Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Server ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)
    print ("User ran serverinfo")

# userinfo command
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    """Displays user information."""
    await bot.say("Username: {}".format(user.name))
    await bot.say("User ID: {}".format(user.id))
    await bot.say("Status: {}".format(user.status))
    # await bot.say("Roles: {}".format(user.roles))
    await bot.say("Join date: {}".format(user.joined_at))
    print ("User ran userinfo")
   
# joined command
@bot.command(pass_context=True)
async def joined(ctx, member: discord.Member = None):
    """Shows when a user joined the server."""
    if member is None:
        member = ctx.message.author
    await bot.say('{0} joined the server at {0.joined_at}'.format(member))
    print ("User ran joined")

# kick command
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True, kick_members=True)
async def kick(ctx, user: discord.Member):
    """Kicks a user. (requires role called staff)"""
    await bot.say("User kicked!")
    await bot.kick(user)
    print ("User ran kick")

# ban command
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True, ban_members=True)
async def ban(ctx, user: discord.Member):
    """Bans a user. (requires role called staff)"""
    await bot.say("User banned!")
    await bot.ban(user)
    print ("User ran ban")
    
# addition command
@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)
    print ("User ran add")
    
# logs
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


# this is where you insert your token
bot.run("Token goes here")

