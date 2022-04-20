#(©)DKBOTx

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : 𝖽𝗄 [𝖮𝖥𝖥𝖫𝖨𝖭𝖤]\n○ 𝖳𝖾𝖺𝗆 : <a href='https://t.me/dk_botx'>@𝖣𝖪_𝖡𝖮𝖳𝗑</a>\n○ 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖢𝗁𝖺𝗍: <a href='https://t.me/dkbotxchats'>@𝖣𝖪𝖡𝖮𝖳𝗑𝖢𝖧𝖠𝖳𝖲 \n○ 𝖲𝗈𝗎𝗋𝖼𝖾 𝖢𝗈𝖽𝖾 : <a href='https://github.com/DKBOTx/DKBOTx-FileStoreBot'>𝖢𝗅𝗂𝖼𝗄 𝖧𝖾𝗋𝖾</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
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
