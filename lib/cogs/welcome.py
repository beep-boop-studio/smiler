from discord.errors import Forbidden
from discord.ext.commands import command
from discord.ext.commands import Cog
from discord import Embed
import random

from ..db import db

class Welcome(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.primary_colour = 0xC0C0C0

    @Cog.listener()
    async def on_ready(self):
        print("Cog Ready: 'Welcome'")

    @Cog.listener()
    async def on_member_join(self, member):
        responses = [f"Enjoy your stay at **{member.guild.name}**, **{member.mention}**!",
                     f"Welcome to **{member.guild.name}**! Enjoy your stay here, **{member.mention}**!",
                     f"Welcome, **{member.mention}**! Enjoy your stay at **{member.guild.name}**!"]
        embed = Embed(title="Hello!",
                      description=f"{random.choice(responses)}",
                      colour=self.primary_colour)
        embed.set_author(name=f"{member.display_name}", icon_url=member.avatar_url)
        db.execute("INSERT INTO exp (UserID) VALUES (?)", member.id)
        await member.guild.system_channel.send(embed=embed)

        try:
            await member.send(embed=embed)

        except Forbidden:
            pass

    @Cog.listener()
    async def on_member_remove(self, member):
        responses = [f"Farewell, **{member.mention}**! We hope you had a good time in **{member.guild.name}**!",
                     f"Goodbye, **{member.mention}**! We hope you enjoyed your stay at **{member.guild.name}**!",
                     f"Goodbye, **{member.mention}**! We'll miss you..."]
        embed = Embed(title="Goodbye!",
                      description=f"{random.choice(responses)}",
                      colour=self.primary_colour)
        embed.set_author(name=f"{member.display_name}", icon_url=member.avatar_url)
        await member.guild.system_channel.send(embed=embed)
        await db.execute("DELETE FROM exp WHERE UserID = ?", member.id)

        try:
            await member.send(embed=embed)

        except Forbidden:
            pass


def setup(bot):
    bot.add_cog(Welcome(bot))