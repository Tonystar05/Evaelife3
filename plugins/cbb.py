from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://settings'>ᴛʜɪꜱ ᴘᴇʀꜱᴏɴ</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/CornFlix_link'>xғʟɪx ᴀᴅᴜʟᴛ</a>\n○ ᴍᴏᴠɪᴇs ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/xeonflixmovies'>ᴛᴇᴀᴍ xᴇᴏɴғʟɪx</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/TeamXeon'>xᴇᴏɴғʟɪx ɴᴇᴛᴡᴏʀᴋ</a>\n○ ᴀɴɪᴍᴇ  : <a href='https://t.me/Anime_Xeon'>ᴡᴇᴇʙ ᴢᴏɴᴇ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/CornFlix_link"),
                    InlineKeyboardButton('ᴄʜᴀɴɴᴇʟ', url='https://t.me/Xeonflix')
                    ],
                    [
                    InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/Xeonflixmovies"),
                    InlineKeyboardButton('ᴄʜᴀɴɴᴇʟ', url='https://t.me/TeamXeon')
                    ],
                    [
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/+uQ67sH2k6HNiZTc1')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
