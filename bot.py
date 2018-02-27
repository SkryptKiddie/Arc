# Arc by Joshek

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='/')

print (discord.__version__)

@bot.event
async def on_ready():
    print ("Arc is online")
    await client.change_presence(game=discord.Game(name="with code"))

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
    
bot.run("Token goes here")
