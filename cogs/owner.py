import discord # owner cog for Arc
import asyncio
import aiohttp 
import traceback
import sys
import requests
import os
import subprocess
from discord.ext import commands
from discord.ext.commands import Bot

owner = "372931332239654912"

def ownercheck(ctx):
    return ctx.message.author.id == owner

class Owner():
    def __init__(self, bot):
        self.bot = bot

    @commands.check(ownercheck)
    @commands.command()
    async def leaveguild(self, id):
        """Leave a guild."""
        toleave = self.bot.get_server(id)
        await self.bot.leave_server(toleave)
        await self.bot.say("<:bfdyes:414604312296030208> Left {0} (`{1}`)".format(toleave.name, toleave.id))

    @commands.check(ownercheck)
    @commands.command()
    async def shutdown(self):
        await self.bot.say("<:offline2:464520569929334784> Shutting down...")
        await self.bot.logout()
        print("Shutdown issued.")

    @commands.check(ownercheck)
    @commands.command()
    async def restart(self):
        await self.bot.say("<:away2:464520569862357002> Restarting...")
        await self.bot.logout()
        subprocess.call([sys.executable, "bot.py"])

    @commands.check(ownercheck)
    @commands.command()
    async def relay(self, server, channel, *, message):
        await self.bot.say("<:bfdyes:414604312296030208> Relayed message")
        server = self.bot.get_server(server)
        channel = self.bot.get_channel(channel)
        await self.bot.send_message(channel, message)

    @commands.check(ownercheck)
    @commands.command()
    async def status(self, *, status):
        await self.bot.change_presence(game=discord.Game(name=status))
        await self.bot.say("<:bfdyes:414604312296030208> Changed playing status")

    @commands.check(ownercheck)
    @commands.command()
    async def say(self, *, arg):
        await self.bot.say(arg)

    @commands.check(ownercheck)
    @commands.command()
    async def loadsudo(self):
        await self.bot.say("<a:loading:473853564406595614> Loading sudo mode...")
        await self.bot.logout()
        subprocess.call([sys.executable, "sudo-bot.py"])

def setup(bot):
    bot.add_cog(Owner(bot))