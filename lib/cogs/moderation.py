from discord.ext.commands import Cog
from discord.ext.commands import command, has_permissions, bot_has_permissions
from discord import Member, User, member
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
	async def ban(self, ctx, member: Member, reason = None):
		self.log_channel = ctx.guild.system_channel
		await member.ban(reason=reason)
		await ctx.message.delete()
		await ctx.send(f'Banned {member.mention}')
		embed = Embed(title="Ban", timestamp=datetime.now(), colour=0xFF0000)
		embed.add_field(name="Banned User:", value=member.mention, inline=False)
		embed.add_field(name="Admin User:", value=ctx.author.mention, inline=True)
		embed.add_field(name="Reason:", value=reason, inline=False)
		embed.add_field(name="See you in hell!", value=f"You naughty child, you aren't getting any presents this year!", inline=True)
		embed.set_author(name=member.name, icon_url=member.avatar_url)
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text="Unban ID: " + str(member.id) + " Admin ID: " + str(ctx.author.id))
		await self.log_channel.send(embed=embed)
		return

	@command(name="kick", aliases=["tempkick"])
	@bot_has_permissions(kick_members=True)
	@has_permissions(kick_members=True)
	async def kick(self, ctx, member: Member, *, reason = None):
		self.log_channel = ctx.guild.system_channel
		await member.kick(reason=reason)
		await ctx.message.delete()
		await ctx.send(f'Kicked {member.mention}')
		embed = Embed(title="Kick", timestamp=datetime.now(), colour=0xFFA500)
		embed.add_field(name="Kicked User:", value=member.mention, inline=False)
		embed.add_field(name="Admin User:", value=ctx.author.mention, inline=True)
		embed.add_field(name="Reason:", value=reason, inline=False)
		embed.add_field(name="You can do better", value=f"Come on, Work Harder! DO IT!", inline=True)
		embed.set_author(name=member.name, icon_url=member.avatar_url)
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text="Unban ID: " + str(member.id) + " Admin ID: " + str(ctx.author.id))
		await self.log_channel.send(embed=embed)
		return

	@command(name="unban", aliases=["permaunban", "tempunban"])
	@bot_has_permissions(ban_members=True)
	@has_permissions(ban_members=True)
	async def unban(self, ctx, member: str):
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split('#')

		for ban_entry in banned_users:
			user = ban_entry.user
			
		if (user.name, user.discriminator) == (member_name, member_discriminator):
			self.log_channel = ctx.guild.system_channel
			await ctx.guild.unban(user)
			await ctx.message.delete()
			await ctx.send(f'Unbanned {user.mention}')
			embed = Embed(title="Unban", timestamp=datetime.now(), colour=0xBFFF00)
			embed.add_field(name="Unbanned User:", value=user.mention, inline=False)
			embed.add_field(name="Admin User:", value=ctx.author.mention, inline=True)
			embed.add_field(name="Everyone deserves a second chance!", value=f"Except you, <@495696567479697423>", inline=False)
			embed.set_author(name=user.name, icon_url=user.avatar_url)
			embed.set_thumbnail(url=user.avatar_url)
			embed.set_footer(text="Unban ID: " + str(user.id) + " Admin ID: " + str(ctx.author.id))
			await self.log_channel.send(embed=embed)
			return

def setup(bot): 
	bot.add_cog(Moderation(bot))