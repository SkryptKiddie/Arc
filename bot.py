import discord # Arc by Joshek#1024
import asyncio # Written in Discord.py asyncio because I can't be arsed to learn rewrite
import aiohttp # Embeds were generated using https://cog-creators.github.io/discord-embed-sandbox/
import traceback # Open source but it's mainly mine.
import sys # Support server invite is https://discord.gg/smHzBYD
import json # This code comes with no warrenty or support because you shouldn't be hosting it
import random # stackoverflow is so helpful lmao
import datetime # Thank you DJ Electro#8950 for debug, ownercheck and error handling.
import time # Now with added music playback! but the bot file is now longer
import requests # tinydb is a pain lol
import os
import subprocess
from tinydb import TinyDB, Query
from discord.ext import commands
from discord.ext.commands import Bot  

startup_extensions = ["cogs.music", "cogs.owner", "cogs.mod"]
testdb = TinyDB('databases/testdb.json') # testing database
moddb = TinyDB('databases/moddb.json') # the database for moderation
User = Query()

# Configuration and settings
token = ""
dbltoken = ""
prefix = "arc!"
owner = ""
centeralserver = ""
cmdlog = ""
serverlog = ""
errorlog = ""

# Startup 
dblurl = "https://discordbots.org/api/bots/417982648749654016/stats"
headers = {"Authorization" : dbltoken} # define the auth for dbl stats
bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix), case_insensitive=True)
bot.remove_command('help') # remove default help command
startup = open("arc.txt") # arc.txt is required for the ASCII logo to display but is not required.
print(startup.read()) # just remove these lines if you don't want it.
print(str(datetime.datetime.now().time()) + " - Connecting to Discord API...")

# Successful API connection.
@bot.event
async def on_ready():
    ping = (time.monotonic()) / 10000
    print(str(datetime.datetime.now().time()) + " - Connected to Discord API.")
    print(str(datetime.datetime.now().time()) + " - Loading stats and posting to DBL...")
    payload = {"server_count"  : len(bot.servers)} # prep headers for dbl stats
    requests.post(dblurl, data=payload, headers=headers) # send bot stats
    await bot.change_presence(game=discord.Game(name="arc!help | {} servers and {} users | joshek.pw/arc".format(len(bot.servers), len(set(bot.get_all_members()))), type=3))
    print(str(datetime.datetime.now().time()) + " - Loading complete!")
    # startup channel log
    print(str(datetime.datetime.now().time()) + " - Primed and set.")
    print(str(datetime.datetime.now().time()) + " - {0} guilds".format(len(bot.servers)))

# Specify bot owners ID for owner-only commands.
def ownercheck(ctx):
    return ctx.message.author.id == owner
def botcheck(ctx):
    return ctx.message.author.bot == False

# General Commands.
@bot.event
async def when_mentioned(ctx):
    embed=discord.Embed(title="Hi, I'm Arc", description="My default prefix is `arc!` or a mention. Hope this helps!", color=0x176cd5)
    await bot.send_message(ctx.message.channel, embed=embed)
# help command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def help(ctx):
    embed=discord.Embed(title="Here's your help", description="<:stafftools:314348604095594498> [Commands](https://gitlab.com/Joshek/discordarc/blob/master/commands.md) \n <:discord:314003252830011395> [Support server](https://discord.gg/cTMfa56) \n <:botTag:230105988211015680> [Website](https://joshek.pw/arc) \n 📲 [Invite](https://discordapp.com/oauth2/authorize?client_id=417982648749654016&scope=bot&permissions=8) \n <:staff:314068430787706880> [Joshek's website](https://joshek.pw) \n <:trello:468491326980096000> [Trello](https://trello.com/b/W12CBdcP/arc)", color=0x0080ff)
    embed.set_author(name="Requested by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

# about command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def about(ctx):
    """Information about the bot."""
    embed = discord.Embed(description="Hello, My name is Arc and I'm here to make your Discord server better with great features. \n <:stafftools:314348604095594498> **[Support server](https://discord.gg/cTMfa56)** \n <:botTag:230105988211015680> **[Website](https://joshek.pw/arc)** \n <:update:264184209617321984> **[GitLab](https://gitlab.com/Joshek/discordarc/)** \n <:trello:468491326980096000> **[Trello](https://trello.com/b/W12CBdcP/arc)** \n 📲 **[Invite](https://discordapp.com/oauth2/authorize?client_id=417982648749654016&scope=bot&permissions=8)**", color=0x176cd5)
    embed.set_author(name="Developed by Joshek#1024", url="https://joshek.pw", icon_url="https://cdn.discordapp.com/avatars/372931332239654912/fee7f1717f9d2b3a1f5ce28c0369efdd.webp?size=1024")
    embed.set_thumbnail(url="https://joshek.xyz/arc/images/ArcProdLogo.png")
    await bot.say(embed=embed)

# donate commmand
@commands.check(botcheck)
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
@commands.check(botcheck)
@bot.command(pass_context=True)
async def ping(ctx):
    """Ping the bot."""
    now = datetime.datetime.utcnow()
    delta = ctx.message.timestamp
    pingtime = now-delta
    embed = discord.Embed(title="Pong! {} ms".format(pingtime), color=0x176cd5)
    embed.set_author(name="Requested by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

# Moderation commands.
# serverinfo command
@commands.check(botcheck)
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
    embed.set_author(name=ctx.message.server.name, icon_url=ctx.message.server.icon_url)
    embed.set_footer(text="Server ID is " + ctx.message.server.id)
    await bot.say(embed=embed)

# userinfo command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member=None):
    """Displays user information."""
    if not user: # this command took forever to redo for the no user lol
        embed = discord.Embed(title="Your info.", color=0x176cd5)
        embed.add_field(name="Username", value=ctx.message.author.name + "#" + ctx.message.author.discriminator, inline=True)
        embed.add_field(name="ID", value=ctx.message.author.id, inline=True)
        embed.add_field(name="Status", value=ctx.message.author.status, inline=True)
        embed.add_field(name="Highest role", value=ctx.message.author.top_role)
        embed.add_field(name="Roles", value=len(ctx.message.author.roles))
        embed.add_field(name="Game", value=ctx.message.author.game)
        embed.add_field(name="Joined", value=ctx.message.author.joined_at)
        embed.add_field(name="Created", value=ctx.message.author.created_at)
        embed.add_field(name="Bot?", value=ctx.message.author.bot)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="{}'s info".format(user), color=0x176cd5)
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
@commands.check(botcheck)
@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member=None):
    """Displays users avatar."""
    if not user:
        embed = discord.Embed(color=0x176cd5)
        embed = discord.Embed(title="View full image.", url=ctx.message.author.avatar_url, color=0x176cd5)
        embed.set_image(url=ctx.message.author.avatar_url)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(color=0x176cd5)
        embed = discord.Embed(title="View full image.", url=user.avatar_url, color=0x176cd5)
        embed.set_image(url=user.avatar_url)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)


# warn command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def warn(ctx, member: discord.Member, *, note : str = None):
    """Warn a specified user"""
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.kick_members or ctx.message.author.server_permissions.ban_members:
        embed=discord.Embed(title="You have recieved a warning.", description="You were warned in **{0}** by **{1}**. Moderator note is {2}.".format(ctx.message.server.name, ctx.message.author, note), color=0x176cd5)
        embed.set_thumbnail(url="https://images.emojiterra.com/twitter/512px/26a0.png")
        await bot.send_message(member, embed=embed)
        embed=discord.Embed(title="Warning issued", color=0x176cd5)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x176cd5)
        await bot.say(embed=embed)

# nick command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def nick(ctx, user: discord.Member, *, nickname):
    """Changes the nickname of a user."""
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.manage_nicknames:
        await bot.change_nickname(user, nickname)
        embed = discord.Embed(title="User nicknamed!", description="**{0}**'s nickname was changed to **{1}**!".format(user, nickname), color=0x176cd5)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Responsible moderator - " + str(ctx.message.author))
        await bot.say(embed=embed)
        moddb.insert({'server': ctx.message.server.id, 'user_id': user.id, 'type': 'nick'})
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x176cd5)
        await bot.say(embed=embed)

# kick command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    """Kicks a user."""
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.kick_member:
        await bot.kick(user)
        embed = discord.Embed(title="User kicked!", description="**{}** has been kicked!".format(user), color=0x176cd5)
        embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
        moddb.insert({'server': ctx.message.server.id, 'user_id': user.id, 'type': 'kick'})
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x176cd5)
        await bot.say(embed=embed)

# purge command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def purge(ctx, amount):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.manage_messages:
        await bot.purge_from(ctx.message.channel, limit=int("1"))
        await bot.purge_from(ctx.message.channel, limit=int(amount))
        embed=discord.Embed(title="Purged successfully!", description="Purged " + amount + " message(s).", color=0x176cd5)
        embed.set_footer(text="Responsible moderator - " + str(ctx.message.author))
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x176cd5)
        await bot.say(embed=embed)

# addrole command
@commands.check(botcheck)
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
@commands.check(botcheck)
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

# Fun commands

# slap command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def slap(ctx, member: discord.Member):
    """Slap someone."""
    embed = discord.Embed(title="Wapow!", description="**{1}** slaps **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    embed.set_image(url="https://m.popkey.co/08a7fe/VelWq_s-200x150.gif")
    await bot.say(embed=embed)

# punch command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def punch(ctx, member: discord.Member):
    """Punch someone."""
    embed = discord.Embed(title="Kapow!", description="**{1}** punches **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    embed.set_thumbnail(url="https://m.popkey.co/7bc81e/vzaX9_s-200x150.gif")
    await bot.say(embed=embed)

# shoot command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def shoot(ctx, member: discord.Member):
    """Shoot someone."""
    embed = discord.Embed(title="Pow Pow Pow!", description="**{1}** shoots **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    embed.set_thumbnail(url="https://media.giphy.com/media/9umH7yTO8gLYY/giphy.gif")
    await bot.say(embed=embed)

# cookie command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def cookie(ctx, member: discord.Member):
    """Give a cookie to someone."""
    embed = discord.Embed(title="Nom nom nom!", description="**{1}** gave a cookie to **{0}**! :cookie:".format(member.name, ctx.message.author.name), color=0x176cd5)
    await bot.say(embed=embed)

# hug command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def hug(ctx, member: discord.Member):
    """Hug someone."""
    embed = discord.Embed(title="Huggies!", description="**{1}** hugs **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    embed.set_thumbnail(url="https://media1.tenor.com/images/0be55a868e05bd369606f3684d95bf1e/tenor.gif?itemid=7939558")
    await bot.say(embed=embed)

# cat command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def cat(ctx):
    embed = discord.Embed(title="Meow!", description=" ", color=0x176cd5)
    embed.set_image(url="http://thecatapi.com/api/images/get?format=src&type=png")
    await bot.say(embed=embed)

# duck command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def duck(ctx):
    embed = discord.Embed(title="Quack!", description=" ", color=0x176cd5)
    embed.set_image(url="https://random-d.uk/api/v1/randomimg")
    await bot.say(embed=embed)

# Dice roll command
@commands.check(botcheck)
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
@commands.check(botcheck)
@bot.command(pass_context=True, name='8ball', aliases=['eightball'])
async def _8ball(ctx, *, question):
    responses = ["That is a resounding no" , "It is not looking likely", "Too hard to tell", "It is quite possible", "Definitely", "Reply hazy, try again"]
    embed=discord.Embed(title="The magic 8 ball has spoken.", color=0x176cd5)
    embed.add_field(name="Question", value=question, inline=True)
    embed.add_field(name="Answer", value=random.choice(responses), inline=True)
    await bot.say(embed=embed)

# slots command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def slots(ctx):
    """Play a very basic version of slots."""
    responses = ["🍋" , "🍊", "🍉", ":seven:", ]
    embed=discord.Embed(title="🎰 Slot Machine 🎰", description=random.choice(responses) + random.choice(responses) + random.choice(responses), color=0x176cd5)
    embed.set_footer(text="You need triple 7's to win.")
    await bot.say(embed=embed)

# wherewedroppin command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def wherewedroppin(ctx):
    locations = ["Dusty Divot", "Tilted Towers", "Fatal Fields", "Wailing Woods", "Tomato Town", "Retail Row", "Moisty Mire", "Flush Factory", "Shifty Shafts", "Snobby Shores", "Greasy Grove", "Salty Springs", "Junk Junction", "Loot Lake", "Haunted Hills", "Wailing Woods", "The ocean", "The lobby", "Lazy Links"]
    embed=discord.Embed(title="Where we droppin'?", color=0x761fa1)
    embed.add_field(name="Location", value=random.choice(locations), inline=False)
    await bot.say(embed=embed)

# Choose command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def choose(ctx, *choices : str):
    embed=discord.Embed(title="I have made my choice.", description="I choose....", color=0x176cd5)
    embed.add_field(name="Options", value=choices, inline=True)
    embed.add_field(name="Choice", value=random.choice(choices), inline=True)
    await bot.say(embed=embed)

# speak command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def speak(ctx, *, message):
    embed=discord.Embed(description=message)
    embed.set_author(name="Message by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)

# steam game news command
@commands.check(botcheck)
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
@commands.check(botcheck)
@bot.command(pass_context=True)
async def json(ctx, url):
    """Parse a JSON API and post the results."""
    embed=discord.Embed(title="Please wait... <a:loading:393852367751086090>")
    embed.set_footer(text="If it's stuck on this embed then you've messed up.")
    message = await bot.say(embed=embed)
    url = url
    # Do the HTTP get request
    response = requests.get(url)
    # Decode the JSON response into a dictionary and use the data
    embed=discord.Embed(title="Response.", description="```" + str(response.json()) + "```", color=0x80ff80)
    await bot.edit_message(message, embed=embed)

# fox command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def fox(ctx):
    url = 'https://randomfox.ca/floof/' # api link
    response = response.json()
    embed=discord.Embed(title="Yip!", color=0x176cd5)
    embed.set_image(url=response["image"])
    await bot.say(embed=embed)

# weather command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def weather(ctx, *, loc):
    """Fetch the current weather of a town."""
    await bot.say("https://wttr.in/{0}.png?m".format(loc))

# dbl command
@commands.check(botcheck)
@bot.command(pass_context=True)
async def dbl(ctx, *, botid):
    """Show the stat image for a bot on Discord Bot List."""
    embed=discord.Embed(title="Here ya go", color=0x7289DA)
    embed.set_image(url="https://discordbots.org/api/widget/{0}.svg".format(botid))
    await bot.say(embed=embed)

# Owner only commands
# eval command
@commands.check(ownercheck)
@bot.command(pass_context=True, name='eval', aliases=['debug'])
async def _eval(ctx, *, code):
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
        embed.add_field(name="**Input** :inbox_tray:", value="```" + code + "```")
        embed.add_field(name="**Output** :outbox_tray:", value="```" + result + "```")
        await bot.say(embed=embed)
    except Exception as error:
        embed=discord.Embed(title="<:error:442552796420767754> Evaluation failed.", color=0xff0000)
        embed.add_field(name="Input :inbox_tray:", value="```" + code + "```", inline=True)
        embed.add_field(name="Error <:error2:442590069082161163>", value='```{}: {}```'.format(type(error).__name__, str(error)))
        await bot.say(embed=embed)
        return

@commands.check(ownercheck)
@bot.command(pass_context=True)
async def load(ctx, extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("<:bfdyes:414604312296030208> `{}` loaded.".format(extension_name))

@commands.check(ownercheck)
@bot.command(pass_context=True)
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("<:bfdyes:414604312296030208> `{}` unloaded.".format(extension_name))

@commands.check(ownercheck)
@bot.command(pass_context=True)
async def reload(ctx, extension_name : str):
    """Reloads an extension."""
    try:
        bot.unload_extension(extension_name)
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("<a:loading:473853564406595614> `{}` reloaded.".format(extension_name))

# error handling, responses and more error stuff
@bot.event
async def on_command_error(event, ctx):
    if isinstance(event, commands.CheckFailure): 
        embed=discord.Embed(title="Check error.", description="A check error occured")
        embed.add_field(name="Username", value=ctx.message.author)
        embed.add_field(name="Bot user?", value=ctx.message.author.bot)
        embed.add_field(name="Command", value=ctx.message.content)
        embed.add_field(name="Server", value=str(ctx.message.server.name), inline=True)
        server = bot.get_server(centeralserver)
        await bot.send_message(bot.get_channel(errorlog), embed=embed)

@bot.event
async def on_command_error(event, ctx):
    if isinstance(event, commands.CommandNotFound): 
        embed=discord.Embed(title="Command not found.")
        embed.add_field(name="Username", value=ctx.message.author)
        embed.add_field(name="Bot user?", value=ctx.message.author.bot)
        embed.add_field(name="Attempted command", value=ctx.message.content)
        embed.add_field(name="Server", value=str(ctx.message.server.name), inline=True)
        server = bot.get_server(centeralserver)
        await bot.send_message(bot.get_channel(errorlog), embed=embed)  

    # Missing subcommand traceback
    if isinstance(event, commands.MissingRequiredArgument):
        await send_cmd_help(ctx)

# Missing subcommand
async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        pages = bot.formatter.format_help_for(ctx, ctx.invoked_subcommand)
        for page in pages:
            embed=discord.Embed(title="Missing subcommand values", description=page, color=0x176cd5)
            await bot.send_message(ctx.message.channel, embed=embed)

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
    server = bot.get_server(centeralserver)
    await bot.send_message(bot.get_channel(cmdlog), embed=embed)

# find channel to send welcome message too
async def find_channel(server):
    for c in server.channels:
        if not c.permissions_for(server.me).send_messages:
            continue
        return c

# load cogs on startup
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

# server join and leave handler
@bot.event
async def on_server_join(server):
    channel = await find_channel(server)
    await bot.change_presence(game=discord.Game(name="arc!help | {} servers and {} users | joshek.pw/arc".format(len(bot.servers), len(set(bot.get_all_members()))), type=3))
    embed=discord.Embed(title="Joined a server", color=0x90EA69)
    embed.add_field(name="Guild count", value=len(bot.servers))
    embed.add_field(name="Server", value=server.name)
    embed.set_thumbnail(url=server.icon_url)
    embed.add_field(name="Server member count", value=len(server.members))
    embed.add_field(name="Server ID", value=server.id)
    server = bot.get_server(centeralserver)
    await bot.send_message(bot.get_channel(serverlog), embed=embed)
    payload = {"server_count"  : len(bot.servers)}
    requests.post(dblurl, data=payload, headers=headers)
    print(str(datetime.datetime.now().time()) + " - {0} guilds".format(len(bot.servers)))

@bot.event
async def on_server_remove(server):
    embed=discord.Embed(title="Removed from a server", color=0xEA6969)
    embed.add_field(name="Guild count", value=len(bot.servers))
    embed.add_field(name="Server", value=server.name)
    server = bot.get_server(centeralserver)
    await bot.send_message(bot.get_channel(serverlog), embed=embed)
    await bot.change_presence(game=discord.Game(name="arc!help | {} servers and {} users | joshek.pw/arc".format(len(bot.servers), len(set(bot.get_all_members()))), type=3))
    payload = {"server_count"  : len(bot.servers)}
    requests.post(dblurl, data=payload, headers=headers)
    print(str(datetime.datetime.now().time()) + " - {0} guilds".format(len(bot.servers)))

bot.run(token)
