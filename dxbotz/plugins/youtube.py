# Copyright (C) 2023 DX_MODS
#Licensed under the  AGPL-3.0 License;
#you may not use this file except in compliance with the License.
#Author ZIYAN
from os import mkdir
from random import randint
from pyrogram import Client
from pyrogram import filters
from plugins.utils.ytdl import getIds,ytdl_down,audio_opt,thumb_down

@Client.on_message(filters.regex(r'(https?://)?.*you[^\s]+') & filters.private | filters.command(["yt","ytd","ytmusic"]) & filters.regex(r'https?://.*you[^\s]+') & filters.chat(AUTH_CHATS))
async def _(_,message):
    m = await message.reply_text("Gathering information... Please Wait.")
    link = message.matches[0].group(0)
    if link in [
        "https://youtube.com/",
        "https://youtube.com",
        "https://youtu.be/",
        "https://youtu.be",
    ]:
        return await m.edit_text("Please send a valid playlist or video link.")
    elif "channel" in link or "/c/" in link:
        return await m.edit_text("**Channel** Download Not Available. ")
    try:
        ids = await getIds(message.matches[0].group(0))
        videoInPlaylist = len(ids)
        randomdir = "/tmp/"+str(randint(1,100000000))
        mkdir(randomdir)
        for id in ids:
            PForCopy = await message.reply_photo(f"https://i.ytimg.com/vi/{id[0]}/hqdefault.jpg",caption=f"🎧 Title : `{id[3]}`\n🎤 Artist : `{id[2]}`\n💽 Track No : `{id[1]}`\n💽 Total Track : `{videoInPlaylist}`")
            fileLink = await ytdl_down(audio_opt(randomdir,id[2]),id[0])
            thumnail = await thumb_down(id[0])
            
