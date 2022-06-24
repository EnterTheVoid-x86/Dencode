# Dencode bot
# This bot is licensed under GNU GPLv3.
# More info can be found on the LICENSE file.
import discord
from discord.ext import commands
import base64
import datetime
import os
import string

token = "your token here!"

status = "bytes of ascii into base64, binary, and more! Prefix is =."

botver = "1.4"

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
    if isinstance(error, commands.TooManyArguments):
        await ctx.send("```Too many arguments.```")
@bot.command()
async def debugrebootdontuse(ctx):
    await ctx.send("```Rebooting...```")
    os.system("taskkill /f /im py.exe && py main.py")
@bot.command()
async def encode64(ctx, *, message):
    print("[ENCODE64] " + str(datetime.datetime.now()))
    await ctx.send("```Encoded output: " + base64.b64encode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def decode64(ctx, *, message):
    print("[DECODE64] " + str(datetime.datetime.now()))
    await ctx.send("```Decoded output: " + base64.b64decode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def encodebin(ctx, *, message):
    print("[ENCODEBIN] " + str(datetime.datetime.now()))
    message = message.encode('utf-8').decode('utf-8')
    res = ''.join(format(ord(i), '08b') for i in message)
    await ctx.send("```Encoded output: " + res + "```")
@bot.command()
async def decodebin(ctx, *, message):
    print("[DECODEBIN] " + str(datetime.datetime.now()))
    message = message.encode('utf-8').decode('utf-8')
    res = ''.join(chr(int(message[i:i+8], 2)) for i in range(0, len(message), 8))
    await ctx.send("```Decoded output: " + res + "```")
@bot.command()
async def encodehex(ctx, *, message):
    print("[ENCODEHEX] " + str(datetime.datetime.now()))
    message = message.encode('utf-8').decode('utf-8')
    res = ''.join(format(ord(i), '02x') for i in message)
    await ctx.send("```Encoded output: " + res + "```")
@bot.command()
async def decodehex(ctx, *, message):
    print("[DECODEHEX] " + str(datetime.datetime.now()))
    message = message.encode('utf-8').decode('utf-8')
    res = ''.join(chr(int(message[i:i+2], 16)) for i in range(0, len(message), 2))
    await ctx.send("```Decoded output: " + res + "```")
@bot.command()
async def experimentalencodeoct(ctx, *, message):
    print("[ENCODEOCT] " + str(datetime.datetime.now()))
    message = message.encode('utf-8').decode('utf-8')
    res = ''.join(format(ord(i), '02o') for i in message)
    await ctx.send("```Encoded output: " + res + "```")
@bot.command()
async def experimentaldecodeoct(ctx, *, message):
    print("[DECODEOCT] " + str(datetime.datetime.now()))
    message = message.encode('utf-8').decode('utf-8')
    res = ''.join(chr(int(message[i:i+3], 8)) for i in range(0, len(message), 3))
    await ctx.send("```Decoded output: " + res + "```")
@bot.command()
async def encode32(ctx, *, message):
    print("[ENCODE32] " + str(datetime.datetime.now()))
    await ctx.send("```Encoded output: " + base64.b32encode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def decode32(ctx, *, message):
    print("[DECODE32] " + str(datetime.datetime.now()))
    await ctx.send("```Decoded output: " + base64.b32decode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def encode16(ctx, *, message):
    print("[ENCODE16] " + str(datetime.datetime.now()))
    await ctx.send("```Encoded output: " + base64.b16encode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def decode16(ctx, *, message):
    print("[DECODE16] " + str(datetime.datetime.now()))
    await ctx.send("```Decoded output: " + base64.b16decode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def encodea85(ctx, *, message):
    print("[ENCODEA85] " + str(datetime.datetime.now()))
    await ctx.send("```Encoded output: " + base64.a85encode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def decodea85(ctx, *, message):
    print("[DECODEA85] " + str(datetime.datetime.now()))
    await ctx.send("```Decoded output: " + base64.a85decode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def encode85(ctx, *, message):
    print("[ENCODE85] " + str(datetime.datetime.now()))
    await ctx.send("```Encoded output: " + base64.b85encode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def decode85(ctx, *, message):
    print("[DECODE85] " + str(datetime.datetime.now()))
    await ctx.send("```Decoded output: " + base64.b85decode(message.encode('utf-8')).decode('utf-8') + "```")
@bot.command()
async def encodenum(ctx, *, message):
    num_list = [ord(x) - 96 for x in message]
    print("[ENCODENUM] " + str(datetime.datetime.now()))
    await ctx.send("```Encoded output: " + str(num_list) + "```")
@bot.command()
async def decodenum(ctx):
    print("[DECODENUM] " + str(datetime.datetime.now()))
    await ctx.send("```Not yet supported!```")
@bot.command()
async def info(ctx):
    print("[INFO] " + str(datetime.datetime.now()))
    await ctx.send("```This bot was made by @Nucleus#1922.\nThe source code can be found here: https://github.com/EnterTheVoid-x86/Dencode```")
@bot.command()
async def ping(ctx):
    print("[PING] " + str(datetime.datetime.now()))
    await ctx.send("```Pong!```")
@bot.command()
async def version(ctx):
    print("[VERSION] " + str(datetime.datetime.now()))
    await ctx.send("```Version: " + botver + "```")
@bot.command()
async def help(ctx):
    print("[HELP] " + str(datetime.datetime.now()))
    await ctx.send("```Available commands:\n\n=encode64 <message>\n=decode64 <message>\n=encodebin <message>\n=decodebin <message>\n=encodehex <message>\n=decodehex <message>\n=experimentalencodeoct <message>\n=experimentaldecodeoct <message>\n=encode32 <message>\n=decode32 <message>\n=encode16 <message>\n=decode16 <message>\n=encodea85 <message>\n=decodea85 <message>\n=encode85 <message>\n=decode85\n=encodenum <message>\n=decodenum <message>\n=info\n=ping\n=help\n\nOctal encoding/decoding is experimental, and still has many bugs. For example,\nmessages encoded or decoded with spaces won't encode or decode properly.```")
bot.run(token)
