# Dencode bot
# This bot is licensed under GNU GPLv3.
# More info can be found on the LICENSE file.
import discord
from discord.ext import commands
import base64

token = "your token here!"

status = "bytes of ascii into base64, binary, and more!"

bot = commands.Bot(command_prefix='=')



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name = status))
@bot.command()
async def encode64(ctx, *, message):
    """Encode a message to base64"""
    await ctx.send("```Encoded output: " + base64.b64encode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def decode64(ctx, *, message):
    """Decode a message from base64"""
    await ctx.send("```Decoded output: " + base64.b64decode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def encodebin(ctx, *, message):
    """Encode a message to binary"""
    message = message.encode('utf-8').decode('utf-8')
    res = ''.join(format(ord(i), '08b') for i in message)
    await ctx.send("```Encoded output: " + res + "```")
@bot.command()
async def decodebin(ctx, *, message):
    """Decode a message from binary"""
    message = message.encode('utf-8').decode('utf-8')
    res = ''.join(chr(int(message[i:i+8], 2)) for i in range(0, len(message), 8))
    await ctx.send("```Decoded output: " + res + "```")
@bot.command()
async def encodehex(ctx, *, message):
    """Encode a message to hex"""
    message = message.encode('utf-8').decode('utf-8')
    res = ''.join(format(ord(i), '02x') for i in message)
    await ctx.send("```Encoded output: " + res + "```")
@bot.command()
async def decodehex(ctx, *, message):
    """Decode a message from hex"""
    message = message.encode('utf-8').decode('utf-8')
    res = ''.join(chr(int(message[i:i+2], 16)) for i in range(0, len(message), 2))
    await ctx.send("```Decoded output: " + res + "```")
@bot.command()
async def info(ctx):
    """Info about the bot"""
    await ctx.send("```This bot was made by @Nucleus#1922.\nThe source code can be found here: https://github.com/EnterTheVoidx86/dencode```")
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("```Command not found.```")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("```Missing required argument.```")
bot.run(token)
