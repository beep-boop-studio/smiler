from typing import Optional
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed
import random

from discord.member import Member

class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="kill", brief="Kills a user.")
    async def kill_someone(self, ctx, member: Member):
        '''Kills a user.'''
        responses = [f"{ctx.message.author.mention} slips bleach into {member.mention}'s lemonade.",
            f"{member.mention} dies of natural causes.",
            f"{member.mention} dies from bad succ.",
            f"{member.mention} dies from dabbing too hard.",
            f"{member.mention} dies from posting normie memes.",
            f"{member.mention} dies from disrespecting wahmen.",
            f"{member.mention} dies from watching the emoji movie and enjoying it.",
            f"{ctx.message.author.mention} hired me to kill you, but I don't want to! {member.mention}",
            f"{member.mention} slips on a banana peel and falls down the stairs.",
            f"{ctx.message.author.mention} murders {member.mention} with an axe.",
            f"{ctx.message.author.mention} pressed delete. It deleted {member.mention}",
            f"{member.mention} dies because they used a bobby pin to lift their eyelashes",
            f"{member.mention} dies because they were just too angry.",
            f"{member.mention} decided it was a good idea to fight a tiger while smelling like meat. It did not end well.",
            f"{member.mention} disappeared from the universe.",
            f"{member.mention} drank some toxic soda before it was recalled.",
            f"{member.mention} was killed by {ctx.message.author.mention} with baby wipes.",
            f"{member.mention} dies in a horrible accident, and it was engineered by {ctx.message.author.mention}.",
            f"{member.mention} dies of starvation.",
            f"{ctx.message.author.mention} decapitates {member.mention} with a sword.",
            f"{ctx.message.author.mention} challenges {member.mention} to a fist fight to the death. {member.mention} wins.",
            f"Sorry, {ctx.message.author.mention}, I don't like killing people.",
            f"{member.mention} dies after swallowing a toothpick.",
            f"{member.mention} was murdered by {ctx.message.author.mention} and everyone knows it, but there is no proof.",
            f"{ctx.message.author.mention} kills {member.mention} after hours of torture.",
            f"{member.mention} dies on death row via lethal injection after murdering {ctx.message.author.mention} and their family.",
            f"{member.mention} vocally opposed the Clintons and then suddenly disappeared.",
            f"{ctx.message.author.mention} shoots {member.mention} in the head.",
            f"{ctx.message.author.mention}, are you sure you want to kill {member.mention}? They seem nice to me.",
            f"{member.mention} lives, despite {ctx.message.author.mention}'s murder attempt.",
            f"{member.mention} gets hit by a car.",
            f"{member.mention} gets struck by lightning.",
            f"{member.mention} reads memes till they die.",
            f"{member.mention} dies at the hands of {ctx.message.author.mention}.",
            f"{member.mention} has some bad chinese food, and pays the ultimate price.",
            f"{member.mention} chokes on cheerios and dies. What an idiot...",
            f"{member.mention} is killed by their own stupidity.",
            f"{member.mention} is killed in a robbery gone wrong.",
            f"{member.mention} is dead at the hands of {ctx.message.author.mention}.",
            f"{member.mention} can't be killed, as they are a ghost.",
            f"{member.mention} gets stabbed by {ctx.message.author.mention}",
            f"In a sudden turn of events, I **don't** kill {member.mention}.",
            f"{member.mention} kills themselves after realizing how dumb {ctx.message.author.mention} is.",
            f"{member.mention} bleeds out after trying to get on \"Dumbest hillbilly moments\".",
            f"{member.mention} is not able to be killed. Oh, wait, no, {ctx.message.author.mention} kills them anyway.",
            f"{ctx.message.author.mention} strangles {member.mention}.",
            f"After getting pushed into the ocean by {ctx.message.author.mention}, {member.mention} is eaten by a shark.",
            f"{member.mention} dies.", f"After a struggle, {member.mention} kills {ctx.message.author.mention}",
            f"{member.mention} is abducted by aliens, and the government kills them to cover it up.",
            f"{member.mention} got stepped on by an elephant.", f"{member.mention} died from eating too much ass.",
            f"{member.mention} is so dumb that they choked on oxygen.",
            f"{member.mention} died from not eating enough ass.",
            f"{member.mention} died from doing the ice bucket challenge.",
            f"{member.mention} died from eating too much ass.",
            f"The bullet missed Harambe and hit {member.mention} instead. Yay for Harambe!",
            f"Aids, {member.mention} died from aids.",
            f"{member.mention} died because RemindMeBot forgot to remind them to breathe",
            f"{member.mention} got into a knife fight with the pope. One of them is in hell now.",
            f"{member.mention} died from swallowing rocks too fast",
            f"{member.mention} accidentally clicked on a popup ad that reads \"Doctors hate us, see the one best trick for dying today!\"",
            f"{member.mention} died from ebola.",
            f"{member.mention} fell into a pit of angry feminists.",
            f"{member.mention} died from drinking too much water Huh, I guess it IS possible!.",
            f"{member.mention} died while playing hopscotch on *seemingly* deactivated land mines.",
            f"{member.mention} ripped their own heart out to show their love for {ctx.message.author.mention}.",
            f"{member.mention} died from too many sunburns.",
            f"{member.mention} died from a swift kick to the brain.",
            f"{member.mention} was eaten alive by ants",
            f"{member.mention} died after gaming for 90 hours straight without moving or eating.",
            f"{member.mention} tried to outrun a train, the train won.",
            f"{member.mention} killed themselves after seeing the normie memes that {ctx.message.author.mention} posts.",
            f"{member.mention} talked back to mods and got destroyed by the ban hammer.",
            f"{member.mention} died after trying to out-meme Smiler.",
            f"{member.mention} died from eating too much bread :/",
            f"{member.mention} died an honorable death. Death by snoo snoo.",
            f"{member.mention} tried to get famous on YouTube by live-streaming something dumb. Skydiving while chained to a fridge.",
            f"{member.mention} was walking normally when out of the corner of their eye they saw someone do a bottle flip and dab causing {member.mention} to have a stroke.",
            f"{member.mention} died from eating cactus needles.",
            f"{member.mention} died after playing with an edgy razor blade fidget spinner.",
            f"{member.mention} died because they started playing with a fidget spinner but they realise its 2016 so you start fapping to the old witch in snow white and obama starts mowing their lawn and they jump out of the window and get ripped to pieces by Obama's lawn mower",
            f"{member.mention} drowned in their own tears.",
            f"{member.mention} died of oversucc",
            f"{member.mention} accidentally tripped and died while getting up to write their suicide note.",
            f"{member.mention} died from whacking it too much. (There's a healthy balance, boys)",
            f"{member.mention} died from not whacking it enough. (There's a healthy balance, boys)",
            f"{ctx.message.author.mention} kills {member.mention} with their own foot.",
            f"{member.mention} dies due to lack of friends.",
            f"{member.mention} chokes on a chicken bone.",
            f"{member.mention} went on a ride with a lead balloon.",
            f"{member.mention} did not make a meme dank enough and was stoned.",
            f"Our lord and savior Gaben strikes {member.mention} with a lighting bolt.",
            f"{ctx.message.author.mention} tries to shoot the broad side of a barn, misses and hits {member.mention} instead.",
            f"{member.mention} slipped in the bathroom and choked on the shower curtain.",
            f"While performing colonoscopy on an elephant, {member.mention} gets their head stuck in the elephants rectum and chokes.",
            f"{ctx.message.author.mention} attempted to play a flute, exploding the head of {member.mention}.",
            f"{ctx.message.author.mention} straps {member.mention} to an ICBM and sends them to North Korea along with it.",
            f"{ctx.message.author.mention} drowns {member.mention} in a beer barrel.",
            f"{member.mention} was thrown in the crusher of a trash truck by {ctx.message.author.mention}.",
            f"{member.mention} dropped a Nokia phone on their face and split their skull.",
            f"{ctx.message.author.mention} cleaves the head of {member.mention} with a keyboard.",
            f"{ctx.message.author.mention} crushes {member.mention} with a fridge.",
            f"{member.mention} chokes in a trash can.",
            f"{ctx.message.author.mention} fires a supersonic frozen turkey at {member.mention}, killing them instantly.",
            f"{member.mention} watched the Emoji Movie and died of sheer cringe.",
            f"{ctx.message.author.mention} shoots in {member.mention} mouth with rainbow laser, causing {member.mention} head to explode with rainbows and {member.mention} is reborn as unicorn. :unicorn:",
            f"{member.mention} ate a piece of exotic butter. It was so amazing that it killed them.",
            f"{member.mention} is stuffed into a suit by Freddy on their night guard duty. Oh, not those animatronics again!",
            f"{ctx.message.author.mention} grabs {member.mention} and shoves them into an auto-freeze machine with some juice and sets the temperature to 100 Kelvin, creating human ice pops.",
            f"{ctx.message.author.mention} drowns {member.mention} in a tub of hot chocolate. *How was your last drink?*",
            f"{member.mention} screams in terror as they accidentally spawn in the cthulhu while uttering random latin words. Cthulhu grabs {member.mention} by the right leg and takes them to his dimension yelling, \"Honey, Dinner's ready!\"",
            f"{ctx.message.author.mention} feeds toothpaste-filled oreos to {member.mention}, who were apparently allergic to fluorine. GGWP.",
            f"{ctx.message.author.mention} forgot to zombie-proof {member.mention} lawn... Looks like zombies had a feast last night.",
            f"{member.mention} cranks up the music system only to realize the volume was at max and the song playing was Baby by Justin Beiber...",
            f"{member.mention} presses a random button and is teleported to the height of 100m, allowing them to fall to their inevitable death. Moral of the story: Don't go around pressing random buttons.",
            f"{member.mention} is injected with chocolate syrup, which mutates them into a person made out of chocolate. While doing a part-time job at the Daycare, they are devoured by the hungry babies. :chocolate_bar:",
            f"{member.mention} is sucked into Minecraft. {member.mention}, being a noob at the so called Real-Life Minecraft faces the Game Over screen.",
            f"{ctx.message.author.mention} turns on Goosebumps(2015 film) on the TV. {member.mention} being a scaredy-cat, dies of an heart attack.",
            f"{ctx.message.author.mention} after a long day, plops down on the couch with {member.mention} and turns on The Big Bang Theory. After a Sheldon Cooper joke, {member.mention} laughs uncontrollably as they die.",
            f"{member.mention} was given a chance to synthesize element 119 (Ununennium) and have it named after them, but they messed up. R.I.P.",
            f"{ctx.message.author.mention} gets {member.mention} to watch anime with them. {member.mention} couldn't handle it.",
            f"{member.mention} tried to get crafty, but they accidentally cut themselves with the scissors.:scissors:",
            f"{member.mention} goes genocide and Sans totally dunks {member.mention}!",
            f"{ctx.message.author.mention} was so swag that {member.mention} died due to it. #Swag",
            f"{member.mention} has been found guilty, time for their execution!",
            f"{member.mention} fell down a cliff while playing Pokemon Go. Good job on keeping your nose in that puny phone. :iphone:",
            f"{ctx.message.author.mention} strikes {member.mention} with the killing curse... *Avada Kedavra!*",
            f"{member.mention} ate an apple and turned out it was made out of wax. Someone died from wax poisoning later that day.",
            f"{member.mention} was teleported to the timeline where Jurassic World was real and they were eaten alive by the Indominus Rex.",
            f"{member.mention} was charging their Samsung Galaxy Note 7...",
            f"{ctx.message.author.mention} shot {member.mention} using the Starkiller Base!",
            f"{member.mention} was a resident of Alderaan before Darth Vader destroyed the planet...",
            f"{member.mention} was scooped by {ctx.message.author.mention} and their innards are now Ennard.",
            f"{ctx.message.author.mention} Alt+F4'd {member.mention}.exe!",
            f"{member.mention} was accused of stealing Neptune's crown...",
            f"{ctx.message.author.mention} eviscerates {member.mention} with a rusty butter knife. Ouch!",
            f"{ctx.message.author.mention} pushes {member.mention} into the cold vacuum of space.",
            f"{ctx.message.author.mention} runs {member.mention} over with a PT Cruiser.",
            f"{member.mention} trips over his own shoe laces and dies.",
            f"{member.mention} tried to pick out the holy grail. He chose... poorly.",
            f"{ctx.message.author.mention} hulk smashes {member.mention} into a pulp.",
            f"{member.mention} steps on a george foreman and dies of waffle foot.",
            f"{member.mention} dies from just being a bad, un-likeable dude.",
            f"Calling upon the divine powers, {ctx.message.author.mention} smites {member.mention} and their heathen ways",
            f"{member.mention} has a stroke after a sad miserable existence. They are then devoured by their ample cats.",
            f"{member.mention} takes an arrow to the knee. And everywhere else.",
            f"{member.mention} dies of dysentery.",
            f"{member.mention} dies of AIDS.",
            f"{ctx.message.author.mention} killed {member.mention} by ripping the skin off of their face and making a mask out of it.",
            f"{member.mention} spins a fidget spinner and when it stops he dies...",
            f"{member.mention} ripped his heart out..",
            f"{ctx.message.author.mention} fell in love with {member.mention} then broke his heart literally.",
            f"{ctx.message.author.mention} blew his ear drums out listening to music too hard.",
            f"{ctx.message.author.mention} hugs {member.mention} too hard..",
            f"{ctx.message.author.mention} tears off {member.mention}s lips after a kiss.",
            f"{ctx.message.author.mention} drags {member.mention}s ears too hard and rips them off.",
            f"{member.mention} tried to play in the street...",
            f"{member.mention} is killed by a rabbit with a vicious streak a mile wide",
            f"{ctx.message.author.mention} forgot to leave the car door window open and {member.mention} dies from overheating",
            f"{member.mention} dies, but don't let this distract you from the fact that in 1998, The Undertaker threw Mankind off Hell In A Cell, and plummeted 16 ft through an announcer’s table",
            f"{member.mention} tips his fedora too far and falls onto the tracks of an oncoming subway.",
            f"{member.mention} eats too much copypasta and explodes",
            f"{ctx.message.author.mention} kills {member.mention} with kindness",
            "no u",
            f"{ctx.message.author.mention} kills {member.mention} with a candlestick in the study",
            f"{member.mention} dies north of the wall and transforms into a white walker",
            f"{ctx.message.author.mention} thicc and collapses {member.mention}'s rib cage",
            f"{member.mention} loses the will to live",
            f"{member.mention} dies from dabbing too hard",
            f"{member.mention} died from a tragic amount of bad succ",
            f"{member.mention} dies by swearing on a Christian Minecraft server",
            f"{member.mention} died. OOF",
            f"{member.mention} died while listening to 'It's every day bro'",
            f"{member.mention} died while trying to find the city of England",
            f"{member.mention} died from a high salt intake",
            f"{member.mention} died due to {ctx.message.author.mention} being so stupid",
            f"{member.mention} died from reposting in the wrong neighborhood",
            f"{member.mention} died when testing a hydrogen bomb. There is nothing left to bury.",
            f"{member.mention} died from meme underdose :/",
            f"{member.mention} died after fapping 50 times in a row with no break.",
            f"{member.mention} dies from severe dislike of sand. It's coarse and rough and irritating it gets everywhere"]
        await ctx.send(f"{random.choice(responses)}")

    @command(name="embed", brief="Creates a custom embed.")
    async def create_embed(self, ctx, title, description, colour):
        '''Creates a custom embed.'''
        available_colours = ["red", "blue", "orange", "gold", "green", "purple", "silver", "black", None]
        if colour == colour in available_colours:
            if colour == "red":
                embed = Embed(title=title,
                            description=description,
                            colour=0xFF3E30)
                await ctx.send(embed=embed)
            if colour == "blue":
                embed = Embed(title=title,
                            description=description,
                            colour=0x3098FF)
                await ctx.send(embed=embed)
            if colour == "orange":
                embed = Embed(title=title,
                            description=description,
                            colour=0xFF8630)
                await ctx.send(embed=embed)
            if colour == "gold":
                embed = Embed(title=title,
                            description=description,
                            colour=0xFFD700)
                await ctx.send(embed=embed)
            if colour == "green":
                embed = Embed(title=title,
                            description=description,
                            colour=0x45FF4E)
                await ctx.send(embed=embed)
            if colour == "purple":
                embed = Embed(title=title,
                            description=description,
                            colour=0xE645FF)
                await ctx.send(embed=embed)
            if colour == "silver":
                embed = Embed(title=title,
                            description=description,
                            colour=0xC0C0C0)
                await ctx.send(embed=embed)
            if colour == "black":
                embed = Embed(title=title,
                            description=description,
                            colour=141414)
                await ctx.send(embed=embed)
            if colour is None:
                embed = Embed(title=title,
                            description=description)
                await ctx.send(embed=embed)

        else:
            await ctx.send("Unfortunately, that colour isn't available! However, you can head over to <#794958798325678142> and suggest it!")

    @Cog.listener()
    async def on_ready(self):
        print("Cog Ready: 'Fun'")

def setup(bot):
    bot.add_cog(Fun(bot))