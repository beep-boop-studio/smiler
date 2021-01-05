from datetime import datetime, timedelta
from random import choice

from discord import Embed
from discord.ext.commands import Cog
from discord.ext.commands import command, has_permissions

from ..db import db

# Here are all the number emotes.
# 0⃣ 1️⃣ 2⃣ 3⃣ 4⃣ 5⃣ 6⃣ 7⃣ 8⃣ 9⃣

numbers = ("1️⃣", "2⃣", "3⃣", "4⃣", "5⃣",
		   "6⃣", "7⃣", "8⃣", "9⃣", "🔟")

class Reactions(Cog):
	def __init__(self, bot):
		self.bot = bot
		self.polls = []
		self.giveaways = []

	@Cog.listener()
	async def on_ready(self):
		print("Cog Ready: 'Reactions'")

	@command(name="createpoll", aliases=["mkpoll", "mkp"])
	@has_permissions(manage_guild=True)
	async def create_poll(self, ctx, seconds: int, question: str, *options):
		if len(options) > 10:
			await ctx.send("You can only give 10 options.")

		else:
			embed = Embed(title="Poll Time!",
						  description=question,
						  colour=0xC0C0C0,
						  timestamp=datetime.utcnow())
           
			fields = [("Options:", "\n".join([f"{numbers[idx]} {option}" for idx, option in enumerate(options)]), False),
					  ("Instructions:", "React to cast a vote!", False),
                      ("Voting Time:", f"{seconds} seconds.", False)]
			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)
			message = await ctx.send(embed=embed)
			for emoji in numbers[:len(options)]:
				await message.add_reaction(emoji)
			self.polls.append((message.channel.id, message.id))
			self.bot.scheduler.add_job(self.complete_poll, "date", run_date=datetime.now()+timedelta(seconds=seconds),
									   args=[message.channel.id, message.id])

	async def complete_poll(self, channel_id, message_id):
		message = await self.bot.get_channel(channel_id).fetch_message(message_id)
		most_voted = max(message.reactions, key=lambda r: r.count)

		await message.channel.send(f"The results are in and option {most_voted.emoji} is the winner with {most_voted.count-1:,} votes!")
		self.polls.remove((message.channel.id, message.id))

	@Cog.listener()
	async def on_raw_reaction_add(self, payload):
		if payload.message_id in (poll[1] for poll in self.polls):
			message = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

			for reaction in message.reactions:
				if (not payload.member.bot
					and payload.member in await reaction.users().flatten()
					and reaction.emoji != payload.emoji.name):
					await message.remove_reaction(reaction.emoji, payload.member)

def setup(bot):
	bot.add_cog(Reactions(bot))