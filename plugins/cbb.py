#(Ā©)DKBOTx

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>ā š¢šš¾šŗššš : š½š [š®š„š„š«šØš­š¤]\nā š³š¾šŗš : <a href='https://t.me/dk_botx'>@š£šŖ_š”š®š³š</a>\nā š²šššššš š¢ššŗš: <a href='https://t.me/dkbotxchats'>@š£šŖš”š®š³šš¢š§š š³š² \nā š²šššš¼š¾ š¢šš½š¾ : <a href='https://github.com/DKBOTx/DKBOTx-FileStoreBot'>š¢ššš¼š š§š¾šš¾</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("š Close", callback_data = "close")
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
