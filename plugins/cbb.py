from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://settings'>ᴛʜɪꜱ ᴘᴇʀꜱᴏɴ</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Adult_Infinity/4'>ᴀᴅᴜʟᴛ ɪɴғɪɴɪᴛʏ</a>\n○ ᴍᴏᴠɪᴇs ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/MovieflixOcean'>ᴛᴇᴀᴍ xᴇᴏɴғʟɪx</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/TeamXeon'>xᴇᴏɴғʟɪx ɴᴇᴛᴡᴏʀᴋ</a>\n○ ᴀɴɪᴍᴇ  : <a href='https://t.me/Anime_Xeon'>ᴡᴇᴇʙ ᴢᴏɴᴇ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/Adult_Infinity"),
                    InlineKeyboardButton('ᴄʜᴀɴɴᴇʟ', url='https://t.me/Xeonflix')
                    ],
                    [
                    InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/MovieflixOcean"),
                    InlineKeyboardButton('ᴄʜᴀɴɴᴇʟ', url='https://t.me/SeriesFlixOcean')
                    ],
                    [
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/Adult_Infinity/4')
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
