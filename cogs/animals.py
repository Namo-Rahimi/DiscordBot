from discord.ext import commands
import requests
import discord

class Animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Gets a random image of a dog
    @commands.command(aliases=["dog"])
    async def dogs(self, ctx):
        dog = requests.get("https://dog.ceo/api/breeds/image/random").json()
        embed = discord.Embed(title="Dogs", color=0x42f55a)
        dogImage = dog["message"]
        embed.set_image(url=dogImage)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        await ctx.send(embed=embed)
     
    # Gets a random image of a cat
    @commands.command(aliases=["cat"])
    async def cats(self, ctx):
        cat = requests.get("https://api.thecatapi.com/v1/images/search?beng&include_breeds=true").json()
        catImage = cat[0]["url"]
        embed = discord.Embed(title="Cats", color=0xe35927)
        image = embed.set_image(url=catImage)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        await ctx.send(embed=embed)

# Sets up the cog
def setup(bot):
    bot.add_cog(Animals(bot))