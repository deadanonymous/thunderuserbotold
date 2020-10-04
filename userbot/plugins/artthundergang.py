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

H = ("───▄▄─▄████▄▐▄▄▄▌\n"
"──▐──████▀███▄█▄▌\n"
"▐─▌──█▀▌──▐▀▌▀█▀\n"
"─▀───▌─▌──▐─▌\n"
"─────█─█──▐▌█\n")

J = ("──▄──▄────▄▀\n"
"───▀▄─█─▄▀▄▄▄\n"
"▄██▄████▄██▄▀█▄\n"
"─▀▀─█▀█▀▄▀███▀\n"
"──▄▄▀─█──▀▄▄\n")

K = ("░╔╔╩╩╝\n"
"▄██▄\n"
"░░██████▄░░░░░░▄▄▄▄▄▄█\n"
"░░█▀█▀█▀█░░▄░▄████████\n"
"░▄▌▄▌▄▌▄▌░▀▄▄▄▄█▄▄▄▄█▄\n")

L = ("█───▄▀▀▀▀▄─▐█▌▐█▌▐██\n"
"█──▐▄▄────▌─█▌▐█─▐▌─\n"
"█──▐█▀█─▀─▌─█▌▐█─▐██\n"
"█──▐████▄▄▌─▐▌▐▌─▐▌─\n"
"███─▀████▀───██──▐██\n")


Z = ("░▄░█░░░▄▀▀▀▀▀▄░░░█░▄░\n"
"▄▄▀▄░░░█─▀─▀─█░░░▄▀▄▄\n"
"░░░░▀▄▒▒▒▒▒▒▒▒▒▄▀░░░░\n"
"░░░░░█────▀────█░░░░░\n"
"░░░░░█────▀────█░░░░░\n")

X = ("░░░░░░░░░░░░░░░░▄▓▄\n"
"░░░░▄█▄░░░░░░░░▄▓▓▓▄\n"
"░░▄█████▄░░░░░▄▓▓▓▓▓▄\n"
"░▀██┼█┼██▀░░░▄▓▓▓▓▓▓▓▄\n"
"▄▄███████▄▄▄▄▄▄▄▄█▄▄▄▄\n")

C = ("░▄▀▀▀▀▄░░▄▄\n"
"█░░░░░░▀▀░░█░░░░░░▄░▄\n"
"█░║░░░░██░████████████ \n"
"█░░░░░░▄▄░░█░░░░░░▀░▀\n"
"░▀▄▄▄▄▀░░▀▀\n")

V = ("░▄▌░░░░░░░░░▄\n"
"████████████▄\n"
"░░░░░░░░▀▐████\n"
"░░░░░░░░░░░▐██▌\n")

B = ("─────▀▄▀─────▄─────▄\n"
"──▄███████▄──▀██▄██▀\n"
"▄█████▀█████▄──▄█\n"
"███████▀████████▀\n"
"─▄▄▄▄▄▄███████▀\n")


N = ("▄▀─────────────▀▄\n"
"█▄█──█▀█─█▀█─▄█▄█\n"
"─▀██▄▀▄▀─▀▄▀▄██▀\n"
"░░░▄██▀███▀███▄\n"
"░▐▀█▀██▄▄▄██▀█▀▌\n")

M = ("║░█░█░║░█░█░█░║░█░█░║\n"
"║░█░█░║░█░█░█░║░█░█░║\n"
"║░║░║░║░║░║░║░║░║░║░║\n"
"╚═╩═╩═╩═╩═╩═╩═╩═╩═╩═╝\n")
QQ = ("───────▄██████▄───────\n"
"──────▐▀▀▀▀▀▀▀▀▌──────\n"
"──────▌▌▀▀▌▐▀▀▐▐──────\n"
"──────▐──▄▄▄▄──▌──────\n"
"───────▌▐▌──▐▌▐───────\n")

WW = ("───▄▀▀▀▀▀───▄█▀▀▀█▄\n"
"──▐▄▄▄▄▄▄▄▄██▌▀▄▀▐██\n"
"──▐▒▒▒▒▒▒▒▒███▌▀▐███\n"
"───▌▒▓▒▒▒▒▓▒██▌▀▐██\n"
"───▌▓▐▀▀▀▀▌▓─▀▀▀▀▀\n")

EE = ("──███▅▄▄▄▄▄▄▄▄▄\n"
"─██▐████████████\n"
"▐█▀████████████▌▌\n"
"▐─▀▀▀▐█▌▀▀███▀█─▌\n"
"▐▄───▄█───▄█▌▄█\n")

RR = ("───▄▄▄\n"
"─▄▀░▄░▀▄\n"
"─█░█▄▀░█\n"
"─█░▀▄▄▀█▄█▄▀\n"
"▄▄█▄▄▄▄███▀\n")

TT = ("─────────█▄██▄█\n"
"█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█\n"
"███┼█████▐████▌█████┼███\n"
"█████████▐████▌█████████\n")

YY = ("─▀▀▌───────▐▀▀\n"
"─▄▀░◌░░░░░░░▀▄\n"
"▐░░◌░▄▀██▄█░░░▌\n"
"▐░░░▀████▀▄░░░▌\n"
"═▀▄▄▄▄▄▄▄▄▄▄▄▀═\n")

UU = ("░░█▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
"██▀▀▀██▀▀▀▀▀▀██▀▀▀██\n"
"█▒▒▒▒▒█▒▀▀▀▀▒█▒▒▒▒▒█\n"
"█▒▒▒▒▒█▒████▒█▒▒▒▒▒█\n"
"██▄▄▄██▄▄▄▄▄▄██▄▄▄██\n")

II = ("▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░\n"
"▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░\n"
"▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░\n"
"▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░\n"
"░░░░▄▄███▄▄░░░░░█████░\n")

OO = ("▒▒▒▒▒▒▐███████▌\n"
"▒▒▒▒▒▒▐░▀░▀░▀░▌\n"
"▒▒▒▒▒▒▐▄▄▄▄▄▄▄▌\n"
"▄▀▀▀█▒▐░▀▀▄▀▀░▌▒█▀▀▀▄\n"
"▌▌▌▌▐▒▄▌░▄▄▄░▐▄▒▌▐▐▐▐\n")

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
@borg.on(admin_cmd(pattern=r"fox"))
async def thundergangfox(fox):
    await fox.edit(H)
@borg.on(admin_cmd(pattern=r"spider"))
async def thundergangspider(spider):
    await spider.edit(J)
@borg.on(admin_cmd(pattern=r"winter"))
async def thundergangwinter(winter):
    await winter.edit(K)
@borg.on(admin_cmd(pattern=r"love"))
async def thunderganglove(love):
    await love.edit(L)
@borg.on(admin_cmd(pattern=r"snowman"))
async def thundergangsnowman(snowman):
    await snowman.edit(Z)
@borg.on(admin_cmd(pattern=r"home"))
async def thunderganghome(home):
    await home.edit(X)
@borg.on(admin_cmd(pattern=r"guitar"))
async def thundergangguitar(guitar):
    await guitar.edit(C)
@borg.on(admin_cmd(pattern=r"pistol"))
async def thundergangpistol(pistol):
    await pistol.edit(V)
@borg.on(admin_cmd(pattern=r"whale"))
async def thundergangwhale(whale):
    await whale.edit(B)
@borg.on(admin_cmd(pattern=r"crab"))
async def thundergangcrab(crab):
    await crab.edit(N)
@borg.on(admin_cmd(pattern=r"piano"))
async def thundergangpiano(piano):
    await piano.edit(M)
@borg.on(admin_cmd(pattern=r"man"))
async def thundergangman(man):
    await man.edit(QQ)
@borg.on(admin_cmd(pattern=r"lion"))
async def thunderganglion(lion):
    await lion.edit(WW)
@borg.on(admin_cmd(pattern=r"elephant"))
async def thundergangelephant(elephant):
    await elephant.edit(EE)
@borg.on(admin_cmd(pattern=r"snail"))
async def thundergangsnail(snail):
    await snail.edit(RR)
@borg.on(admin_cmd(pattern=r"fort"))
async def thundergangfort(fort):
    await fort.edit(TT)
@borg.on(admin_cmd(pattern=r"fish"))
async def thundergangfish(fish):
    await fish.edit(YY)
@borg.on(admin_cmd(pattern=r"radio"))
async def thundergangradio(radio):
    await radio.edit(UU)
@borg.on(admin_cmd(pattern=r"computer"))
async def thundergangcomputer(computer):
    await computer.edit(II)
@borg.on(admin_cmd(pattern=r"boy"))
async def thundergangboy(boy):
    await boy.edit(OO)
