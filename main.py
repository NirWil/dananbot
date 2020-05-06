import discord
from discord.ext import commands
import random
import os
import asyncio
import time`

prefix = "danan!"
dclient = discord.Client()
client = commands.Bot(description="danan", command_prefix=prefix)
sleep = time.sleep


@client.command(pass_context=True)
async def say(ctx):
    msg = ctx.message.content.split(" ", 1)
    await client.delete_message(ctx.message)
    await client.send_message(ctx.message.channel, msg)
