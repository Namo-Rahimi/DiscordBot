from discord.ext import commands
import discord
import requests

class Cryptocurreny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Get's the price of a cryptocurrency
    @commands.command()
    async def price(self, ctx, crypto = ""):
        if crypto == "":
            crypto = "BTC"
            site = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={crypto}&tsyms=EUR").json()
            embed = discord.Embed(title=f"{crypto} price", description=f"Current Price: €{site}", color=0xebe72f)

        site = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={crypto}&tsyms=EUR").json()
        embed = discord.Embed(title = f"{crypto} price", description=f'Current Price: €{site["EUR"]}\nTry adding a crypto next to the command for example .price XMR', color=0xebe72f)
        
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        await ctx.send(embed=embed)

    
def setup(bot):
    bot.add_cog(Cryptocurreny(bot))