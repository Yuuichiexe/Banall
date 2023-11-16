import os
import time
from pyrogram import filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from . import bot 
from Banall import STARTED, FINISH, ERROR, OWN_UNAME

# Track bot start time
start_time = time.time()

@bot.on_message(filters.group & filters.command("banall"))
def main(_, msg: Message):
    chat = msg.chat
    me = chat.get_member(bot.get_me().id)
    if chat.get_member(msg.from_user.id) and me.can_restrict_members and me.can_delete_messages:
        try:
            msg.reply(STARTED.format(chat.members_count))
            count_kicks = 0
            for member in chat.iter_members():
                if not member.can_manage_chat:
                    bot.ban_chat_member(chat_id=msg.chat.id, user_id=member.user.id)
                    count_kicks += 1
            msg.reply(FINISH.format(count_kicks))
        except Exception as e:
            msg.reply(ERROR.format(str(e)))
    else:
        msg.reply("ɪ ɴᴇᴇᴅ ᴛᴏ ʙᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ ᴛᴏ ᴘᴇʀғᴏʀᴍ ᴛʜɪs ᴀᴄᴛɪᴏɴ !")

@bot.on_message(filters.group & filters.service, group=2)
def service(c, m):
    m.delete()

@bot.on_message(filters.private)
def start(_, msg: Message):
    msg.reply_photo(
                    photo="https://te.legra.ph/file/a7aa081d0ce7f3b0124aa.jpg", 
                    caption="ʜᴇʏ ᴅᴜᴅᴇ, ɪ'ᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇ & ᴘᴏᴡᴇʀꜰᴜʟ ʙᴀɴ-ᴀʟʟ ʙᴏᴛ ᴡɪᴛʜ ɴᴏ ʟᴀɢ ɪꜱꜱᴜᴇꜱ. ᴛʜɪꜱ ʙᴀɴ-ᴀʟʟ ᴇᴅɪᴛɪᴏɴ ɪꜱ ᴄʀᴇᴀᴛᴇ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ꜰᴏʀ ꜰᴜᴄᴋɪɴɢ ᴛᴏxɪᴄ ᴄᴜᴍᴍɪɴɪᴛʏ'ꜱ.\n───────────────────────\nɴᴏᴡ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴇɴᴇᴍʏ'ꜱ ɢʀᴏᴜᴘ ᴀɴᴅ ᴅᴏɴ'ᴛ ғᴏʀɢᴇᴛ ᴛᴏ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ  ʙᴀɴ ʀɪɢʜᴛꜱ. ᴛʜᴇɴ  sᴇɴᴅ /banall ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴀɴᴅ ɪ ᴡɪʟʟ ꜰᴜᴄᴋ ᴛʜᴇ ᴡʜᴏʟᴇ ɢʀᴏᴜᴘ. \n◎ᴘᴏᴡᴇʀᴇᴅ ʙʏ ˹ʙᴏɴᴛᴇɴ ɴᴇᴛᴡᴏʀᴋ˼", 
                    reply_markup=InlineKeyboardMarkup(
                                                      [
                                                       [
                                                        InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/bonten_mainchats"), 
                                                        InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url="https://t.me/Bonten_Destroyers")                                      
                                                       ], 
                                                       [
                                                        InlineKeyboardButton("oᴡɴᴇʀ⎋", url=f"https://t.me/{OWN_UNAME}"),
                                                        InlineKeyboardButton("Hᴇʟᴘ", callback_data="help_command")  # Added Help Button
                                                       ]                                                     
                                                      ]
                                                     )
)

@bot.on_callback_query(filters.regex("help_command"))
def help_command_handler(_, callback_query):
    callback_query.answer("Check your private messages.")
    callback_query.message.delete()
    callback_query.from_user.send_text(
        "Here are the available commands:\n\n"
        "/banall - Ban all members in the group (Admin only).\n"
        "/start - Start the bot in private chat.\n"
        "/ping - Check bot's uptime and speed.\n\n"
        "For further assistance or support, join our [Support Chat](https://t.me/bonten_mainchats) "
        "or check our [Channel](https://t.me/Bonten_Destroyers).",
        disable_web_page_preview=True
    )

@bot.on_message(filters.command("ping"))
def ping(_, msg: Message):
    uptime = round(time.time() - start_time)
    ping = bot.get_ping()
    msg.reply(f"🏓 **Pong!**\n\nUptime: `{uptime // 60}m {uptime % 60}s`\nPing: `{ping}ms`")

bot.run()
idle()

print("ᴅᴏɴᴇ ʙᴀɴᴀʟʟ  sᴛᴀʀᴛᴇᴅ ...") 
print("ᴊᴏɪɴ  @bonten_mainchats ꜰᴏʀ ʜᴇʟᴘ")
