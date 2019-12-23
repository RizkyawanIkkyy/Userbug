# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# You can find misc modules, which dont fit in anything xD
""" Userbot module for other small commands. """

from random import randint
from asyncio import sleep
from os import execl
import sys
import os
import io
import sys
import json
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import register

@register(outgoing=True, pattern="^!krypton$")
async def shalom(e):
    await e.edit(
        "\n▄▄   ▄▄▄"
        "\n██  ██▀"
        "\n██▄██"
        "\n█████"
        "\n██  ██▄"
        "\n██   ██▄"
        "\n▀▀    ▀▀"
        "\n"
        "\n _ __"
        "\n| '__|"
        "\n| |"
        "\n|_|"
        "\n"
        "\n _   _"
        "\n| | | |"
        "\n| |_| |"
        "\n \__, |"
        "\n |___/"
        "\n"
        "\n ____"
        "\n|  _ \"
        "\n| |_) |"
        "\n|  __/"
        "\n|_|"
        "\n"
        "\n _"
        "\n| |_"
        "\n| __|"
        "\n| |_"
        "\n \__|"
        "\n"
        "\n  ___"
        "\n / _ \"
        "\n| (_) |"
        "\n \___/"
        "\n"
        "\n _   _"
        "\n| \ | |"
        "\n|  \| |"
        "\n| |\  |"
        "\n|_| \_|")
        
    
    CMD_HELP.update({
    'krypton':
    '.krypton\
\nUsage: gives a nice KryPtoN as output😂.'
})




