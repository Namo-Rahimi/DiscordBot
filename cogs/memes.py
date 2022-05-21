from discord.ext import commands
import discord
import requests

class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["meme"])
    async def memes(self, ctx):
        meme = requests.get("https://meme-api.herokuapp.com/gimme").json()
        embed = discord.Embed(title=f"{meme['title']}", color=0x7FFF00)
        image = embed.set_image(url=meme["url"])
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Memes(bot))