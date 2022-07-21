#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """ٓ❍ | 𝙎𝙊𝙐𝙍𝘾𝙀 𝙒𝙊𝙍𝙇𝘿 .

•═════•| 𝘞𝘖𝘙𝘓𝘋 |•═════•
✅ اليك قائمة اوامر الادمن ,

◐ جميع الاوامر خاصه ب الادمن فقط .

- لعرض سرعه البوت اكتب : بنج .
- للتحكم في لغه البوت اكتب : اللغات .
- لعرض اعدادات البوت اكتب : الاعدادات .

◐ ثانيا اليك اوامر الرتب .

- لرفع ادمن في الجروب اكتب : رفع مطور ميوزك .
- لرفع ادمن في الجروب اكتب : تنزيل مطور ميوزك .
- لعرض قائمه الادمنيه اكتب : المطورين .

◐ ثالثا اليك اوامر الحظر .

- لحظر عضو من الجروب اكتب : حظر ميوزك .
- لالغاء حظر عضو من الجروب اكتب : الغاء حظر ميوزك .
- لعرض قائمه المحظورين اكتب : المحظورين ميوزك . """

HELP_2 = """ٓ❍ | 𝙎𝙊𝙐𝙍𝘾𝙀 𝙒𝙊𝙍𝙇𝘿 .

•═════•| 𝘞𝘖𝘙𝘓𝘋 |•═════•
✅ اليك قائمة اوامر التشغيل ,

❀ اليك اوامر التشغيل ف الجروب .
- لتشغيل اغنيه اكتب : تشغيل او شغل او /play
- لتشغيل فيديو اكتب : /vplay
- لأنهاء الاغنيه اكتب : انهاء او اسكت او /end
- لايقاف الاغنيه مؤقت اكتب : ايقاف او توقف او /pause
- لتكملة الاغنيه من الايقاف المؤقت اكتب : كمل او استئناف او /resume
- لتخطي الاغنيه اكتب : تخطي او /skip
- لكتم البوت في الكول اكتب : ميوت او /mute
- لألغاء كتم البوت في الكول اكتب : فك ميوت او /unmute
- لاعادة تشغيل البوت اكتب : ريستارت او /restart """


HELP_3 = """✅<u>**اوامر البوت:**</u>

/stats • احصل على أفضل 10 مسارات إحصائيات عالمية ، وأفضل 10 مستخدمين للبوت ، وأفضل 10 دردشات على الروبوت ، وأفضل 10 دردشات تم لعبها في دردشة وما إلى ذلك.

/sudolist • تحقق من قائمه المطورين

/lyrics اسم الموسيقى • يبحث في كلمات الأغاني عن موسيقى معينة على الويب.

/song اسم المسار أو رابط YT • قم بتنزيل أي مسار من youtube بتنسيقات mp3 أو mp4.

/player -  احصل على لوحة تشغيل تفاعلية.

**c** تعني تشغيل في القناه

/queue or /cqueue • تحقق من قائمة انتظار الموسيقى."""

HELP_4 = """✅<u>**Extra  Commands:**</u>
/start - Start the Music Bot.
/help  - Get Commands Helper Menu with detailed explanations of commands.
/ping- Ping the Bot and check Ram, Cpu etc stats of Bot.

✅<u>**Group Settings:**</u>
/settings - Get a complete group's settings with inline buttons

🔗 **Options in Settings:**

1️⃣ You can set **Audio Quality** you want to stream on voice chat.

2️⃣ You can set **Video Quality** you want to stream on voice chat.

3️⃣ **Auth Users**:- You can change admin commands mode from here to everyone or admins only. If everyone, anyone present in you group will be able to use admin commands(like /skip, /stop etc)

4️⃣ **Clean Mode:** When enabled deletes the bot's messages after 5 mins from your group to make sure your chat remains clean and good.

5️⃣ **Command Clean** : When activated, Bot will delete its executed commands (/play, /pause, /shuffle, /stop etc) immediately.

6️⃣ **Play Settings:**

/playmode - Get a complete play settings panel with buttons where you can set your group's play settings. 

<u>Options in playmode:</u>

1️⃣ **Search Mode** [Direct or Inline] - Changes your search mode while you give /play mode. 

2️⃣ **Admin Commands** [Everyone or Admins] - If everyone, anyone present in you group will be able to use admin commands(like /skip, /stop etc)

3️⃣ **Play Type** [Everyone or Admins] - If admins, only admins present in group can play music on voice chat."""

HELP_5 = """🔰**<u>ADD & REMOVE SUDO USERS :</u>**
/addsudo [Username or Reply to a user]
/delsudo [Username or Reply to a user]

🛃**<u>HEROKU:</u>**
/usage - Dyno Usage.

🌐**<u>CONFIG VARS:</u>**
/get_var - Get a config var from Heroku or .env.
/del_var - Delete any var on Heroku or .env.
/set_var [Var Name] [Value] - Set a Var or Update a Var on heroku or .env. Seperate Var and its Value with a space.

🤖**<u>BOT COMMANDS:</u>**
/reboot - Reboot your Bot. 
/update - Update Bot.
/speedtest - Check server speeds
/maintenance [enable / disable] 
/logger [enable / disable] - Bot logs the searched queries in logger group.
/get_log [Number of Lines] - Get log of your bot from heroku or vps. Works for both.
/autoend [enable|disable] - Enable Auto stream end after 3 mins if no one is listening.

📈**<u>STATS COMMANDS:</u>**
/activevoice - Check active voice chats on bot.
/activevideo - Check active video calls on bot.
/stats - Check Bots Stats

⚠️**<u>BLACKLIST CHAT FUNCTION:</u>**
/blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
/whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot
/blacklistedchat - Check all blacklisted chats.

👤**<u>BLOCKED FUNCTION:</u>**
/block [Username or Reply to a user] - Prevents a user from using bot commands.
/unblock [Username or Reply to a user] - Remove a user from Bot's Blocked List.
/blockedusers - Check blocked Users Lists

👤**<u>GBAN FUNCTION:</u>**
/gban [Username or Reply to a user] - Gban a user from bot's served chat and stop him from using your bot.
/ungban [Username or Reply to a user] - Remove a user from Bot's gbanned List and allow him for using your bot
/gbannedusers - Check Gbanned Users Lists

🎥**<u>VIDEOCALLS FUNCTION:</u>**
/set_video_limit [Number of Chats] - Set a maximum Number of Chats allowed for Video Calls at a time. Default to 3 chats.
/videomode [download|m3u8] - If download mode is enabled, Bot will download videos instead of playing them in M3u8 form. ByDefault to M3u8. You can use download mode when any query doesnt plays in m3u8 mode.

⚡️**<u>PRIVATE BOT FUNCTION:</u>**
/authorize [CHAT_ID] - Allow a chat for using your bot.
/unauthorize [CHAT_ID] - Disallow a chat from using your bot.
/authorized - Check all allowed chats of your bot.

🌐**<u>BROADCAST FUNCTION:</u>**
/broadcast [Message or Reply to a Message] - Broadcast any message to Bot's Served Chats.

<u>options for broadcast:</u>
**-pin** : This will pin your message 
**-pinloud** : This will pin your message with loud notification
**-user** : This will broadcast your message to the users who have started your bot.
**-assistant** : This will broadcast your message from assistant account of your bot.
**-nobot** : This will force your bot to not broadcast message

**Example:** `/broadcast -user -assistant -pin Hello Testing`

"""
