import os
import discord
from discord.ext import commands
from pkg.utils import intdiv, plus, minus, multi, intdiv, moddiv, get_time

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    ready_channel_id = int(os.getenv('READY_CHANNEL'))
    channel = discord.utils.get(bot.get_all_channels(), id=ready_channel_id)
    await channel.send(f'{get_time()} | {bot.user} | Ready!')

@bot.command(name='plus')
async def cmd_plus(ctx, a: int, b: int):
    await ctx.send(f'{a} + {b} = {plus(a, b)}')

@bot.command(name='minus')
async def cmd_minus(ctx, a: int, b: int):
    await ctx.send(f'{a} - {b} = {minus(a, b)}')

@bot.command(name='multi')
async def cmd_multi(ctx, a: int, b: int):
    await ctx.send(f'{a} * {b} = {multi(a, b)}')

@bot.command(name='intdiv')
async def cmd_intdiv(ctx, a: int, b: int):
    await ctx.send(f'{a} // {b} = {intdiv(a, b)}')

@bot.command(name='moddiv')
async def cmd_moddiv(ctx, a: int, b: int):
    await ctx.send(f'{a} % {b} = {moddiv(a, b)}')

if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))
