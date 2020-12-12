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
		channel = ctx.guild.system_channel

		embed = Embed(title="The ultimate all-purpose Discord Bot", description="Make your server a better place!", timestamp=datetime.now())
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
	async def on_guild_join(self, guild):
		channel = guild.system_channel

		embed = Embed(title="The ultimate all-purpose Discord Bot", description="Make your server a better place!", timestamp=datetime.now())
		fields = [("What Can I Do?", "-Auto Moderation\n-Polls\n-POKEMON, gotta catch em all!", True),
				  ("What Can't I Do?", "-Your mama\n-The 100m meter sprint\n-Get you to stop watching anime", True),
				  ("Contribute to me!", "1. Post issues and pull requests at **https://www.github.com/beep-boop-studio/smiler/**\n2. Support my developers at **https://www.patreon.com/beepboopstudio**\n2. Join the team at **https://www.studiobeepboop.com/**", False)
				 ]
		for name, value, inline in fields:
			embed.add_field(name=name, value=value, inline=inline)

		embed.set_author(name="Welcome to Smiler v" + self.bot.VERSION, icon_url=self.bot.user.avatar_url)
		embed.set_footer(text="Copyright © Beep Boop Studio Ltd 2020. All Rights Reserved.")

		await channel.send(embed=embed)

def setup(bot): 
	bot.add_cog(Join(bot))