from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from strings import get_command
from strings.filters import command
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
import asyncio
from typing import Union
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME, START_IMG_URL
import re
import sys
from os import getenv
from dotenv import load_dotenv

load_dotenv()

START_IMG_URL = getenv("START_IMG_URL")

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")

@app.on_message(
    command(["اسمي"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""ٲسـمـك💕 ⇐ {message.from_user.mention}""", 
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
    command(["صورتي"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""غير صورتك بقا قرفتنا 😏""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],[
                    InlineKeyboardButton(
                        "╞. 𝐒𝐨𝐮𝐫𝐜𝐞.╡", url=f"https://t.me/ch_world_music"),
                ],
            ]
        ),
    )
    
@app.on_message(
    command(["معرفي"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""مـعـرفـك💕 ⇐ @{message.from_user.username}""", 
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
    command(["بوت"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG_URL}",
        caption=f"اسمي {MUSIC_BOT_NAME} ينجم 😮‍💨💕", 
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
    
@app.on_message(
    command(["قول"])
    & filters.group
    & ~filters.edited
)
def echo(client, msg):
    text = msg.text.split(None, 1)[1]
    msg.reply(text)

@app.on_message(
    command(["الـبـابـو"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.about)
    name = usr.first_name
    async for photo in client.iter_profile_phmessage.from_user.about, limit=1):
                    await message.reply_text( 
                    f"""الـبـايـو💕 ⇐ {message.from_user.about}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "╞. 𝐒𝐨𝐮𝐫𝐜𝐞 .╡", url=f"https://t.me/ch_world_music"),
                ],
            ]
        ),
    )
