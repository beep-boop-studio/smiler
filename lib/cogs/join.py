from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed
from datetime import datetime

class Join(Cog):
	def __init__(self, bot):
		self.bot = bot

	@Cog.listener()
	async def on_ready(self):
		print("Join Cog Ready.")

	@command(name="info", aliases=["information", "status", "update"])
	async def info(self, ctx):

		embed = Embed(title="A free, open-source, feature-packed Discord Bot", description="Spice up your Discord server!", timestamp=datetime.now(), colour=0xc0c0c0)
		fields = [("What Can I Do?", "-Auto Moderation\n-Polls\n-Automatic Roles", True),
				  ("What Can't I Do?", "-Play Music\n-Stream Anime\n-Steal Personal Data", True),
				  ("Contribute to me!", "1. Post issues and pull requests at **https://www.github.com/beep-boop-studio/smiler/**\n2. Support my creators at **https://www.patreon.com/beepboopstudio**\n2. Join the team at **https://www.studiobeepboop.com/**", False)
				 ]

		for name, value, inline in fields:
			embed.add_field(name=name, value=value, inline=inline)

		embed.set_author(name="Welcome to Smiler v" + self.bot.VERSION, icon_url=self.bot.user.avatar_url)
		embed.set_footer(text="Copyright © Beep Boop Studio Ltd 2020. All Rights Reserved.")

		await ctx.send(embed=embed)

	@Cog.listener()
	async def on_guild_join(self, guild):
		print("Joined server with ID: " + str(guild.id))
		channel = guild.system_channel

		embed = Embed(title="A free, open-source, feature-packed Discord Bot", description="Spice up your Discord server!", timestamp=datetime.now(), colour=0xc0c0c0)
		fields = [("What Can I Do?", "-Auto Moderation\n-Polls\n-Automatic Roles", True),
				  ("What Can't I Do?", "-Play Music\n-Stream Anime\n-Steal Personal Data", True),
				  ("Contribute to me!", "1. Post issues and pull requests at **https://www.github.com/beep-boop-studio/smiler/**\n2. Support my creators at **https://www.patreon.com/beepboopstudio**\n2. Join the team at **https://www.studiobeepboop.com/**", False)
				 ]

		for name, value, inline in fields:
			embed.add_field(name=name, value=value, inline=inline)

		embed.set_author(name="Welcome to Smiler v" + self.bot.VERSION, icon_url=self.bot.user.avatar_url)
		embed.set_footer(text="Copyright © Beep Boop Studio Ltd 2020. All Rights Reserved.")

		await channel.send(embed=embed)

	@Cog.listener()
	async def on_member_join(self, member):
		print("Member with ID: " + str(member.id) + " joined Server with ID: " + str(member.guild.id))
		channel = member.guild.system_channel

		embed = Embed(title="Join", timestamp=datetime.now(), colour=0x00FF00)
		embed.add_field(name="Joining Member", value=member.mention, inline=False)
		embed.add_field(name="Member Number", value="#" + str(member.guild.member_count), inline=True)
		embed.add_field(name="Welcome to this beautiful server!", value="We are glad you are here", inline=False)
		embed.set_author(name=member.name, icon_url=member.avatar_url)
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text="ID: " + str(member.id))

		await channel.send(embed=embed)
	
	@Cog.listener()
	async def on_member_leave(self, member):
		print("Member with ID: " + str(member.id) + " left Server with ID: " + str(member.guild.id))
		channel = member.guild.system_channel

		embed = Embed(title="Leave", timestamp=datetime.now(), colour=0xD3D3D3)
		embed.add_field(name="Leaving Member", value=member.mention, inline=False)
		embed.add_field(name="New Member Count", value="#" + str(member.guild.member_count), inline=True)
		embed.add_field(name="See you soon!", value="We are sad to see you go!", inline=False)
		embed.set_author(name=member.name, icon_url=member.avatar_url)
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text="ID: " + str(member.id))

		await channel.send(embed=embed)

def setup(bot): 
	bot.add_cog(Join(bot))