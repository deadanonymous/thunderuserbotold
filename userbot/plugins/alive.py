from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

name = str(ALIVE_NAME)
THUNDERUSERBOT_IS_ALIVE = (
"╔══╦╗╔╦╦╦═╦╦══╦═╦═╗\n"
"╚╗╔╣╚╝║║║║║╠╗╗║╦╣╬║\n"
"░║║║╔╗║║║║║╠╩╝║╩╣╗╣\n"
"░╚╝╚╝╚╩═╩╩═╩══╩═╩╩╝\n"
    " 🗲🗲🗲🗲 ThunderUserbot 🗲🗲🗲🗲                                              "
    "**Wow I Am Alive^.^** \n`⚡️BOT Status : ` **⚡️ALIVE**\n\n"
    f"`My Boss`: {name}\n\n"
    "`Thunder Userbot Version:` **3.8.7**\n`Python:` **3.8.5**\n"
    "`Database Status:` **⚡️ALL OK**\n\n`Always with you, Dear!\n`"
    "**Support channel:** [⚡️THUNDERSUPPORT](t.me/thunderuserbot)\n"
    " [⚡️Deploy Your Own THUNDERUSERBOT⚡️](https://github.com/Thundergang/thunderuserbot)"
)
@borg.on(admin_cmd(pattern="alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    await borg.send_message(chat, THUNDERUSERBOT_IS_ALIVE, link_preview=False)
