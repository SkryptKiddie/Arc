import discord # Arc by Joshek#1337
import asyncio # Written in Discord.py asyncio because I can't be arsed to learn rewrite
import logging # Thank you DJ Electro#8950 for debug, ownercheck and error handling.
import aiohttp # Embeds were generated using https://cog-creators.github.io/discord-embed-sandbox/
import traceback
import sys
import json
import random
import datetime
import time
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import find

# Configuration and settings
bot = commands.Bot(command_prefix='arc!', case_insensitive=True)
bot.remove_command('help')
print("          _____                    _____                    _____          ")
print("         /\    \                  /\    \                  /\    \         ")
print("        /::\    \                /::\    \                /::\    \        ")
print("       /::::\    \              /::::\    \              /::::\    \       ")
print("      /::::::\    \            /::::::\    \            /::::::\    \      ")
print("     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     ")
print("    /:::/__\:::\    \        /:::/__\:::\    \        /:::/  \:::\    \    ")
print("   /::::\   \:::\    \      /::::\   \:::\    \      /:::/    \:::\    \   ")
print("  /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/    / \:::\    \  ")
print(" /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\  /:::/    /   \:::\    \ ")
print("/:::/  \:::\   \:::\____\/:::/  \:::\   \:::|    |/:::/____/     \:::\____\ ")
print("\::/    \:::\  /:::/    /\::/   |::::\  /:::|____|\:::\    \      \::/    /")
print(" \/____/ \:::\/:::/    /  \/____|:::::\/:::/    /  \:::\    \      \/____/ ")
print("          \::::::/    /         |:::::::::/    /    \:::\    \             ")
print("           \::::/    /          |::|\::::/    /      \:::\    \            ")
print("           /:::/    /           |::| \::/____/        \:::\    \           ")
print("          /:::/    /            |::|  ~|               \:::\    \          ")
print("         /:::/    /             |::|   |                \:::\    \         ")
print("        /:::/    /              \::|   |                 \:::\____\        ")
print("        \::/    /                \:|   |                  \::/    /        ")
print("         \/____/                  \|___|                   \/____/         ")
print("Arc.")
print("By Joshek#1337")
print("Connecting to Discord API...")

# Successful API connection.
@bot.event
async def on_ready():
    print("Connected to Discord API.")
    print("Loading status...")
    await bot.change_presence(game=discord.Game(name="arc!help | {} servers and {} users!".format(len(bot.servers), len(set(bot.get_all_members()))), type=3))
    print("Loading complete!")

# Specify bot owners ID for owner-only commands.
def ownercheck(ctx):
    return ctx.message.author.id == ""

# General Commands.
# help command
@bot.command(pass_context=True)
async def help(ctx):
    embed=discord.Embed(title="Help is on the way!", color=0x0080ff)
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)
    embed=discord.Embed(title="General.", color=0x176cd5)
    embed.set_author(name="Website.", url="https://joshek.xyz/arc/", icon_url="https://joshek.xyz/arc/images/ArcLogo.png")
    embed.add_field(name="about", value="Show's information.", inline=True)
    embed.add_field(name="stats", value="Show's technical details.", inline=True)
    embed.add_field(name="support", value="Invite to support server.", inline=True)
    embed.add_field(name="donate", value="Donate to the development.", inline=True)
    embed.add_field(name="ping", value="Pong!", inline=True)
    embed.add_field(name="invite", value="Invite the bot to your server.", inline=True)
    await bot.send_message(ctx.message.author, embed=embed)
    embed=discord.Embed(title="Moderation.", color=0xff8080)
    embed.add_field(name="serverinfo", value="Displays server details.", inline=True)
    embed.add_field(name="userinfo", value="Displays user details.", inline=True)
    embed.add_field(name="kick", value="Kick a user.", inline=True)
    embed.add_field(name="ban", value="Ban a user.", inline=True)
    embed.add_field(name="purge", value="Purge messages.", inline=True)
    embed.add_field(name="avatar", value="Shows a users avatar.", inline=True)
    embed.add_field(name="mute", value="Mute a user.", inline=True)
    embed.add_field(name="unmute", value="Unmute a user.", inline=True)
    embed.add_field(name="addrole", value="Add a role.", inline=True)
    embed.add_field(name="removerole", value="Remove a role.", inline=True)
    await bot.send_message(ctx.message.author, embed=embed)
    embed=discord.Embed(title="Fun.", color=0xffff80)
    embed.add_field(name="slap", value="Slap a user.", inline=True)
    embed.add_field(name="lick", value="Lick a user.", inline=True)
    embed.add_field(name="punch", value="Punch a user.", inline=True)
    embed.add_field(name="hug", value="Hug a user.", inline=True)
    embed.add_field(name="cat", value="Picture of a cat.", inline=True)
    embed.add_field(name="duck", value="Picture of a duck.", inline=True)
    embed.add_field(name="roll", value="Roll a dice in NdN format.", inline=True)
    await bot.send_message(ctx.message.author, embed=embed)

# stats command
@bot.command(pass_context=True)
async def stats(ctx):
    embed=discord.Embed(title="Technical details.", color=0x176cd5)
    embed.add_field(name="Guilds", value=len(bot.servers), inline=True)
    embed.add_field(name="Members", value=len(set(bot.get_all_members())), inline=True)
    embed.add_field(name="Channels", value=len(set(bot.get_all_channels())), inline=True)
    embed.add_field(name="Emojis", value=len(set(bot.get_all_emojis())), inline=True)
    embed.add_field(name="Discord.py release", value=discord.version_info, inline=True)
    embed.add_field(name="Discord.py version", value=discord.__version__, inline=True)
    embed.add_field(name="Bot owner", value="Joshek#1337", inline=True)
    await bot.say(embed=embed)

# about command
@bot.command(pass_context=True)
async def about(ctx):
    """Information about the bot."""
    embed = discord.Embed(title="About Arc.", description="Hello, My name is Arc and I'm here to make your Discord server better with great features.", color=0x176cd5)
    embed.set_author(name="Developed by Joshek#1337", url="https://joshek.xyz", icon_url="https://joshek.xyz/joshek.png")
    embed.set_thumbnail(url="https://joshek.xyz/arc/images/ArcLogo.png")
    embed.add_field(name="Support", value="https://discord.gg/cTMfa56", inline=True)
    embed.add_field(name="Website", value="https://joshek.xyz/arc", inline=True)
    embed.add_field(name="Donators", value="adam#0327 - $5", inline=False)
    await bot.say(embed=embed)

# donate commmand
@bot.command(pass_context=True)
async def donate(ctx):
    """Links to donate to the development."""
    embed = discord.Embed(title="Donate to the Patreon.", url="https://www.patreon.com/arcbot", description="Help support the development of Arc.", color=0x176cd5)
    embed.set_thumbnail(url="https://joshek.xyz/arc/arc.png")
    await bot.send_message(ctx.message.author, embed=embed)

# ping command
@bot.command(pass_context=True)
async def ping(ctx):
    """Ping the bot."""
    embed = discord.Embed(title="Pong!", color=0x176cd5)
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

# invite command
@bot.command(pass_context=True)
async def invite(ctx):
    """Invite link for the bot."""
    embed = discord.Embed(title="I've sent you a DM with the invite link.", color=0x176cd5)
    await bot.say(embed=embed)
    embed = discord.Embed(title="Invite Arc to your server.", url="https://discordapp.com/oauth2/authorize?client_id=417982648749654016&scope=bot&permissions=8", color=0x176cd5)
    embed.set_footer(text="Add Arc to your server (requires manage server permissions)")
    await bot.send_message(ctx.message.author, embed=embed)

# invite command
@bot.command(pass_context=True)
async def support(ctx):
    """Support server link."""
    embed = discord.Embed(title="I've sent you a DM with the support link.", color=0x176cd5)
    await bot.say(embed=embed)
    await bot.send_message(ctx.message.author, "https://discord.gg/cTMfa56")

# Moderation commands.
# serverinfo command
@bot.command(pass_context=True)
async def serverinfo(ctx):
    """Displays server information."""
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), color=0x176cd5)
    embed.add_field(name="Server Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Server ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.add_field(name="Channels", value=len(ctx.message.server.channels))
    embed.add_field(name="Region", value=ctx.message.server.region)
    embed.add_field(name="Verification Level", value=ctx.message.server.verification_level)
    embed.add_field(name="Owner", value=ctx.message.server.owner)
    embed.add_field(name="Emojis", value=len(ctx.message.server.emojis))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

# userinfo command
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    """Displays user information."""
    embed = discord.Embed(title="{}'s info".format(user.name), color=0x176cd5)
    embed.add_field(name="Username", value=user.name + "#" + user.discriminator, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Game", value=user.game)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.add_field(name="Created", value=user.created_at)
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

# avatar command
@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
    """Displays users avatar."""
    embed = discord.Embed(color=0x176cd5)
    embed.set_author(name="Here you go!")
    embed.set_image(url=user.avatar_url)
    embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

# kick command
@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    """Kicks a user."""
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.kick_member:
        await bot.kick(user)
        embed = discord.Embed(title="User kicked!", description="User has been kicked!", color=0x176cd5)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
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
        embed = discord.Embed(title="User banned!", description="User has been banned!", color=0x176cd5)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
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
        embed=discord.Embed(title="Purge complete!", description="Purged " + amount + " message(s).", color=0x176cd5)
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
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x176cd5)
        await bot.say(embed=embed)

# addrole command
@bot.command(pass_context=True)
async def addrole(ctx, member: discord.Member, role):
    """Add a role to a user (case sensitive)"""
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.manage_roles:
        role = discord.utils.get(member.server.roles, name=role)
        await bot.add_roles(member, role)
        embed = discord.Embed(title="Role added", description="**{0}** added **{1}** to **{2}**!".format(ctx.message.author, role, member), color=0x176cd5)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x176cd5)
        await bot.say(embed=embed)

# removerole command
@bot.command(pass_context=True)
async def removerole(ctx, member: discord.Member, role):
    """Remove a role (case sensitive)"""
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.manage_roles:
        role = discord.utils.get(member.server.roles, name=role)
        await bot.remove_roles(member, role)
        embed = discord.Embed(title="Role removed", description="**{0}** removed **{1}** from **{2}**!".format(ctx.message.author, role, member), color=0x176cd5)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x176cd5)
        await bot.say(embed=embed)

# Fun commands

# slap command
@bot.command(pass_context=True)
async def slap(ctx, member: discord.Member):
    """Slap someone."""
    embed = discord.Embed(title="Wapow!", description="**{1}** slaps **{0}**!".format(member, ctx.message.author), color=0x176cd5)
    embed.set_thumbnail(url="https://media.giphy.com/media/t1CsJ1o1sdOHm/giphy.gif")
    await bot.say(embed=embed)
    
# lick command
@bot.command(pass_context=True)
async def lick(ctx, member: discord.Member):
    """Lick someone."""
    embed = discord.Embed(title="Mmmmm.", description="**{1}** licks **{0}**!".format(member, ctx.message.author), color=0x176cd5)
    embed.set_thumbnail(url="https://media.giphy.com/media/oHIzafphZWPn2/giphy.gif")
    await bot.say(embed=embed)

# punch command
@bot.command(pass_context=True)
async def punch(ctx, member: discord.Member):
    """Punch someone."""
    embed = discord.Embed(title="Kapow!", description="**{1}** punches **{0}**!".format(member, ctx.message.author), color=0x176cd5)
    embed.set_thumbnail(url="https://m.popkey.co/7bc81e/vzaX9_s-200x150.gif")
    await bot.say(embed=embed)

# shoot command
@bot.command(pass_context=True)
async def shoot(ctx, member: discord.Member):
    """Shoot someone."""
    embed = discord.Embed(title="Pow Pow Pow!", description="**{1}** shoots **{0}**!".format(member, ctx.message.author), color=0x176cd5)
    embed.set_thumbnail(url="https://media.giphy.com/media/9umH7yTO8gLYY/giphy.gif")
    await bot.say(embed=embed)

# cookie command
@bot.command(pass_context=True)
async def cookie(ctx, member: discord.Member):
    """Give a cookie to someone."""
    embed = discord.Embed(title="Nom nom nom!", description="**{1}** gave a cookie to **{0}**! :cookie: ".format(member, ctx.message.author), color=0x176cd5)
    await bot.say(embed=embed)

# hug command
@bot.command(pass_context=True)
async def hug(ctx, member: discord.Member):
    """Hug someone."""
    embed = discord.Embed(title="Huggies!", description="**{1}** hugs **{0}**!".format(member, ctx.message.author), color=0x176cd5)
    embed.set_thumbnail(url="https://media1.tenor.com/images/0be55a868e05bd369606f3684d95bf1e/tenor.gif?itemid=7939558")
    await bot.say(embed=embed)

# cat command
@bot.command(pass_context=True)
async def cat(ctx):
    """Purrr."""
    embed = discord.Embed(title="Meow!", description=" ", color=0x146aeb)
    embed.set_image(url="http://thecatapi.com/api/images/get?format=src&type=png")
    await bot.say(embed=embed)

# duck command
@bot.command(pass_context=True)
async def duck(ctx):
    """Quack."""
    embed = discord.Embed(title="Quack!", description=" ", color=0x146aeb)
    embed.set_image(url="https://random-d.uk/api/v1/randomimg")
    await bot.say(embed=embed)

# Dice roll command
@bot.command(pass_context=True)
async def roll(self, dice : str):
    """Roll a dice."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        embed=discord.Embed(title="Wrong layout.", description="Must be formatted in NdN format.", color=0x146aeb)
        await bot.say(embed=embed)
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    embed=discord.Embed(color=0x146aeb)
    embed.add_field(name="Result", value=result, inline=True)
    await bot.say(embed=embed)

# Choose command
@bot.command(pass_context=True)
async def choose(ctx, *choices : str):
    await bot.say(random.choice(choices))

# Owner only commands and error handling
# say command
@commands.check(ownercheck)
@bot.command(pass_context=True, hidden=True)
async def say(ctx, arg):
        await bot.say(arg)

# embedsay command
@commands.check(ownercheck)
@bot.command(pass_context=True, hidden=True)
async def embedsay(ctx, title, desc):
        embed = discord.Embed(title=title, description=desc, color=0x176cd5)
        await bot.say(embed=embed)

# status command
@commands.check(ownercheck)
@bot.command(pass_context=True, hidden=True)
async def status(ctx, status):
        await bot.change_presence(game=discord.Game(name=status))
        embed=discord.Embed(title="Updated status.", description="Status has been modified.", color=0x176cd5)
        await bot.say(embed=embed)

# reloadstats command
@commands.check(ownercheck)
@bot.command(pass_context=True)
async def reloadstats(ctx):
    """Updates playing status with new stats."""
    await bot.change_presence(game=discord.Game(name="arc!help | {} servers and {} users!".format(len(bot.servers), len(set(bot.get_all_members()))), type=3))
    embed=discord.Embed(title="Done.", description="Updated playing status!", color=0x176cd5)
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
        result = str(result)
        embed=discord.Embed(title="Evaluation Output", description="```" + result + "```", color=0x80ff80)
        embed.set_thumbnail(url="https://joshek.xyz/arc/images/hackerman.png")
        await bot.say(embed=embed)
    except Exception as error:
        embed=discord.Embed(title="Evaluation error!", description='```{}: {}```'.format(type(error).__name__, str(error)), color=0xff0000)
        await bot.say(embed=embed)
        return

# Shutdown command
@commands.check(ownercheck)
@bot.command(pass_context=True)
async def shutdown(ctx, why):
    embed=discord.Embed(title="Shutting down...", description="Pending shutdown....", color=0xff8080)
    embed.add_field(name="Reason", value=why, inline=False)
    await bot.say(embed=embed)
    embed=discord.Embed(title="Shut down.", color=0xff8080)
    embed.add_field(name="Reason", value=why, inline=True)
    embed.add_field(name="By", value=ctx.message.author, inline=True)
    server = bot.get_server("438316852347666432")
    await bot.send_message(bot.get_channel("438352619988320296"), embed=embed)
    await bot.logout()

# traceback command
@commands.check(ownercheck)
@bot.command(pass_context=True)
async def traceback(ctx):
    embed=discord.Embed(title="Sending traceback via DMs.", color=0x176cd5)
    await bot.say(embed=embed)
    await bot.send_file(ctx.message.author, 'discord.log')

# Error response and traceback
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
        await send_cmd_help(ctx)

# Missing subcommand
async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        pages = bot.formatter.format_help_for(ctx, ctx.invoked_subcommand)
        for page in pages:
            await bot.send_message(ctx.message.channel, page)
    else:
        pages = bot.formatter.format_help_for(ctx, ctx.command)
        for page in pages:
            await bot.send_message(ctx.message.channel, page) 

# Error logging to file
logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot.run("")
