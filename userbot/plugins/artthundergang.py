import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


n = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.hacker$")
@borg.on(admin_cmd(pattern=r"hacker"))
async def thunderganghacker(hacker):
    await hacker.edit(n + "             \n"
"─────█─▄▀█──█▀▄─█─────\n"
"────▐▌──────────▐▌────\n"
"────█▌▀▄──▄▄──▄▀▐█────\n"
"───▐██──▀▀──▀▀──██▌───\n"
"──▄████▄──▐▌──▄████▄──\n")


Q = ("───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n"
"───█▒▒░░░░░░░░░▒▒█───\n"
"────█░░█░░░░░█░░█────\n"
"─▄▄──█░░░▀█▀░░░█──▄▄─\n"
"█░░█─▀▄░░░░░░░▄▀─█░░█\n")

W = ("──────▄▀▄─────▄▀▄\n"
"─────▄█░░▀▀▀▀▀░░█▄\n"
"─▄▄──█░░░░░░░░░░░█──▄▄\n"
"█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█\n")

E = ("▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒\n"
"▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒\n"
"▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒\n"
"▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒\n"
"▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒\n")

R = ("░▄▄▄▄░\n"
"▀▀▄██►\n"
"▀▀███►\n"
"░▀███►░█►\n"
"▒▄████▀▀\n")

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

P = ("───▄█▌─▄─▄─▐█▄\n"
"───██▌▀▀▄▀▀▐██\n"
"───██▌─▄▄▄─▐██\n"
"───▀██▌▐█▌▐██▀\n"
"▄██████─▀─██████▄\n")

A = ("░░░░░░░▄█▄▄▄█▄\n"
"▄▀░░░░▄▌─▄─▄─▐▄░░░░▀▄\n"
"█▄▄█░░▀▌─▀─▀─▐▀░░█▄▄█\n"
"░▐▌░░░░▀▀███▀▀░░░░▐▌\n"
"████░▄█████████▄░████\n")

S = ("▄▄▀█▄───▄───────▄\n"
"▀▀▀██──███─────███\n"
"░▄██▀░█████░░░█████░░\n"
"███▀▄███░███░███░███░▄\n"
"▀█████▀░░░▀███▀░░░▀██▀\n")

D = ("╔══╗░░░░╔╦╗░░╔═════╗\n"
"║╚═╬════╬╣╠═╗║░▀░▀░║\n"
"╠═╗║╔╗╔╗║║║╩╣║╚═══╝║\n"
"╚══╩╝╚╝╚╩╩╩═╝╚═════╝\n")
F = ("───────███\n"
"───────███\n"
"▄█████▄█▀▀\n"
"─▀█████\n"
"──▄████▄\n")

G = ("▄█▀─▄▄▄▄▄▄▄─▀█▄\n"
"▀█████████████▀\n"
"────█▄███▄█\n"
"─────█████\n"
"─────█▀█▀█\n")



@borg.on(admin_cmd(pattern=r"teddy"))
async def thundergangteddy(teddy):
    await teddy.edit(Q)
@borg.on(admin_cmd(pattern=r"cat"))
async def thundergangcat(cat):
    await cat.edit(W)
@borg.on(admin_cmd(pattern=r"alien"))
async def thundergangalien(alien):
    await alien.edit(E)	
@borg.on(admin_cmd(pattern=r"dinosaur"))
async def thundergangdinosaur(dinosaur):
    await dinosaur.edit(R)
@borg.on(admin_cmd(pattern=r"welcome"))
async def thundergangwelcome(welcome):
    await welcome.edit(T)
@borg.on(admin_cmd(pattern=r"drink"))
async def thundergangdrink(drink):
    await drink.edit(Y)
@borg.on(admin_cmd(pattern=r"bomb"))
async def thundergangbomb(bomb):
    await bomb.edit(U)
@borg.on(admin_cmd(pattern=r"bike"))
async def thundergangbike(bike):
    await bike.edit(I)
@borg.on(admin_cmd(pattern=r"goodnight"))
async def thunderganggoodnight(goodnight):
    await goodnight.edit(O)
@borg.on(admin_cmd(pattern=r"devil"))
async def thundergangdevil(devil):
    await devil.edit(P)
@borg.on(admin_cmd(pattern=r"robot"))
async def thundergangrobot(robot):
    await robot.edit(A)
@borg.on(admin_cmd(pattern=r"boa"))
async def thundergangboa(boa):
    await boa.edit(S)
@borg.on(admin_cmd(pattern=r"smile"))
async def thundergangsmile(smile):
    await smile.edit(D)
@borg.on(admin_cmd(pattern=r"toilet"))
async def thundergangtoilet(toilet):
    await toilet.edit(F)
@borg.on(admin_cmd(pattern=r"bull"))
async def thundergangbull(bull):
    await bull.edit(G)
