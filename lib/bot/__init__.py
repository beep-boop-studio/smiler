<<<<<<< HEAD
from discord import Embed, Intents
=======
from os import name
from discord import Intents
>>>>>>> d74b81a4c589dcdb65ee211ca020621bfdcaf5f2
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed
from discord.ext.commands import Bot as BotBase
from discord import utils
from datetime import datetime

PREFIX = "s/"
OWNER_IDS = [274948587295735809, 549213551236087808, 602779813089902600]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(
            command_prefix=PREFIX, 
            owner_ids=OWNER_IDS,
            intents=Intents.all()
            )

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("Running Bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("Bot Connected.")

    async def on_disconnect(self):
        print("Bot Disconnected.")

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            print("Bot Ready.")

        else:
            print("Bot Reconnected.")

    async def on_message(self, message):
        pass

    async def on_guild_join(self, guild):
        print("Joined Server with ID: " + str(guild.id))
        channel = guild.system_channel

        embed = Embed(title="The ultimate all-purpose Discord Bot", description="Make your server a better place!", timestamp=datetime.now())
        fields = [("What Can I Do?", "-Auto Moderation\n-Polls\n-POKEMON, gotta catch em all!", True),
                  ("What Can't I Do?", "-Your mama\n-The 100m meter sprint\n-Get you to stop watching anime", True),
                  ("Contribute to me!", "1. Post issues and pull requests at **https://www.github.com/beep-boop-studio/smiler/**\n2. Support my developers at **https://www.patreon.com/beepboopstudio**\n2. Join the team at **https://www.studiobeepboop.com/**", False)
                  ]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        embed.set_author(name="Welcome to Smiler v" + self.VERSION, icon_url=self.user.avatar_url)
        embed.set_footer(text="Copyright © Beep Boop Studio Ltd 2020. All Rights Reserved.")

        await channel.send(embed=embed)

bot = Bot()
         

    

        