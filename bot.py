import discord # Arc by Joshek#1337
import asyncio # Written in Discord.py asyncio because I can't be arsed to learn rewrite
import logging # Thank you DJ Electro#8950 for debug, ownercheck and error handling.
import aiohttp # Embeds were generated using https://cog-creators.github.io/discord-embed-sandbox/
import traceback # Open source but it's mainly mine.
import sys # Support server invite is https://discord.gg/smHzBYD
import json # This code comes with no warrenty or support because you shouldn't be hosting it
import random
import datetime
import time
import requests
import os
import subprocess
from discord.ext import commands
from discord.ext.commands import Bot

token = ""
prefix = ""
owner = ""

# Configuration and settings
dbltoken = ""
url = "https://discordbots.org/api/bots//stats"
headers = {"Authorization" : dbltoken}
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
bot.remove_command('help')
startup = open("arc.txt") # arc.txt is required for the ASCII logo to display but is not required.
print(startup.read()) # just remove these lines if you don't want it.
print("Connecting to Discord API...")

# Successful API connection.
@bot.event
async def on_ready():
    print("Connected to Discord API.")
    print("Loading status...")
    await bot.change_presence(game=discord.Game(name="arc!help | {} servers and {} users | joshek.xyz/arc".format(len(bot.servers), len(set(bot.get_all_members()))), type=3))
    print("Loading complete!")
    print("Primed and set.")
	
# Specify bot owners ID for owner-only commands.
def ownercheck(ctx):
    return ctx.message.author.id == owner

# General Commands.
# help command
@bot.command(pass_context=True)
async def help(ctx):
    embed=discord.Embed(title="Help is on the way!", color=0x0080ff)
    embed.set_author(name="Better docs", url="https://github.com/SkryptKiddie/Arc/blob/master/commands.md")
    await bot.say(embed=embed)
    embed=discord.Embed(title="General.", color=0x176cd5)
    embed.set_author(name="Website.", url="https://joshek.xyz/arc/", icon_url="https://joshek.xyz/arc/images/ArcLogo.png")
    embed.add_field(name="`about`", value="Show's information.", inline=True)
    embed.add_field(name="`stats`", value="Show's technical details.", inline=True)
    embed.add_field(name="`support`", value="Invite to support server.", inline=True)
    embed.add_field(name="`donate`", value="Donate to the development.", inline=True)
    embed.add_field(name="`ping`", value="Pong!", inline=True)
    embed.add_field(name="`invite`", value="Invite the bot to your server.", inline=True)
    await bot.send_message(ctx.message.author, embed=embed)
    embed=discord.Embed(title="Moderation.", color=0xff8080)
    embed.add_field(name="`serverinfo`", value="Displays server details.", inline=True)
    embed.add_field(name="`userinfo`", value="Displays user details.", inline=True)
    embed.add_field(name="`warn`", value="Warn a user.", inline=True)
    embed.add_field(name="`kick`", value="Kick a user.", inline=True)
    embed.add_field(name="`ban`", value="Ban a user.", inline=True)
    embed.add_field(name="`purge`", value="Purge messages.", inline=True)
    embed.add_field(name="`avatar`", value="Shows a users avatar.", inline=True)
    embed.add_field(name="`mute`", value="Mute a user.", inline=True)
    embed.add_field(name="`unmute`", value="Unmute a user.", inline=True)
    embed.add_field(name="`addrole`", value="Add a role.", inline=True)
    embed.add_field(name="`removerole`", value="Remove a role.", inline=True)
    embed.add_field(name="`announce`", value="Send an announcement.", inline=True)
    await bot.send_message(ctx.message.author, embed=embed)
    embed=discord.Embed(title="Fun.", color=0xffff80)
    embed.add_field(name="`slap`", value="Slap a user.", inline=True)
    embed.add_field(name="`lick`", value="Lick a user.", inline=True)
    embed.add_field(name="`punch`", value="Punch a user.", inline=True)
    embed.add_field(name="`hug`", value="Hug a user.", inline=True)
    embed.add_field(name="`cat`", value="Picture of a cat.", inline=True)
    embed.add_field(name="`duck`", value="Picture of a duck.", inline=True)
    embed.add_field(name="`cookie`", value="Give someone a cookie.", inline=True)
    embed.add_field(name="`choose`", value="Make a choice.", inline=True)
    embed.add_field(name="`roll`", value="Roll a dice in NdN format.", inline=True)
    embed.add_field(name="`wherewedroppin`", value="Selects a random location on the Fortnite map to drop at.", inline=True)
    embed.add_field(name="`speak`", value="Helpful for announcements.", inline=True)
    embed.add_field(name="`gamenews`", value="Get the latest news for a game with a steam game ID.", inline=True)
    embed.add_field(name="`json`", value="Make a request to a JSON API.", inline=True)
    embed.add_field(name="`weather`", value="Gives you weather details for a specified area.")
    await bot.send_message(ctx.message.author, embed=embed)

# stats command
@bot.command(pass_context=True)
async def stats(ctx):
    ping = (time.monotonic()) / 1000
    embed=discord.Embed(title="Technical details.", color=0x176cd5)
    embed.add_field(name="Guilds", value=len(bot.servers), inline=True)
    embed.add_field(name="Members", value=len(set(bot.get_all_members())), inline=True)
    embed.add_field(name="Channels", value=len(set(bot.get_all_channels())), inline=True)
    embed.add_field(name="Emojis", value=len(set(bot.get_all_emojis())), inline=True)
    embed.add_field(name="Discord.py release", value=discord.version_info, inline=True)
    embed.add_field(name="Discord.py version", value=discord.__version__, inline=True)
    embed.add_field(name="Commands", value=len(bot.commands), inline=True)
    embed.add_field(name="Bot owner", value="Joshek#1337", inline=True)
    embed.add_field(name="Ping", value=f"{int(ping)}ms", inline=True)
    await bot.say(embed=embed)

# about command
@bot.command(pass_context=True)
async def about(ctx):
    """Information about the bot."""
    embed = discord.Embed(description="Hello, My name is Arc and I'm here to make your Discord server better with great features.", color=0x176cd5)
    embed.set_author(name="Developed by Joshek#1337", url="https://joshek.xyz", icon_url="https://cdn.discordapp.com/avatars/372931332239654912/fee7f1717f9d2b3a1f5ce28c0369efdd.webp?size=1024")
    embed.set_thumbnail(url="https://joshek.xyz/arc/images/ArcProdLogo.png")
    embed.add_field(name="Support", value="[Join](https://discord.gg/cTMfa56)", inline=True)
    embed.add_field(name="Website", value="[Link](https://joshek.xyz/arc)", inline=True)
    await bot.say(embed=embed)

# donate commmand
@bot.command(pass_context=True)
async def donate(ctx):
    """Links to donate to the development."""
    embed=discord.Embed(title="Support the development!", description="Donate to our Patreon and get some perks, or if you can't, upvote us on DBL to get us recognized.", color=0x176cd5)
    embed.set_thumbnail(url="https://joshek.xyz/arc/images/ArcProdLogo.png")
    embed.add_field(name="Discord Bot List", value="https://discordbots.org/bot/417982648749654016/vote", inline=False)
    embed.add_field(name="Patreon", value="https://patreon.com/arcbot", inline=False)
    embed.set_footer(text="Or you can spread to word and get some servers to add me ??")
    await bot.say(embed=embed)

# ping command
@bot.command(pass_context=True)
async def ping(ctx):
    """Ping the bot."""
    ping = (time.monotonic()) / 10000
    embed = discord.Embed(title=f"Pong!  `{int(ping)}ms`", color=0x176cd5)
    embed.set_footer(text="The lower the number, the better the response time.")
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

# invite command
@bot.command(pass_context=True)
async def invite(ctx):
    """Invite link for the bot."""
    embed = discord.Embed(title="I've sent you a DM with the invite link.", color=0x176cd5)
    await bot.say(embed=embed)
    embed = discord.Embed(title="Invite Arc to your server.", url="https://discordapp.com/oauth2/authorize?client_id=417982648749654016&scope=bot&permissions=8", color=0x176cd5)
    embed.set_thumbnail(url="https://joshek.xyz/arc/images/ArcLogo.png")
    embed.set_footer(text="Add Arc to your server (requires manage server permissions)")
    await bot.send_message(ctx.message.author, embed=embed)

# support command
@bot.command(pass_context=True)
async def support(ctx):
    """Support server link."""
    embed = discord.Embed(title="I've sent you a DM with the support links.", color=0x176cd5)
    await bot.say(embed=embed)
    embed=discord.Embed(title="Support links.", color=0x176cd5)
    embed.add_field(name="Discord", value="https://discord.gg/cTMfa56", inline=False)
    embed.add_field(name="Commands", value="https://joshek.xyz/arc/commands", inline=False)
    embed.add_field(name="Trello", value="https://trello.com/b/W12CBdcP/arc", inline=False)
    embed.set_thumbnail(url="https://joshek.xyz/arc/images/ThinkingArc.png")
    await bot.send_message(ctx.message.author, embed=embed)

# Moderation commands.
# serverinfo command
@bot.command(pass_context=True)
async def serverinfo(ctx):
    """Displays server information."""
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), color=0x176cd5)
    embed.add_field(name="Server Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.add_field(name="Channels", value=len(ctx.message.server.channels))
    embed.add_field(name="Region", value=ctx.message.server.region)
    embed.add_field(name="Verification Level", value=ctx.message.server.verification_level)
    embed.add_field(name="Owner", value=ctx.message.server.owner.mention)
    embed.add_field(name="Emojis", value=len(ctx.message.server.emojis))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text="Server ID is " + ctx.message.server.id)
    await bot.say(embed=embed)

# userinfo command
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    """Displays user information."""
    if user is None:
        user = ctx.message.author
    embed = discord.Embed(title="{}'s info".format(user.mention), color=0x176cd5)
    embed.add_field(name="Username", value=user.name + "#" + user.discriminator, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Roles", value=len(user.roles))
    embed.add_field(name="Game", value=user.game)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.add_field(name="Created", value=user.created_at)
    embed.add_field(name="Bot?", value=user.bot)
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

# avatar command
@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
    """Displays users avatar."""
    if user is None:
        user = ctx.message.author
    embed = discord.Embed(color=0x176cd5)
    embed = discord.Embed(title="View full image.", url=user.avatar_url, color=0x176cd5)
    embed.set_image(url=user.avatar_url)
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text="Avatar of " + user)
    await bot.say(embed=embed)

# warn command
@bot.command(pass_context=True)
async def warn(ctx, member: discord.Member, *, note):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.kick_members or ctx.message.author.server_permissions.ban_members:
        embed=discord.Embed(title="You have recieved a warning.", description="You were warned in **{0}** by **{1}**. Moderator note is {2}.".format(ctx.message.server.name, ctx.message.author, note), color=0x176cd5)
        embed.set_thumbnail(url="https://images.emojiterra.com/twitter/512px/26a0.png")
        await bot.send_message(member, embed=embed)
        embed=discord.Embed(title="Warning issued", color=0x176cd5)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x176cd5)
        await bot.say(embed=embed)

# kick command
@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    """Kicks a user."""
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.kick_member:
        await bot.kick(user)
        embed = discord.Embed(title="User kicked!", description="**{}** has been kicked!".format(user), color=0x176cd5)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Responsible moderator - " + ctx.message.author)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x176cd5)
        await bot.say(embed=embed)

# ban command
@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    """Bans a user."""
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.kick_member:
        await bot.ban(user)
        embed = discord.Embed(title="User banned!", description="**{}** has been banned!".format(user), color=0x176cd5)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Responsible moderator - " + ctx.message.author)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x176cd5)
        await bot.say(embed=embed)

# purge command
@bot.command(pass_context=True)
async def purge(ctx, amount):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.manage_messages:
        await bot.purge_from(ctx.message.channel, limit=int("1"))
        await bot.purge_from(ctx.message.channel, limit=int(amount))
        embed=discord.Embed(title="Purged successfully!", description="Purged " + amount + " message(s).", color=0x176cd5)
        embed.set_footer(text="Responsible moderator - " + ctx.message.author)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x176cd5)
        await bot.say(embed=embed)

# mute command
@bot.command(pass_context=True)
async def mute(ctx, member: discord.Member):
    """Mutes a user (requires muted role)"""
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.manage_roles:
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed = discord.Embed(title="User muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0x176cd5)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Responsible moderator - " + ctx.message.author)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x176cd5)
        await bot.say(embed=embed)

# unmute command
@bot.command(pass_context=True)
async def unmute(ctx, member: discord.Member):
    """Unmutes a user."""
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.manage_roles:
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.remove_roles(member, role)
        embed = discord.Embed(title="User unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0x176cd5)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Responsible moderator - " + ctx.message.author)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x176cd5)
        await bot.say(embed=embed)

# addrole command
@bot.command(pass_context=True)
async def addrole(ctx, member: discord.Member, *, role):
    """Add a role to a user (case sensitive)"""
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.manage_roles:
        role = discord.utils.get(member.server.roles, name=role)
        await bot.add_roles(member, role)
        embed = discord.Embed(title="Role added", description="Role was added!".format(ctx.message.author, role, member), color=0x176cd5)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Responsible moderator - " + ctx.message.author)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x176cd5)
        await bot.say(embed=embed)

# removerole command
@bot.command(pass_context=True)
async def removerole(ctx, member: discord.Member, *, role):
    """Remove a role (case sensitive)"""
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.manage_roles:
        role = discord.utils.get(member.server.roles, name=role)
        await bot.remove_roles(member, role)
        embed = discord.Embed(title="Role removed", description="Role was removed!".format(ctx.message.author, role, member), color=0x176cd5)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Responsible moderator - " + ctx.message.author)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x176cd5)
        await bot.say(embed=embed)

# announcement command
@bot.command(pass_context=True)
async def announce(ctx, channel : discord.Channel, *, announcement):
    """Send an announcement with a channel mention and the message. Requires manage server."""
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.manage_server:
        embed = discord.Embed(title="Announcement!", description="New announcement from **{0}**".format(ctx.message.author), color=0x176cd5)
        embed.add_field(name="Message", value=announcement)
        await bot.send_message(bot.get_channel(channel.id), embed=embed)
        embed = embed.Discord(title="Announcement sent!")
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x176cd5)
        await bot.say(embed=embed)

# Fun commands

# slap command
@bot.command(pass_context=True)
async def slap(ctx, member: discord.Member):
    """Slap someone."""
    embed = discord.Embed(title="Wapow!", description="**{1}** slaps **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    embed.set_image(url="https://m.popkey.co/08a7fe/VelWq_s-200x150.gif")
    await bot.say(embed=embed)

# punch command
@bot.command(pass_context=True)
async def punch(ctx, member: discord.Member):
    """Punch someone."""
    embed = discord.Embed(title="Kapow!", description="**{1}** punches **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    embed.set_thumbnail(url="https://m.popkey.co/7bc81e/vzaX9_s-200x150.gif")
    await bot.say(embed=embed)

# shoot command
@bot.command(pass_context=True)
async def shoot(ctx, member: discord.Member):
    """Shoot someone."""
    embed = discord.Embed(title="Pow Pow Pow!", description="**{1}** shoots **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    embed.set_thumbnail(url="https://media.giphy.com/media/9umH7yTO8gLYY/giphy.gif")
    await bot.say(embed=embed)

# cookie command
@bot.command(pass_context=True)
async def cookie(ctx, member: discord.Member):
    """Give a cookie to someone."""
    embed = discord.Embed(title="Nom nom nom!", description="**{1}** gave a cookie to **{0}**! :cookie: ".format(member.name, ctx.message.author.name), color=0x176cd5)
    await bot.say(embed=embed)

# hug command
@bot.command(pass_context=True)
async def hug(ctx, member: discord.Member):
    """Hug someone."""
    embed = discord.Embed(title="Huggies!", description="**{1}** hugs **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    embed.set_thumbnail(url="https://media1.tenor.com/images/0be55a868e05bd369606f3684d95bf1e/tenor.gif?itemid=7939558")
    await bot.say(embed=embed)

# cat command
@bot.command(pass_context=True)
async def cat(ctx):
    embed = discord.Embed(title="Meow!", description=" ", color=0x176cd5)
    embed.set_image(url="http://thecatapi.com/api/images/get?format=src&type=png")
    await bot.say(embed=embed)

# duck command
@bot.command(pass_context=True)
async def duck(ctx):
    embed = discord.Embed(title="Quack!", description=" ", color=0x176cd5)
    embed.set_image(url="https://random-d.uk/api/v1/randomimg")
    await bot.say(embed=embed)

# Dice roll command
@bot.command(pass_context=True)
async def roll(self, dice : str):
    """Roll a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        embed=discord.Embed(title="Wrong layout.", description="Must be formatted in NdN format.", color=0x176cd5)
        await bot.say(embed=embed)
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    embed=discord.Embed(color=0x146aeb)
    embed.add_field(name="Result", value=result, inline=True)
    await bot.say(embed=embed)

# 8ball command
@bot.command(pass_context=True)
async def eightball(ctx, *, question):
    responses = ["That is a resounding no" , "It is not looking likely", "Too hard to tell", "It is quite possible", "Definitely", "Reply hazy, try again"]
    embed=discord.Embed(title="The magic 8 ball has spoken.", color=0x176cd5)
    embed.add_field(name="Question", value=question, inline=True)
    embed.add_field(name="Answer", value=random.choice(responses), inline=True)
    await bot.say(embed=embed)

# wherewedroppin command
@bot.command(pass_context=True)
async def wherewedroppin(ctx):
    locations = ["Dusty Divot", "Tilted Towers", "Fatal Fields", "Wailing Woods", "Anarchy Acres", "Tomato Town", "Retail Row", "Moisty Mire", "Flush Factory", "Shifty Shafts", "Snobby Shores", "Greasy Grove", "Salty Springs", "Junk Junction", "Loot Lake", "Haunted Hills", "Wailing Woods", "The ocean", "The lobby"]
    embed=discord.Embed(title="Where we droppin'?", color=0x761fa1)
    embed.add_field(name="Location", value=random.choice(locations), inline=False)
    embed.set_thumbnail(url="https://joshek.xyz/arc/images/Fortnite.jpg")
    await bot.say(embed=embed)

# Choose command
@bot.command(pass_context=True)
async def choose(ctx, *choices : str):
    embed=discord.Embed(title="I have made my choice.", description="I choose....", color=0x176cd5)
    embed.add_field(name="Options", value=choices, inline=True)
    embed.add_field(name="Choice", value=random.choice(choices), inline=True)
    await bot.say(embed=embed)

# speak command
@bot.command(pass_context=True)
async def speak(ctx, *, message):
    embed=discord.Embed(description=message)
    embed.set_author(name="Message by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

# steam game news command
@bot.command(pass_context=True)
async def gamenews(self, *, gameid):
    """Get the latest news for a game with a steam game ID."""
    embed=discord.Embed(title="Parsing Steam API... <a:loading:393852367751086090>")
    message = await bot.say(embed=embed)
    news = requests.get("http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?count=1&appid=" + str(gameid))
    news = news.json()
    news = news['appnews']['newsitems'][0]
    postingtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(news['date']))
    embed = discord.Embed(title="Game Latest News", description="Latest news post for game.", color=0x176cd5)
    embed.add_field(name="News Post Title", value=news['title'], inline=True)
    embed.add_field(name="News Post Content", value=news['contents'], inline=True)
    embed.set_footer(text="Posted On: " + postingtime)
    await bot.edit_message(message, embed=embed)

# json parse command
@bot.command(pass_context=True)
async def json(ctx, url):
    """Parse a JSON API and post the results."""
    embed=discord.Embed(title="Parsing requested API... <a:loading:393852367751086090>")
    embed.set_footer(text="This may take a while depending on the API load of the server your parsing.")
    message = await bot.say(embed=embed)
    url = url
    # Do the HTTP get request
    response = requests.get(url)
    # Decode the JSON response into a dictionary and use the data
    embed=discord.Embed(title="Response.", description="```" + str(response.json()) + "```", color=0x80ff80)
    embed.set_footer(text="If you encountered an unauthorised error, you may require auth on the API.")
    await bot.edit_message(message, embed=embed)

# fox command
@bot.command(pass_context=True)
async def fox(ctx):
    url = 'https://randomfox.ca/floof/' # api link
    response = response.json()
    embed=discord.Embed(title="Yip!", color=0x176cd5)
    embed.set_image(url=response["image"])
    await bot.say(embed=embed)

# weather command
@bot.command(pass_context=True)
async def weather(ctx, *, loc):
    """Fetch the current weather of a town."""
    await bot.say("https://wttr.in/{0}.png?m".format(ctx.message.server.name))

# hex command
@bot.command(pass_context=True)
async def hex(ctx):
    """Generates a random hex"""
    r = lambda: random.randint(0,255)
    hex = "#%02X%02X%02X" % (r(),r(),r())
    embed=discord.Embed(title="Random hex", color=hex)
    embed.add_field(name="Hex code", value=hex)
    await bot.say(embed=embed)
    
# RATELIMITED.ME commands

# token bump command
@commands.check(rlcheck)
@bot.command(pass_context=True)
async def tokenbump(ctx):
    embed=discord.Embed(title="Your token request was bumped!")
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text="Thank you for waiting in the RATELIMITED.ME Air departure lounge.")
    await bot.say(embed=embed)
    # send to bump channel
    embed=discord.Embed(title="New token bump!", description="An outstanding token request has been bumped.")
    embed.add_field(name="Username", value=ctx.message.author.mention, inline=False)
    embed.add_field(name="ID", value=ctx.message.author.id, inline=False)
    embed.add_field(name="Date of bump", value=datetime.datetime.today(), inline=False)
    server = bot.get_server("363508876164726795")
    await bot.send_message(bot.get_channel("419238803656409100"), embed=embed)

# role bump command
@commands.check(rlcheck)
@bot.command(pass_context=True)
async def rolebump(ctx):
    embed=discord.Embed(title="Your has token role request was bumped!")
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text="Thank you for waiting in the RATELIMITED.ME Air departure lounge.")
    await bot.say(embed=embed)
    # send to bump channel
    embed=discord.Embed(title="New role bump!", description="An outstanding has token has been bumped.")
    embed.add_field(name="Username", value=ctx.message.author.mention, inline=False)
    embed.add_field(name="Date of bump", value=datetime.datetime.today(), inline=False)
    server = bot.get_server("363508876164726795")
    await bot.send_message(bot.get_channel("419238803656409100"), embed=embed)

# Owner only commands
# say command
@commands.check(ownercheck)
@bot.command(pass_context=True, hidden=True)
async def say(ctx, *, arg):
        await bot.say(arg)

# embedsay command
@commands.check(ownercheck)
@bot.command(pass_context=True, hidden=True)
async def embedsay(ctx, title, *, desc):
        embed = discord.Embed(title=title, description=desc, color=0x176cd5)
        await bot.say(embed=embed)

# status command
@commands.check(ownercheck)
@bot.command(pass_context=True, hidden=True)
async def status(ctx, *, status):
        await bot.change_presence(game=discord.Game(name=status))
        embed=discord.Embed(title="Updated status.", description="Status has been modified.", color=0x176cd5)
        embed.add_field(name="Current setting", value=status)
        await bot.say(embed=embed)

# refresh command
@commands.check(ownercheck)
@bot.command(pass_context=True)
async def refresh(ctx):
    payload = {"server_count"  : len(bot.servers)}
    requests.post(url, data=payload, headers=headers)
    await bot.change_presence(game=discord.Game(name="arc!help | {} servers and {} users | joshek.xyz/arc".format(len(bot.servers), len(set(bot.get_all_members()))), type=3))
    embed=discord.Embed(title="Done.", description="Updated stats count for dbl and bot!", color=0x176cd5)
    embed.add_field(name="guilds", value=len(bot.servers))
    await bot.say(embed=embed)

# debug command
@commands.check(ownercheck)
@bot.command(pass_context=True)
async def debug(ctx, *, code):
    """Evaluate code"""

    global_vars = globals().copy()
    global_vars['bot'] = bot
    global_vars['ctx'] = ctx
    global_vars['message'] = ctx.message
    global_vars['author'] = ctx.message.author
    global_vars['channel'] = ctx.message.channel
    global_vars['server'] = ctx.message.server

    try:
        result = eval(code, global_vars, locals())
        if asyncio.iscoroutine(result):
            result = await result
        result = str(result) # the eval output was modified by me but originally submitted by DJ electro
        embed=discord.Embed(title="<:success:442552796303196162> Evaluated successfully.", color=0x80ff80)
        embed.add_field(name="Input :inbox_tray:", value="```" + code + "```")
        embed.add_field(name="Output :outbox_tray:", value="```" + result + "```")
        await bot.say(embed=embed)
    except Exception as error:
        embed=discord.Embed(title="<:error:442552796420767754> Evaluation failed.", color=0xff0000)
        embed.add_field(name="Input :inbox_tray:", value="```" + code + "```", inline=True)
        embed.add_field(name="Error <:error2:442590069082161163>", value='```{}: {}```'.format(type(error).__name__, str(error)))
        await bot.say(embed=embed)
        return

# Shutdown command
@commands.check(ownercheck)
@bot.command(pass_context=True)
async def shutdown(ctx):
    embed=discord.Embed(title="Shutting down...", color=0xff8080)
    print("Shutdown was issued, closing bot process and killing API connection")
    await bot.say(embed=embed)
    await bot.logout() # ends connection to api and closes bot.py

# restart command
@commands.check(ownercheck)
@bot.command(pass_context=True)
async def restart(ctx):
    embed=discord.Embed(title="Restarting...", color=0xff8080)
    await bot.say(embed=embed)
    print("Restart was issued, executing process and closing API connection")
    await bot.logout()
    subprocess.call([sys.executable, "bot.py"])

# cross server chat command
@commands.check(ownercheck)
@bot.command(pass_context=True)
async def relay(ctx, server, channel, *, message):
    embed=discord.Embed(title="Sent message!", color=0x176cd5)
    await bot.say(embed=embed)
    embed=discord.Embed(title="Relayed message.", description=message, color=0x176cd5)
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    server = bot.get_server(server)
    await bot.send_message(bot.get_channel(channel), embed=embed)

# traceback command
@commands.check(ownercheck)
@bot.command(pass_context=True)
async def traceback(ctx):
    embed=discord.Embed(title="Sending traceback via DMs.", color=0x176cd5)
    await bot.say(embed=embed)
    await bot.send_file(ctx.message.author, 'discord.log')

# permcheck command
@commands.check(ownercheck)
@bot.command(pass_context=True)
async def permcheck(ctx):
    embed=discord.Embed(title="Permissions checker", description="Checks the bot permissions to debug any possible issues.")
    embed.add_field(name="Administrator", value=ctx.message.author.server_permissions.administrator, inline=False)
    embed.add_field(name="Manage server", value=ctx.message.author.server_permissions.manage_server, inline=False)
    embed.add_field(name="Manage roles", value=ctx.message.author.server_permissions.manage_roles, inline=False)
    embed.add_field(name="Kick members", value=ctx.message.author.server_permissions.kick_members, inline=False)
    embed.add_field(name="Ban members", value=ctx.message.author.server_permissions.ban_members, inline=False)
    embed.add_field(name="Manage channels", value=ctx.message.author.server_permissions.manage_channels, inline=False)
    embed.add_field(name="Send messages", value=ctx.message.author.server_permissions.send_messages, inline=False)
    embed.add_field(name="Manage messages", value=ctx.message.author.server_permissions.manage_messages, inline=False)
    embed.set_footer(text="True means yes, false means no.")
    await bot.say(embed=embed)

# load
@commands.check(ownercheck)
@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

# unload
@commands.check(ownercheck)
@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

# error handling, responses and more error stuff
@bot.event
async def on_command_error(event, ctx):
    if isinstance(event, commands.CheckFailure): 
        embed=discord.Embed(title="An error has occured.", description="Whoops! An error has occured and I can't run the command you wanted to run, the most common causes of this are", color=0xffff00)
        embed.set_thumbnail(url="https://emojipedia-us.s3.amazonaws.com/thumbs/120/apple/129/warning-sign_26a0.png")
        embed.add_field(name="Invalid permissions", value="You may of tried to run a moderator command without permissions.", inline=False)
        embed.add_field(name="Invalid permissions <:botTag:230105988211015680>", value="The bot may not be able to do this action.", inline=False)
        embed.add_field(name="Owner only command", value="The command could just be reserved for the developer.", inline=False)
        await bot.send_message(ctx.message.channel, embed=embed)

    # Missing subcommand traceback
    if isinstance(event, commands.MissingRequiredArgument):
        await send_cmd_help(ctx) # send default subcommand embed

# Error logging to file
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# command execution logging
@bot.event
async def on_command(command, ctx):
    embed = discord.Embed(title="Command ran!", color=0x176cd5)
    embed.add_field(name="Command author", value=str(ctx.message.author), inline=True)
    embed.add_field(name="Command ran", value=str(ctx.message.content), inline=True)
    embed.add_field(name="Server", value=str(ctx.message.server.name), inline=True)
    embed.add_field(name="Server ID", value=str(ctx.message.server.id), inline=True)
    embed.add_field(name="Channel ID", value=str(ctx.message.channel.id), inline=True)
    embed.add_field(name="Author ID", value=str(ctx.message.author.id), inline=True)
    server = bot.get_server("438316852347666432")
    await bot.send_message(bot.get_channel("452998136793923585"), embed=embed)

bot.run(token)
