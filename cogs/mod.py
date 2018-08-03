import discord # mod cog for Arc
import asyncio
import aiohttp 
from discord.ext import commands
from discord.ext.commands import Bot
from tinydb import TinyDB, Query

moddb = TinyDB('/root/Arc/databases/moddb.json') # the database for moderation
User = Query()

def botcheck(ctx): # prevent bots from triggering the bot
    return ctx.message.author.bot == False

class Mod():
    def __init__(self, bot):
        self.bot = bot

    @commands.check(botcheck)
    @commands.command()
    async def ban(self, member: discord.Member):
        """Warn a specified user."""
        if ctx.message.author.server_permissions.administrator or ctx.message.author.server_permissions.ban_members:
            await self.bot.say("**{0}** was banned!".format(member))
            await self.bot.ban(member)
            moddb.insert({'server': ctx.message.server.id, 'user_id': member.id, 'type': 'strike'})
        else:
            await self.bot.say("<:bfdno:414604345770770432> Permission denied.")

def setup(bot):
    bot.add_cog(Mod(bot))