import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from strings import get_command
from strings.filters import command
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


# الكود اهو يصحبي  . 

@app.on_message(
    filters.command(["id"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""⇐𓂄𓆩💕نـيـمـك𓆪𓂁 {message.from_user.mention}\n\n⇐𓂄𓆩💕يوزرك𓆪𓂁 @{message.from_user.username}\n\n⇐𓂄𓆩💕الايدي بتاعك𓆪𓂁 {message.from_user.id}\n\n⇐𓂄𓆩💕ايدي الجروب𓆪𓂁 {message.chat.id}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],[
                    InlineKeyboardButton(
                        "╞. 𝐒𝐨𝐮𝐫𝐜𝐞 .╡", url=f"https://t.me/ch_world_music"),
                ],
            ]
        ),
    )
