from glob import glob
import discord

from discord import Intents
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.errors import HTTPException
from discord.ext.commands import Bot as BotBase
from discord.ext.commands.errors import (BadArgument, BotMissingPermissions, CommandNotFound, MissingAnyRole, MissingRequiredArgument, MissingPermissions)

from ..db import db

PREFIX = "s/"
OWNER_IDS = [274948587295735809, 549213551236087808, 602779813089902600]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        db.autosave(self.scheduler)
        super().__init__(
            command_prefix=PREFIX,
            owner_ids=OWNER_IDS,
            intents=Intents.all()
        )

    def setup(self):
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f"Cog Loaded: '{cog}'.")

        print("Setup Complete.")

    def run(self, version):
        self.VERSION = version

        print("Running Setup...")
        self.setup()

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("Running Bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("Bot Connecting...")

    async def on_disconnect(self):
        print("Bot Disconnected.")

    async def on_error(self, err, *args, **kwargs):
        await self.stdout.send("Unfortunately, an unidentified error occured.")

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            await ctx.send("That command could not be found! Please check if the command you are looking for is valid, and try again.")
        elif isinstance(exc, BadArgument):
            await ctx.send("You made a bad argument. Please correct your mistake and try again.")
        elif isinstance(exc, MissingPermissions):
            await ctx.send("You don't have permission to do that!")
        elif isinstance(exc, BotMissingPermissions):
            await ctx.send("I'm missing the permissions to do that!")
        elif isinstance(exc, MissingRequiredArgument):
            await ctx.send("You're missing one or more required arguments. Please correct your mistake and try again.")
        elif isinstance(exc.original, HTTPException):
            await ctx.send("Unfortunately, I'm unable to send a message.")
        else:
            raise exc.original

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.stdout = self.get_channel(794240927950569472)
            self.scheduler.start()
            self.update_channel = self.get_channel(795779002857554020)

            await self.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=f"[s/] | Watching {len(self.guilds)} servers"))

            print("Bot Ready.")
            await self.update_channel.send("Bot Ready.")
            

        else:
            print("Bot Reconnected.")
            await self.update_channel.send("Bot Reconnected.")

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)

bot = Bot()