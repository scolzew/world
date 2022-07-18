import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from strings import get_command
from strings.filters import command
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

@app.on_message(
    filters.command(["id"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""نـيـمـك💕 ⇐{message.from_user.mention}\n\nيـوزرك💕 ⇐ @{message.from_user.username}\n\nالايـدي بـتـاعـك💕 ⇐ {message.from_user.id}\n\nايـدي الـجـروب💕 ⇐ {message.chat.id}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "╞. 𝐒𝐨𝐮𝐫𝐜𝐞 .╡", url=f"https://t.me/ch_world_music"),
                ],
            ]
        ),
    )

@app.on_message(
    command(["ايدي","الايدي"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""نـيـمـك💕 ⇐{message.from_user.mention}\n\nيـوزرك💕 ⇐ @{message.from_user.username}\n\nالايـدي بـتـاعـك💕 ⇐ {message.from_user.id}\n\nايـدي الـجـروب💕 ⇐ {message.chat.id}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "╞. 𝐒𝐨𝐮𝐫𝐜𝐞 .╡", url=f"https://t.me/ch_world_music"),
                ],
            ]
        ),
    )