from discord.ext import commands
import discord


class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.remove_command("help")

    @commands.command()
    async def userinfo(self,ctx , user:discord.Member=None):
        if user == None:
            user = ctx.author

        embed = discord.Embed(title = f"User info - {user}", color=user.color)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name='ID:',value=user.id,inline=False)
        embed.add_field(name='Name:',value=user.display_name,inline=False)
        embed.add_field(name='Created at:',value=user.created_at,inline=False)
        embed.add_field(name='Joined at:',value=user.joined_at,inline=False)
        embed.add_field(name='Bot?',value=user.bot,inline=False)
        embed.add_field(name='Top Role:',value=user.top_role.mention,inline=False)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        await ctx.send(embed=embed)

    
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title = "Help")
        embed.add_field(name='Animals',value=f".cats shows random cat pics\n.dogs show random dog pics",inline=False)
        embed.add_field(name='Cryptocurrency',value=f".price CRYPTONAME for example .price BTC",inline=False)
        embed.add_field(name='Memes',value=f".memes to show a random meme",inline=False)
        embed.add_field(name='Moderation',value=f".kick @user to kick a user\n.ban @user to ban a user\n.banlist to show the banlist\n.unban User#1234 to unban a user",inline=False)
        embed.add_field(name='Tools',value=f".userinfo @name to show info on a user\n.help to show this command",inline=True)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Tools(bot))