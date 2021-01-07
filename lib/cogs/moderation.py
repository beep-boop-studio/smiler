from typing import Optional
from datetime import datetime
import random

import discord
from discord import Member, Embed
from discord import guild

from discord.ext.commands import Cog
from discord.ext import commands
from discord.ext.commands import command

from better_profanity import profanity
profanity.load_censor_words_from_file("./data/profanity.txt")

from ..db import db

class Moderation(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.primary_colour = 0xC0C0C0

    @command(name="slap", aliases=["spank", "hit"], brief="Slaps a member.")
    @commands.has_permissions(administrator=True)
    @commands.has_any_role("Developers", "Administrators", "Owners", "Shareholders", "Co-Founders")
    async def slap_member(self, ctx, member: Member, *, reason: Optional[str] = "something idk"):
        '''Slaps a member.'''
        first = [f"Die, {member.mention}!",
                 f"Take that, {member.mention}!",
                 f"Stupid idiot..."]
        second = [f"There are others who recieved worse, and yes, I'm talking to you, <@495696567479697423>!",
                  f"Now, there *definitely* are worse punishments, right?",
                  f"If I'm being honest, I was kinda hoping {ctx.author.display_name} was going to ban you, {member.mention}."]
        await ctx.send(f"{ctx.author.mention} slapped {member.mention} {reason}! {random.choice(first)} {random.choice(second)}")

    @command(name="maketextchannel", aliases=["mktc"], brief="Creates a text channel.")
    @commands.has_permissions(manage_channels=True)
    async def create_channel(self, ctx, ch_name):
        '''Creates a text channel.'''
        channel = await ctx.guild.create_text_channel(ch_name)
        await ctx.send(f"<#{channel.id}> was successfully created, {ctx.message.author.mention}!")

    @command(name="deltextchannel", aliases=["dtc"], brief="Deletes a text channel.")
    @commands.has_permissions(manage_channels=True)
    async def delete_channel(self, ctx, channel):
        '''Deletes a text channel.'''
        channel = discord.utils.get(ctx.guild.channels, name=channel)
        
        if channel is not None:
            await channel.delete()
            await ctx.send(f"#{channel} was successfully deleted, {ctx.message.author.mention}!")

        else:
            await ctx.send(f"No channel named {channel} was found, {ctx.message.author.mention}!")

    @command(name="echo", aliases=["say"], brief="Echoes a message.")
    @commands.has_any_role("Developers", "Administrators", "Owners", "Shareholders", "Co-Founders")
    async def say_echo(self, ctx, *, message):
        '''Echoes a message.'''
        await ctx.message.delete()
        await ctx.send(message)
    
    @command(name="clear", aliases=["purge", "delete"], brief="Deletes a select number of messages.")
    @commands.has_permissions(manage_messages=True)
    async def clear_messages(self, ctx, limit: Optional[int] = 1, sender: Optional[str] = None):
        '''Deletes a select number of messages.'''
        with ctx.channel.typing():
            await ctx.message.delete()
            deleted = await ctx.channel.purge(limit=limit)

            await ctx.send(f"I successfully deleted `{len(deleted):,}` messages!", delete_after=10)
    
    @command(name="giveguilds", aliases=["gg"], brief="Displays bot guilds.")
    @commands.has_permissions(manage_guild=True)
    async def give_guilds(self, ctx):
        '''Displays bot guilds.'''
        async for guild in self.bot.fetch_guilds(limit=200):
            embed = Embed(title=f"{guild}",
                            colour=self.primary_colour,
                            datetime=datetime.utcnow())
            await ctx.send(embed=embed)
    
    @command(name="bannedmembers", alises=["bm"], brief="Shows banned members.")
    async def banned_members(self, ctx):
        '''Shows banned members.'''
        banned_members = await ctx.guild.bans()

        for ban_entry in banned_members:
            member = ban_entry.user

            embed = Embed(title="Banned Users:",
                            description=f"{member}",
                            colour=self.primary_colour)
            await ctx.send(embed=embed)

    @command(name="kick", brief="Kicks a member.")
    @commands.has_permissions(kick_members=True)
    async def kick_member(self, ctx, member : discord.Member, *, reason=None):
        '''Kicks a member.'''
        await member.kick(reason=reason)
        embed = Embed(title="Member Kicked",
                      description=f"{ctx.message.author.mention} has kicked {member.mention} {reason}.",
                      colour=self.primary_colour)
        embed.add_field(name="Reason:", value=f"{reason}", inline=False)
        embed.add_field(name="Peformed By:", value=f"{ctx.message.author.mention}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(name="Smiler Pro", icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @command(name="ban", brief="Bans a member.")
    @commands.has_permissions(kick_members=True)
    async def ban_member(self, ctx, member : discord.Member, *, reason=None):
        '''Bans a member.'''
        await member.ban(reason=reason)
        embed = Embed(title="Member Banned",
                      description=f"{member.mention} has been banned.",
                      colour=self.primary_colour)
        embed.add_field(name="Reason:", value=f"{reason}", inline=False)
        embed.add_field(name="Peformed By:", value=f"{ctx.message.author.mention}")
        embed.add_field(name="Unban ID:", value=f"{member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(name="Smiler Pro", icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @command(name="unban", brief="Unbans a banned member")
    @commands.has_permissions(ban_members=True)
    async def unban_member(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = Embed(title="Member Unbanned",
                              description=f"{user.name} has been unbanned.",
                              colour=self.primary_colour)
                embed.add_field(name="Peformed By:", value=f"{ctx.message.author.mention}")
                embed.set_thumbnail(url=user.avatar_url)
                embed.set_author(name="Smiler Pro", icon_url=self.bot.user.avatar_url)
                await ctx.send(embed=embed)

    @command(name="warn", brief="Gives a warning to a member.")
    @commands.has_permissions(kick_members=True, manage_nicknames=True)
    async def warn_member(self, ctx, member : discord.Member, *, reason):
        '''Gives a warning to a member.'''
        await ctx.message.delete()
        embed = Embed(title=f"Warning from {ctx.message.author.name}!",
                      description=f"{reason}.",
                      colour=self.primary_colour)
        await member.send(embed=embed)
        await ctx.send(f"Message successfully sent to {member.mention}.", delete_after=10)

    @command(name="addprofanity", aliases=["addswears", "as"], brief="Adds curses to profanity.txt")
    @commands.has_permissions(manage_guild=True)
    async def add_profanity(self, ctx, *words):
        '''Adds curses to profanity.txt'''
        await ctx.message.delete()
        with open("./data/profanity.txt", "a", encoding="utf-8") as f:
            f.write("".join([f"{w}\n" for w in words]))

        profanity.load_censor_words_from_file(("./data/profanity.txt"))
        await ctx.send("Action Complete.")

    @command(name="delprofanity", aliases=["delpro", "rp"], brief="Removes curses to profanity.txt")
    @commands.has_permissions(manage_guild=True)
    async def remove_profanity(self, ctx, *words):
        '''Adds curses to profanity.txt'''
        await ctx.message.delete()
        with open("./data/profanity.txt", "r", encoding="utf-8") as f:
            stored = [w.strip() for w in f.readlines()]
        with open("./data/profanity.txt", "w", encoding="utf-8") as f:
            f.write("".join([f"{w}\n" for w in stored if w not in words]))
            
    @Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if profanity.contains_profanity(message.content):
                await message.delete()
                naughty = ["You literally *just* used a bad word...",
                           "Don't **ever** use that word again. Yes, you know the one i'm talking about!",
                           "You used a bad word. Don't let that mistake happen again!",
                           "**Who** taught you such bad language?!"]
                await message.author.send(f"{random.choice(naughty)}")

    @Cog.listener()
    async def on_ready(self):
        print("Cog Ready: 'Moderation'")

def setup(bot):
    bot.add_cog(Moderation(bot))