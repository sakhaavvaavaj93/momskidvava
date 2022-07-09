import asyncio
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import MessageNotModified
from momskidvava.main import Test, bot as Client
from config import START_PIC, UPDATES_CHANNEL, GROUP_SUPPORT


ALIVE_PIC = START_PIC
HOME_TEXT = "『𝙷𝚊𝚒 .... {} , 𝙸 𝚊𝚖 𝚊 𝙻𝚊𝚐𝚐𝚕𝚎𝚜𝚜 𝙱𝚘𝚝 𝚘𝚏 [@𝚔𝚔_𝚔𝚘𝚟𝚒𝚕𝚊𝚔𝚊𝚖](https://t.me/kk_kovilakam)』\n 『𝗼𝘄𝗻𝗲𝗿 : [@kk_heaven_hater](https://t.me/kk_heaven_hater) . 』"
HELP_TEXT = """
🏷️ **Setup Guide** :

\u2022 Start a voice chat in your group.
\u2022 Add bot and user account in chat with admin rights.
\u2022 Done Setup Process Read Commands Below 👇.
"""



USER_TEXT = """
🏷️ **Users Commands** :

\u2022 /play <Query> To Play a Song.
\u2022 /vplay <Query> To Play Video.
\u2022 /stream <Live Url> To Play Live Streams 👇\n /song To Download A Audio file from YouTube. \n /video to download Video From YouTube\n /lyric to find Lyrics.
"""

ADMIN = """
🏷️ **admin Commands** :

\u2022 /userbotjoin To Invite Assistant To Your Chat.
\u2022 /end To End Streaming.
\u2022 /pause To Pause Stream.
\u2022 /resume To Resume Stream.
\u2022 /volume To Set Volume.
\u2022 /skip To Skip Tracks.
"""

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("🗨️ Uꜱᴇʀꜱ", callback_data="users"),
            ],
            [
                InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="home"),
                InlineKeyboardButton("🤷 Cʟᴏꜱᴇ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="home":
        get_me = await client.get_me()
        USERNAME = get_me.username
        buttons = [
            [
                InlineKeyboardButton("🧐 Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀᴛ", url='https://t.me/{USERNAME}?startgroup=true'),
            ],
            [
                InlineKeyboardButton("💌 Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton("🏷️ Cʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            [
                InlineKeyboardButton("🤔 Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ", callback_data="help"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HOME_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="users":
        buttons = [
            [
                InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("🤷 Cʟᴏꜱᴇ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                USER_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="admins":
        buttons = [
            [
                InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("🤷 Cʟᴏꜱᴇ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(ADMIN, reply_markup=reply_markup)
        except MessageNotModified:
            pass

    

@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    get_me = await client.get_me()
    USERNAME = get_me.username
    buttons = [
            [
                InlineKeyboardButton("🧐 Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀᴛ", url=f'https://t.me/{USERNAME}?startgroup=true'),
            ],
            [
                InlineKeyboardButton("💌 Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton("🏷️ Cʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            [
                InlineKeyboardButton("🤔 Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ", callback_data="help"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=f"{ALIVE_PIC}", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client: Client, message: Message):
    get_me = await client.get_me()
    self.username = get_me.username
    buttons = [
            [
                InlineKeyboardButton("👮 Aᴅᴍɪɴꜱ", url="https://telegra.ph/𝗕ooo--‌ᴀꜰᴋ-ᴏꜰꜰʟɪɴᴇ-05-17-2"),
                InlineKeyboardButton("🗨️ Uꜱᴇʀꜱ", callback_data="users"),
            ],
            [
                InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="home"),
                InlineKeyboardButton("🤷 Cʟᴏꜱᴇ", callback_data="close"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=f"{ALIVE_PIC}", caption=f"{HELP_TEXT}", reply_markup=reply_markup)
