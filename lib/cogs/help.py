from apscheduler.triggers.cron import CronTrigger
from discord import Embed, colour, embeds
from typing import Optional
from discord.utils import get
from discord.ext.menus import MenuPages, ListPageSource
from discord.ext.commands import Cog
from discord.ext.commands import command

def syntax(command):
    cmd_and_aliases = "|".join([str(command), *command.aliases])
    params = []
    
    for key, value in command.params.items():
        if key not in ("self", "ctx"):
            params.append(f"[{key}]" if "NoneType" in str(value) else f"<{key}>")

    params = " ".join(params)

    return f"```{cmd_and_aliases} {params}```"

class HelpMenu(ListPageSource):
    def __init__(self, ctx, data):
        self.ctx = ctx
        self.primary_colour = 0xC0C0C0

        super().__init__(data, per_page=5)

    async def write_page(self, menu, fields=[]):
        offset = (menu.current_page*self.per_page) + 1
        len_data = len(self.entries)

        embed = Embed(title="Help",
                      description="Welcome to Smiler Pro help!",
                      colour=self.primary_colour)
        embed.set_thumbnail(url=self.ctx.guild.me.avatar_url)
        embed.set_footer(text=f"{offset:,} - {min(len_data, offset+self.per_page-1):,} of {len_data:,} commands.")

        for name, value in fields:
            embed.add_field(name=name, value=value, inline=False)

        return embed

    async def format_page(self, menu, entries):
        fields = []

        for entry in entries:
            fields.append((entry.brief or "No description.", syntax(entry)))

        return await self.write_page(menu, fields)

class Help(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")
        self.primary_colour = 0xC0C0C0

    async def cmd_help(self, ctx, command):
        embed = Embed(title=f"Help with `{command}`.",
                      description=syntax(command),
                      colour=self.primary_colour)
        embed.add_field(name="Command Description", value=command.help)
        await ctx.send(embed=embed)
    
    @command(name="help", brief="Shows this message.")
    async def show_help(self, ctx, cmd: Optional[str]):
        '''Shows this message.'''
        await ctx.message.delete()
        if cmd is None:
            menu = MenuPages(source=HelpMenu(ctx, list(self.bot.commands)),
                             delete_message_after=True,
                             clear_reactions_after=True,
                             timeout=60.0)
            await menu.start(ctx)                

        else:
            if (command := get(self.bot.commands, name=cmd)):
                await self.cmd_help(ctx, command)

            else:
                await ctx.send("That command could not be found! Please check if the command you are looking for is valid, and try again.")

    @command(name="info", aliases=["information"], brief="Gives information about Smiler Pro.")
    async def information(self, ctx):
        '''Gives information about Smiler Pro.'''
        await ctx.message.delete()
        embed = Embed(title="The ultimate all-purpose Discord bot.", description="Make your server a better place!", 
                        colour=self.primary_colour)
        fields = [("What Can I Do?", "- Pokemon Battle\n- Polls & Quizzes\n- Everything Smiler Can", True),
                    ("What Can't I Do?", "- Steal Personal Data\n- Run Skynet.exe\n- Hack Into The Matrix", True),
                    ("Contribute to me!", "1. Support my creators at `https://www.patreon.com/beepboopstudio`\n2. Join the team at `https://www.studiobeepboop.com/`", False)
                    ]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        embed.set_footer(text="Copyright© 2020 Beep Boop Studio. All Rights Reserved.")
        embed.set_author(name="Smiler Pro", icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @command(name="ping", brief="Shows bot ping.")
    async def show_ping(self, ctx):
        '''Shows bot ping.'''
        await ctx.send(f"Ping `{round(self.bot.latency * 1000)}ms`")

    @command(name="support", aliases=["donate"], brief="Helps you to support Beep Boop Studios.")
    async def support(self, ctx):
        '''Helps you to support Beep Boop Studios.'''
        embed = Embed(title="Hmmm? Another supporter? Very well, may the ritual commence!",
                      description="Support Beep Boop Studios At `https://www.patreon.com/beepboopstudio`!",
                      colour=self.primary_colour)
        embed.set_author(name="Smiler Pro", icon_url=self.bot.user.avatar_url)
        embed.set_footer(text="Copyright © 2020 Beep Boop Studio. All Rights Reserved.")
        await ctx.send(embed=embed)

    @command(name="invite", aliases=["inv"], brief="Creates an invite link for our services.")
    async def gen_invite(self, ctx, item):
        '''Creates an invite link for our services.'''
        if item == "server":
            invite = await ctx.channel.create_invite()
            await ctx.send(f"Invite Created: {invite}")
        if item == "bot":
            embed = Embed(title="Invite For Smiler Pro",
                                    description="https://discord.com/oauth2/authorize?client_id=786922640848977921&permissions=8&redirect_uri=https%3A%2F%2Fstudiobeepboop.com&scope=bot",
                                    colour=self.primary_colour)
            embed.set_author(name="Smiler Pro", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text="Copyright© 2020 Beep Boop Studio. All Rights Reserved.")
            await ctx.send(embed=embed)
        if item == "supportserver":
            embed = Embed(title="Invite To Beep Boop Studio's Server",
                                    description="https://discord.gg/DEwA8pdQnX",
                                    colour=self.primary_colour)
            embed.set_author(name="Smiler Pro", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text="Copyright © 2020 Beep Boop Studio. All Rights Reserved.")
            await ctx.send(embed=embed)

    @command(name="status", aliases=["stat"], brief="Displays bot status.")
    async def show_status(self, ctx):
        '''Displays bot status.'''
        await ctx.message.delete()
        embed = Embed(title="Bot Status",
                      colour=self.primary_colour)
        embed.add_field(name="Watching:", value=f"{len(self.bot.guilds)} Servers", inline=False)
        embed.add_field(name="Ping:", value=f"{round(self.bot.latency * 1000)}ms", inline=False)
        embed.set_author(name="Smiler Pro", icon_url=self.bot.user.avatar_url)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        print("Cog Ready: 'Help'")

def setup(bot):
    bot.add_cog(Help(bot))