from discord.ext import commands

class Animals:
    def __init__(self):
        self.bot = bot

    @commands.command()
    async def dog(self, ctx):
        await ctx.send("Dog")

def setup(bot):
    bot.add_cog(Animals(bot))