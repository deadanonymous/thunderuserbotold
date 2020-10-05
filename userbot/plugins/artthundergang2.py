"""Plugin made by Thundergang for ThunderUserbot 
and if you will copy it without credits then you are the biggest gay of this universe"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot.utils import admin_cmd

T = ("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
"█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
"█░░║║║╠─║─║─║║║║║╠─░░█\n"
"█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
"█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
Y = ("──────▄▀─\n"
"─█▀▀▀█▀█─\n"
"──▀▄░▄▀──\n"
"────█────\n"
"──▄▄█▄▄──\n")
U = ("─▄▀▀███═◯\n"
"▐▌▄▀▀█▀▀▄\n"
"█▐▌─────▐▌\n"
"█▐█▄───▄█▌\n"
"▀─▀██▄██▀\n")
I = ("───────────▀▄\n"
"──█▄▄▄▄▄███▀▄─▄▄\n"
"▄▀──▀▄─▀▀█▀▀▄▀──▀▄\n"
"▀▄▀▀█▀▀████─▀▄──▄▀\n"
"──▀▀──────────▀▀\n")
O = ("O────────────────O\n"
"█▓██▄────────────█\n"
"█▓▓░▀▄▀░░░░░░░░░░█\n"
"█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
"█────────────────█\n")

@borg.on(admin_cmd(pattern=r"welcome"))
async def nandywelcome(welcome):
    await welcome.edit(T)
@borg.on(admin_cmd(pattern=r"drink"))
async def nandydrink(drink):
    await drink.edit(Y)
@borg.on(admin_cmd(pattern=r"bomb"))
async def nandybomb(bomb):
    await bomb.edit(U)
@borg.on(admin_cmd(pattern=r"bike"))
async def nandybike(bike):
    await bike.edit(I)
@borg.on(admin_cmd(pattern=r"goodnight"))
async def nandygoodnight(goodnight):
    await goodnight.edit(O)