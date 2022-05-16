import discord
from discord.ext import commands
from datetime import datetime
from discord_slash import SlashCommand
from discord_slash.utils import manage_commands
import math
import numbers
import re

date = datetime.now()
now = date.strftime("%H:%M:%S")
client = discord.Client()
slash = SlashCommand(client, auto_register=True, auto_delete = True)

guild_ids = [803639880391065623]

@client.event
async def on_ready():
    print(f"[{now}] Bot turned on")

@slash.slash(name="ping", description="Shows QuickCal's latency", guild_ids=guild_ids)
async def _ping(ctx):
    await ctx.send(hidden=True, content=f"Pong! ({round(client.latency*1000)}ms)")

@slash.slash(
  name="add",
  description="Add to numbers up",
  options=[manage_commands.create_option(
    name = "number_1",
    description = "The first number",
    option_type = 3,
    required = True
    ),
  manage_commands.create_option(
    name = "number_2",
    description = "The second number",
    option_type = 3,
    required = True
  ),
  manage_commands.create_option(
    name = "number_3",
    description = "The third number",
    option_type = 3,
    required = False
  )],

  guild_ids=guild_ids)
async def _add(ctx, num1, num2, num3=0):
    if num3:
        extra = f"+{num3}"
    else:
        extra = "+0"
        num3 = "0"
    if ',' in num1:
        num1 = num1.replace(",", ".")
        info = f"""<:Warning:803892226774007838> First number: A comma was given (`,`) but I only use dots (`.`)! Your new sum is now:
`{num1}+{num2}{extra}`"""

    if ',' in num2:
        num2 = num2.replace(",", ".")
        info = f"""<:Warning:803892226774007838> Second number: A comma was given (`,`) but I only use dots (`.`)! Your new sum is now:
`{num1}+{num2}{extra}`"""

    if ',' in num3:
        num3 = num3.replace(",", ".")
        extra = f"+{num3}"
        info = f"""<:Warning:803892226774007838> Third number: A comma was given (`,`) but I only use dots (`.`)! Your new sum is now:
`{num1}+{num2}{extra}`"""

    try:
        info
    except NameError:
        info = "No errors or alerts!"
    try:
        tmp = float(num1)
        await ctx.send(hidden=True, content=f"""
**{num1}+{num2}{extra}={float(num1) + float(num2) + float(num3)}**

<:Information:803899332797005825> If you have nothing as a third number, it automatically adds a `0` to your sum. This is because of limitatations
{info}""")
    except:
        await ctx.send(hidden=True, content=f"`{num1} + {num2} + {num3}` is a invalid sum.")


client.run("ODAzNjM4NjIzMDA5NTA1Mjgw.YBAsyg.h7Y8Got4ZPa1ud37p8cFaz4_bQ")
