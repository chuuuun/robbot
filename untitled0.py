#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 20:36:13 2021

@author: chuuun
"""
import discord
from discord.ext import commands

robbot=commands.Bot(command_prefix='!')
@robbot.event
async def on_ready():
    print('>>robbot is online<<')
robbot.run('ODg0Nzc2NzczMDMwNjcwMzk2.YTdalQ.JWll25v2bORYV5glFV3aQWzchks')
