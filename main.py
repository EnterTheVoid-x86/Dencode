# Dencode bot
# This bot is licensed under GNU GPLv3.
# More info can be found on the LICENSE file.
import discord
from discord.ext import commands
import base64

token = "your token here!"

status = "bytes of ascii into base64, binary, and more! Prefix is =."

bot = commands.Bot(command_prefix='=', help_command=None)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name = status))
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("```Command not found.```")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("```Missing required argument.```")
@bot.command()
async def encode64(ctx, *, message):
    await ctx.send("```Encoded output: " + base64.b64encode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def decode64(ctx, *, message):
    await ctx.send("```Decoded output: " + base64.b64decode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def encodebin(ctx, *, message):
    message = message.encode('utf-8').decode('utf-8')
    res = ''.join(format(ord(i), '08b') for i in message)
    await ctx.send("```Encoded output: " + res + "```")
@bot.command()
async def decodebin(ctx, *, message):
    message = message.encode('utf-8').decode('utf-8')
    res = ''.join(chr(int(message[i:i+8], 2)) for i in range(0, len(message), 8))
    await ctx.send("```Decoded output: " + res + "```")
@bot.command()
async def encodehex(ctx, *, message):
    message = message.encode('utf-8').decode('utf-8')
    res = ''.join(format(ord(i), '02x') for i in message)
    await ctx.send("```Encoded output: " + res + "```")
@bot.command()
async def decodehex(ctx, *, message):
    message = message.encode('utf-8').decode('utf-8')
    res = ''.join(chr(int(message[i:i+2], 16)) for i in range(0, len(message), 2))
    await ctx.send("```Decoded output: " + res + "```")
@bot.command()
async def experimentalencodeoct(ctx, *, message):
    message = message.encode('utf-8').decode('utf-8')
    res = ''.join(format(ord(i), '02o') for i in message)
    await ctx.send("```Encoded output: " + res + "```")
@bot.command()
async def experimentaldecodeoct(ctx, *, message):
    message = message.encode('utf-8').decode('utf-8')
    res = ''.join(chr(int(message[i:i+3], 8)) for i in range(0, len(message), 3))
    await ctx.send("```Decoded output: " + res + "```")
@bot.command()
async def encode32(ctx, *, message):
    await ctx.send("```Encoded output: " + base64.b32encode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def decode32(ctx, *, message):
    await ctx.send("```Decoded output: " + base64.b32decode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def encode16(ctx, *, message):
    await ctx.send("```Encoded output: " + base64.b16encode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def decode16(ctx, *, message):
    await ctx.send("```Decoded output: " + base64.b16decode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def encodea85(ctx, *, message):
    await ctx.send("```Encoded output: " + base64.a85encode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def decodea85(ctx, *, message):
    await ctx.send("```Decoded output: " + base64.a85decode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def info(ctx):
    await ctx.send("```This bot was made by @Nucleus#1922.\nThe source code can be found here: https://github.com/EnterTheVoid-x86/Dencode```")
@bot.command()
async def ping(ctx):
    await ctx.send("```Pong!```")
@bot.command()
async def help(ctx):
    await ctx.send("```Available commands:\n\n=encode64 <message>\n=decode64 <message>\n=encodebin <message>\n=decodebin <message>\n=encodehex <message>\n=decodehex <message>\n=experimentalencodeoct <message>\n=experimentaldecodeoct <message>\n=encode32 <message>\n=decode32 <message>\n=encode16 <message>\n=decode16 <message>\n=encodea85 <message>\n=decodea85 <message>\n=info\n=ping\n=help\n\nOctal encoding/decoding is experimental, and still has many bugs. For example,\nmessages encoded or decoded with spaces won't encode or decode properly.```")
bot.run(token)
