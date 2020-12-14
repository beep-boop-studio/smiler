from discord.ext.commands import Cog, Greedy, Context
from typing import Optional
from discord.ext.commands import command, has_permissions, bot_has_permissions
from discord import Member, User
from discord import Embed
from datetime import datetime

class Moderation(Cog):
	def __init__(self, bot):
		self.bot = bot



	@Cog.listener()
	async def on_ready(self):
		print("Moderation Cog Ready.")

	@command(name="ban", aliases=["permaban", "tempban"])
	@bot_has_permissions(ban_members=True)
	@has_permissions(ban_members=True)
	async def ban(self, ctx, members: Greedy[Member], reason: Optional[str] = "For No Reason. Now that's not very good!", time: Optional[float] = None, interval: Optional[str] = None):
		if not len(members):
			await ctx.send("Missing Arguments")
		else:
			for member in members:
				self.log_channel = member.guild.system_channel
				await member.ban(reason=reason)
				embed = Embed(title="@" + member.name + " was banned by @" + ctx.author.name, timestamp=datetime.now(), colour=0xFF0000)
				embed.add_field(name="See you in hell", value="You naughty child, you're not getting any presents this year!", inline=False)
				embed.set_author(name=member.name, icon_url=member.avatar_url)
				embed.set_thumbnail(url=member.avatar_url)
				embed.set_footer(text="Ban ID: " + str(member.id) + " Admin ID: " + str(ctx.author.id))
				await self.log_channel.send(embed=embed)


	@ban.error
	async def ban_error(self, ctx, exc):
		if isinstance(exc.original, Exception):
			await ctx.send("Please specify a time interval!")

	@command(name="kick", aliases=["tempkick"])
	@bot_has_permissions(kick_members=True)
	@has_permissions(kick_members=True)
	async def kick(self, ctx, members: Greedy[Member], reason: Optional[str] = "For No Reason. No that's not very good!"):
		if not len(members):
			await ctx.send("Missing Arguments")
		else:
			for member in members:
				self.log_channel = member.guild.system_channel
				await member.kick(reason=reason)
				embed = Embed(title="@" + member.name + " was kicked by @" + ctx.author.name, timestamp=datetime.now(), colour=0xFF0000)
				embed.add_field(name="You can do better!", value="Come on, man. Work harder!", inline=False)
				embed.set_author(name=member.name, icon_url=member.avatar_url)
				embed.set_thumbnail(url=member.avatar_url)
				embed.set_footer(text="Kick ID: " + str(member.id) + " Admin ID: " + str(ctx.author.id))
				await self.log_channel.send(embed=embed)

	@command(name="unban", aliases=["tempunban"])
	@bot_has_permissions(ban_members=True)
	@has_permissions(ban_members=True)
	async def unban(self, ctx, member):
		user = await bot.fetch_user(id)
		await ctx.guild.unban(user)


def setup(bot): 
	bot.add_cog(Moderation(bot))