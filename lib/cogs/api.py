
from discord.ext.commands.cog import Cog
from aiohttp import request
from discord.ext.commands import command
from discord import Embed
import praw

class API(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.primary_colour = 0xC0C0C0

    @command(name="meme", brief="Sends a meme.")
    async def meme(self, ctx):
        '''Sends a meme.'''
        URL = "https://some-random-api.ml/meme"

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                await ctx.message.delete()
                data = await response.json()

                embed = Embed(title=data["caption"],
                              description=data["image"],
                              colour=self.primary_colour)
                embed.set_image(url=data["image"])
                await ctx.send(embed=embed)

            else:
                await ctx.send(f"API returned a {response.status} status")

    @command(name="joke", brief="Tells a joke.")
    async def say_joke(self, ctx):
        '''Tells a joke..'''
        URL = "https://some-random-api.ml/joke"

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                await ctx.message.delete()
                data = await response.json()

                embed = Embed(title="Joke", 
                              description=data["joke"], 
                              colour=self.primary_colour)
                await ctx.send(embed=embed)   
    
    @command(name="fact", aliases=["animalfact"], brief="Gives animal facts.")
    async def animal_fact(self, ctx, animal: str):
        '''Gives animal facts.'''
        if (animal := animal.lower()) in ("dog", "cat", "panda", "fox", "bird", "koala"):
            fact_url = f"https://some-random-api.ml/facts/{animal}"
            image_url = f"https://some-random-api.ml/img/{'birb' if animal == 'bird' else animal}"

            async with request("GET", image_url, headers={}) as response:
                if response.status == 200:
                    data = await response.json()
                    image_link = data["link"]

                else:
                    image_link = None

            async with request("GET", fact_url, headers={}) as response:
                if response.status == 200:
                    await ctx.message.delete()
                    data = await response.json()

                    embed = Embed(title=f"{animal.title()} Fact", 
                                description=data["fact"], 
                                colour=self.primary_colour)
                    if image_link is not None:
                        embed.set_image(url=image_link)
                    await ctx.send(embed=embed)
        else:
            await ctx.send("No facts are available for your chosen animal.")

    @command(name="wasted", brief="Adds a wasted overlay to an image.")
    async def wasted_image(self, ctx, image_url):
        '''Adds a wasted overlay to an image.'''
        image = f"https://some-random-api.ml/canvas/wasted?avatar={image_url}"

        async with request("GET", image, headers={}) as response:
            if response.status == 200:
                await ctx.message.delete()                
                embed = Embed(title="Wasted...",
                              colour=0xFF5D52)
                if image is not None:
                    embed.set_image(url=image)
                await ctx.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        print("Cog Ready: 'API'")

def setup(bot):
    bot.add_cog(API(bot))
