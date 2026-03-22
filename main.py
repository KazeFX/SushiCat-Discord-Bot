import discord
import array
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello! SushiCatBot is ready! o7")

@bot.command()
async def hello(ctx):
    await ctx.send('Well, hello there!')

@bot.command()
async def hi(ctx):
    await ctx.send('Well, hello there!')

@bot.command()
async def add(ctx, *arr):
    result = 0
    for i in arr:
        result += int(i)

    await ctx.send(str(result))

@bot.command()
async def d20(ctx):
    channel2 = bot.get_channel(CHANNEL_ID2)
    result = random.randint(1, 20)
    if result == 20:
        await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled a natural **{result}** !!!")
    elif result == 1:
        await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled a natural **{result}**.. :(")
    else:
        await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled **{result}** !")

@bot.command()
async def d12(ctx):
    channel2 = bot.get_channel(CHANNEL_ID2)
    result = random.randint(1, 12)
    if result == 12:
        await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled a natural **{result}** !!!")
    elif result == 1:
        await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled a natural **{result}**.. :(")
    else:
        await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled **{result}** !")

@bot.command()
async def d00(ctx):
    channel2 = bot.get_channel(CHANNEL_ID2)
    numberless = array.array('i', [00, 10, 20, 30, 40, 50, 60, 70, 80, 90])
    random.shuffle(numberless)
    singleperc = random.randint(0, 9)
    if numberless[0] == 00 and singleperc == 0:
        await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled **100%** !!!")
    elif numberless[0] == 00 and singleperc > 0:
        await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled **{singleperc}** !")
    else:
        await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled **{numberless[0] + singleperc}%** !")

@bot.command()
async def d10(ctx):
    channel2 = bot.get_channel(CHANNEL_ID2)
    result = random.randint(0, 9)
    await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled **{result}** !")

@bot.command()
async def d8(ctx):
    channel2 = bot.get_channel(CHANNEL_ID2)
    result = random.randint(1, 8)
    if result == 8:
        await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled a natural **{result}** !!!")
    elif result == 1:
        await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled a natural **{result}**.. :(")
    else:
        await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled **{result}** !")

@bot.command()
async def d6(ctx):
    channel2 = bot.get_channel(CHANNEL_ID2)
    result = random.randint(1, 6)
    if result == 6:
        await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled a natural **{result}** !!!")
    elif result == 1:
        await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled a natural **{result}**.. :(")
    else:
        await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled **{result}** !")

@bot.command()
async def d4(ctx):
    channel2 = bot.get_channel(CHANNEL_ID2)
    result = random.randint(1, 4)
    if result == 4:
        await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled a natural **{result}** !!!")
    elif result == 1:
        await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled a natural **{result}**.. :(")
    else:
        await channel2.send(f"ᕕ( ᐛ )ᕗ You rolled **{result}** !")

bot.run(BOT_TOKEN)
