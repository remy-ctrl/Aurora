import discord
import inspect
from discord.ext import commands

class Secret(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """ - Command which Loads a Module."""
        try:
            self.client.load_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'{type(e).__name__} - {e}')
        else:
            await ctx.send(f'You have successfully loaded the cog: `{cog}`')


    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        """ - Command which Unloads a Module."""
        try:
            self.client.unload_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'{type(e).__name__} - {e}')
        else:
            await ctx.send(f'You have successfully unloaded the cog: `{cog}`')

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        """ - Command which Reloads a Module."""
        try:
            self.client.unload_extension(f'cogs.{cog}')
            self.client.load_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'{type(e).__name__} - {e}')
        else:
            await ctx.send(f'You have successfully reloaded the cog: `{cog}`')
    
    
    @commands.command()
    @commands.is_owner()
    async def eval(self, ctx, *, command):
        """ - Evaluates code."""
        res = eval(command)
        if inspect.isawaitable(res):
            await ctx.send(await res)
        else:
            await ctx.send(res)


def setup(client):
    client.add_cog(Secret(client))