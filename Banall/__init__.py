from pyrogram import Client
from pyrogram import filters
import logging
import os


STARTED = 'ʙᴏᴏᴍ⚡, ꜰᴜᴄᴋɪɴɢ ᴛʜɪꜱ ᴄʀᴇᴀᴘʏ ᴄʟᴀɴ ʙʏ @jashxn_69 ...'
FINISH = 'ꜰᴜᴄᴋᴇᴅ ᴜᴘ, {} ᴜsᴇʀs  ᴡᴇʀᴇ  ʀᴇᴍᴏᴠᴇᴅ  ꜰʀᴏᴍ ᴛʜɪꜱ ᴄʀᴇᴀᴘʏ ᴄʟᴀɴ'
ERROR = 'sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ  ᴡʀᴏɴɢ  ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ᴏʀ ᴇʟsᴇ ʀᴇᴘᴏʀᴛ ᴛᴏ @jashxn_69.\n\n**{}** !'


class Config:
    TOKEN=os.environ['BOT_TOKEN']
    OWNER=os.environ['OWNER_USERNAME']
    APP_HASH=os.environ['API_HASH']
    APP_ID=int(os.environ['API_ID'])
    LOGGER=int(os.environ['LOG_ID']) 
    SUDO_USERS=int(os.environ['SUDO_USERS'])
 
    if not TOKEN:
        raise ValueError(' BOT TOKEN not set')
    
    if not APP_HASH:
        raise ValueError("API_HASH not set, set it first")

    if not APP_ID:
        raise ValueError("API_ID not set, set it first")
    if not OWNER:
        raise ValueError("OWNER_USERNAME not set, set it first")
    if not LOGGER:
        raise ValueError("LOG_ID not set, set i first")
    if not SUDO_USERS:
        raise ValueError("SUDO_USERS not set, set it first")
       

    
OWN_UNAME=Config.OWNER

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot=Client(
           ":memory:",
           api_id=Config.APP_ID,
           api_hash=Config.APP_HASH,
           bot_token=Config.TOKEN
)
