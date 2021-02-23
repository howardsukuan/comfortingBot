#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import discord
from comforting_bot_for_loki import Result as comforting
from account_info import accountInfoDICT

DISCORD_TOKEN=accountInfoDICT["DISCORD_TOKEN"]
DISCORD_GUILD=accountInfoDICT["DISCORD_GUILD"]
BOT_NAME = "dear_tree_hole"

# Documention
# https://discordpy.readthedocs.io/en/latest/api.html#client

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == DISCORD_GUILD:
            break
    print(f'{BOT_NAME}bot has connected to Discord!')
    print(f'{guild.name}(id:{guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    print(client.user.id)
    print(message.content)
    if "<@&807931892573798441>" in message.content:
        if "hi" in message.content:
            response = "哈囉，今天好嗎~"
            await message.channel.send(response)
    #如何有順序的回應? 第一回應跑特定function 第二個回應跑另一個function
        else:
            msgSTR = message.content.replace("<@!{}> ".format(client.user.id), "")
            response = comforting(msgSTR)
            await message.channel.send(response)
            
    


client.run(DISCORD_TOKEN)
