# Arc by Joshek
# Written in Discord.py
# Huge thanks to DJ Electro#8890 for eval, sub_command_not_found, playing status and fixing up stuff

import discord
import asyncio
import time
import logging
import random
import aiohttp
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import find
import traceback
import sys

bot = commands.Bot(command_prefix='arc!')
bot.remove_command('help')
print("Arc v3.0")
print("Connecting to API...")


@bot.event
async def on_ready():
    print("Arc is online.")
    await bot.change_presence(game=discord.Game(name='Starting...'))
    await asyncio.sleep(5)
    await bot.change_presence(game=discord.Game(name="arc!about | {} users and {} servers!".format(
        len(set(bot.get_all_members())), len(bot.servers)), type=1))

def ownercheck(ctx):
    return ctx.message.author.id == "372931332239654912"

# help command
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title=" ", description="Here are the commands for Arc.", color=0x146aeb)
    embed.set_author(name="Help.")
    embed.set_thumbnail(url="https://joshek.xyz/arc/arc.png")
    embed.add_field(name="help", value="Displays this message.", inline=False)
    embed.add_field(name="about", value="Show's information.", inline=False)
    embed.add_field(name="donate", value="Donate to the development.", inline=False)
    embed.add_field(name="ping", value="Test response time.", inline=False)
    embed.add_field(name="invite", value="Invite the bot to your server.", inline=False)
    embed.add_field(name="serverinfo", value="Displays server details.", inline=False)
    embed.add_field(name="userinfo", value="Displays user details.", inline=False)
    embed.add_field(name="avatar", value="Shows a users avatar.", inline=False)
    embed.add_field(name="mute", value="Mute a user.", inline=False)
    embed.add_field(name="unmute", value="Unmute a user.", inline=False)
    embed.add_field(name="slap", value="Slap a user.", inline=False)
    embed.add_field(name="punch", value="Punch a user.", inline=False)
    embed.add_field(name="hug", value="Hug a user.", inline=False)
    embed.set_footer(text="There are some hidden commands too")
    await bot.say(embed=embed)


# about command
@bot.command(pass_context=True)
async def about(ctx):
    """Information about the bot."""
    embed = discord.Embed(title="About Arc.",
    description="Hello there :wave:, Iâ€™m Arc. Iâ€™m here to make your Discord server better with utilitarian features and moderation. Here are some links to where you can find out more about me!",
    color=0x146aeb)
    embed.set_thumbnail(url="https://joshek.xyz/arc/arc.png")
    embed.add_field(name="Support", value="https://discord.gg/cTMfa56", inline=True)
    embed.add_field(name="Website", value="https://joshek.xyz/arc", inline=True)
    embed.add_field(name="Patreon", value="https://www.patreon.com/arcbot", inline=True)
    embed.set_footer(text="Written by Joshek#1337 in Discord.py")
    await bot.say(embed=embed)


# donate commmand
@bot.command(pass_context=True)
async def donate(ctx):
    """Links to donate to the development."""
    embed = discord.Embed(title="Donate to my Patreon.", url="https://www.patreon.com/arcbot",
                          description="Help support the development of Arc.", color=0x146aeb)
    embed.set_thumbnail(url="https://joshek.xyz/arc/arc.png")
    embed.set_author(name="Donate.")
    embed.set_footer(text="I'll always host Arc, but donations help me.")
    await bot.say(embed=embed)


# ping command
@bot.command(pass_context=True)
async def ping(ctx):
    """Ping the bot."""
    embed = discord.Embed(title="Pong!", color=0x8080ff)
    embed.set_thumbnail(url="https://images.emojiterra.com/twitter/512px/1f3d3.png")
    embed.set_footer(text="Response timer coming soon.")
    await bot.say(embed=embed)


# invite command
@bot.command(pass_context=True)
async def invite(ctx):
    """Invite link for the bot."""
    embed = discord.Embed(title="Invite Arc to your server.",
                          url="https://discordapp.com/oauth2/authorize?client_id=417982648749654016&scope=bot&permissions=8",
                          color=0x146aeb)
    embed.set_footer(text="Add Arc to your server (requires manage server permissions)")
    await bot.say(embed=embed)


# serverinfo command
@bot.command(pass_context=True)
async def serverinfo(ctx):
    """Displays server information."""
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), color=0x146aeb)
    embed.add_field(name="Server Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Server ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.add_field(name="Channels", value=len(ctx.message.server.channels))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)


# userinfo command
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    """Displays user information."""
    embed = discord.Embed(title="{}'s info".format(user.name), color=0x146aeb)
    embed.add_field(name="Username", value=user.name + "#" + user.discriminator, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.add_field(name="Game", value=user.game)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)


# avatar command
@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
    """Displays users avatar."""
    embed = discord.Embed(title=user.avatar_url, color=0x146aeb)
    embed.set_author(name="Here is the users avatar.")
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)


# kick command
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True, kick_members=True)
async def kick(ctx, user: discord.Member):
    """Kicks a user."""
    embed = discord.Embed(title="User kicked!", description="User has been kicked from the server.", color=0x146aeb)
    await bot.say(embed=embed)
    await bot.kick(user)


# ban command
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True, ban_members=True)
async def ban(ctx, user: discord.Member):
    """Bans a user."""
    embed = discord.Embed(title="User banned!", description="User has been banned from the server.", color=0x146aeb)
    await bot.say(embed=embed)
    await bot.ban(user)


# mute command
@bot.command(pass_context=True)
async def mute(ctx, member: discord.Member):
    """Mutes a user (requires muted role)"""
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.manage_roles:
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed = discord.Embed(title="User Muted!",
                              description="**{0}** was muted by **{1}**!".format(member, ctx.message.author),
                              color=0x146aeb)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.",
                              color=0x146aeb)
        await bot.say(embed=embed)


# unmute command
@bot.command(pass_context=True)
async def unmute(ctx, member: discord.Member):
    """Unmutes a user."""
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.manage_roles:
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.remove_roles(member, role)
        embed = discord.Embed(title="User Unmuted!",
                              description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author),
                              color=0x146aeb)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.",
                              color=0x146aeb)
        await bot.say(embed=embed)


# slap command
@bot.command(pass_context=True)
async def slap(ctx, member: discord.Member):
    """Hug someone."""
    embed = discord.Embed(title="Wapow!", description="**{1}** slaps **{0}**!".format(member, ctx.message.author),
                          color=0x146aeb)
    embed.set_thumbnail(url="https://media.giphy.com/media/t1CsJ1o1sdOHm/giphy.gif")
    await bot.say(embed=embed)


# punch command
@bot.command(pass_context=True)
async def punch(ctx, member: discord.Member):
    """Punch someone."""
    embed = discord.Embed(title="Kapow!", description="**{1}** punches **{0}**!".format(member, ctx.message.author),
                          color=0x146aeb)
    embed.set_thumbnail(url="https://m.popkey.co/7bc81e/vzaX9_s-200x150.gif")
    await bot.say(embed=embed)


# shoot command
@bot.command(pass_context=True)
async def shoot(ctx, member: discord.Member):
    """Slap someone."""
    embed = discord.Embed(title="Pow Pow Pow!",
                          description="**{1}** shoots **{0}**!".format(member, ctx.message.author), color=0x146aeb)
    embed.set_thumbnail(url="https://media.giphy.com/media/9umH7yTO8gLYY/giphy.gif")
    await bot.say(embed=embed)


# hug command
@bot.command(pass_context=True)
async def hug(ctx, member: discord.Member):
    """Slap someone."""
    embed = discord.Embed(title="Huggies!", description="**{1}** hugs **{0}**!".format(member, ctx.message.author),
                          color=0x146aeb)
    embed.set_thumbnail(url="https://media1.tenor.com/images/0be55a868e05bd369606f3684d95bf1e/tenor.gif?itemid=7939558")
    await bot.say(embed=embed)

# backend and internal stuff, also owner commands

# say command
@bot.command(pass_context=True, hidden=True)
async def say(ctx, arg):
    if ctx.message.author.id == '372931332239654912':
        await bot.say(arg)
    else:
        print("User attempted to run say")
        embed = discord.Embed(title="Permission denied!", description="Command is owner-only to prevent abuse.",
                              color=0xff0000)
        await bot.say(embed=embed)

# embedsay command
@bot.command(pass_context=True, hidden=True)
async def embedsay(ctx, title, desc):
    if ctx.message.author.id == '372931332239654912':
        embed = discord.Embed(title=title, description=desc, color=0x00ff40)
        await bot.say(embed=embed)
    else:
        print("User attempted to run embedsay")
        embed = discord.Embed(title="Permission denied!", description="Command is owner-only to prevent abuse.",
                              color=0xff0000)
        await bot.say(embed=embed)


# status command
@bot.command(pass_context=True, hidden=True)
async def status(ctx, status):
    if ctx.message.author.id == '372931332239654912':
        await bot.change_presence(game=discord.Game(name=status))
        print("Status has been changed")
    else:
        print("User has attempted to change status")
        embed = discord.Embed(title="Permission denied!", description="Command is owner-only to prevent abuse.",
                              color=0xff0000)
        await bot.say(embed=embed)

# eval command (thanks DJ Electro#8890)
@commands.check(ownercheck)
@bot.command(pass_context=True)
async def debug(ctx, *, code):
    """Evaluate Code"""

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
        await bot.say("```" + result + "```")
    except Exception as error:
        await bot.say('```{}: {}```'.format(type(error).__name__, str(error)))
        return

@bot.event
async def on_command_error(event, ctx):
    if isinstance(event, commands.CheckFailure):
        embed = discord.Embed(title="Permission denied!", description="Command is owner-only to prevent abuse.",
                              color=0xff0000)
        await bot.say(embed=embed)
    if isinstance(event, commands.MissingRequiredArgument):
        await send_cmd_help(ctx)
    if isinstance(event, commands.CommandNotFound):
        pass
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(event), event, event.__traceback__, file=sys.stderr)


async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        pages = bot.formatter.format_help_for(ctx, ctx.invoked_subcommand)
        for page in pages:
            await bot.send_message(ctx.message.channel, page)
    else:
        pages = bot.formatter.format_help_for(ctx, ctx.command)
        for page in pages:
            await bot.send_message(ctx.message.channel, page)


# error logging
logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# this is where you insert your token
bot.run("Token goes here")
