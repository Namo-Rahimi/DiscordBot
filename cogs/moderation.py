from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Clean function removes messages
    @commands.command(aliases=["purge"])
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx, amount: int = 5):
        limit = 5
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Cleared by {ctx.author.mention}")
        await ctx.message.delete()
    
    # An error incase if a user tries to use it but don't have admin
    @clean.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title = "Clean error", description=f"You cannot use this {ctx.author.mention}", color=0xd62413)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
            await ctx.send(embed=embed)

    # Kick's the user from the server
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, user: discord.Member, *, reason="No reason provided"):
        userMessage = discord.Embed(description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        userMessage.set_author(name=f"Kicked {user.name}",icon_url=user.avatar_url)
        serverMessge = discord.Embed(description=f"Reason: {reason}\nBy: {ctx.author.mention}", color=0x0fb1d1)
        serverMessge.set_author(name=f"Kicked {user.name}",icon_url=user.avatar_url)
        serverMessge.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        await ctx.channel.send(embed=serverMessge)
        await user.send(embed=userMessage)
        await user.kick(reason=reason)

    # If a user uses it with no admin
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Kick error", description=f"You cannot use this {ctx.author.mention}", color=0xd62413)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
            await ctx.send(embed=embed)

    # Shows server bans
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def banlist(self, ctx):
        bans = await ctx.guild.bans()
        users = [f"User: {ban.user} ID : {ban[1].id}"for ban in bans ]
        list = "\n".join(users)
        embed = discord.Embed(title="Ban list", description=list, color=0x0fb1d1)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        await ctx.send(embed=embed)

    # If a user uses it but has no admin
    @banlist.error
    async def banlist_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Banlist error", description=f"You cannot use this {ctx.author.mention}", color=0xd62413)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
            await ctx.send(embed=embed)
    
    # Ban a use from the server
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, user: discord.Member, *, reason="No reason provided"):
        userMessage = discord.Embed(description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        userMessage.set_author(name=f"Banned {user.name}",icon_url=user.avatar_url)
        serverMessge = discord.Embed(description=f"Reason: {reason}\nBy: {ctx.author.mention}", color=0x0fb1d1)
        serverMessge.set_author(name=f"Banned {user.name}",icon_url=user.avatar_url)
        serverMessge.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        await ctx.channel.send(embed=serverMessge)
        await user.send(embed=userMessage)
        await user.ban(reason=reason)

    # If a user uses it with no admin
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Ban error", description=f"You cannot use this {ctx.author.mention}", color=0xd62413)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
            await ctx.send(embed=embed)

    # Unbans a user from the server
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                embed = discord.Embed(title="Unbanned", description=f"Unbanned {user.mention}", color=0x0fb1d1)
                embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
                await ctx.guild.unban(user)
                await ctx.send(embed=embed)
                return         

    # So a user with no admin can't unban other users
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Unban error", description=f"You cannot use this {ctx.author.mention}", color=0xd62413)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Moderation(bot))