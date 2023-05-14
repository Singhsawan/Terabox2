# Buttons for bot

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from transcripts import *
from database import *
# Start Button
start_btns = InlineKeyboardMarkup([
    [InlineKeyboardButton("Join Channel ♥️", url="https://t.me/Spiner84"),
     InlineKeyboardButton("About Bot 🤖", callback_data="about_data"),
     ],
    [InlineKeyboardButton("Connect Your API 🔗", callback_data="connect_api"
                          ), ]
])


# TO DO web_app=WebAppInfo(url='')
# Back Button
about_btns = InlineKeyboardMarkup([
    [InlineKeyboardButton("◀️ Back️", callback_data="back_data"), ],
])

# Connect button
connect_btns = InlineKeyboardMarkup([
    [InlineKeyboardButton(
        "GET API TOKEN 🔑", url="https:/urllinkshort.in/member/tools/api")],
    [InlineKeyboardButton("◀️ Back️", callback_data="back_data"), ],
])



vividisk_btn_a = InlineKeyboardButton("link.urllinkshort.in ☑️", callback_data="vividisk_cb")
vividisk_btn = InlineKeyboardButton("link.urllinkshort.in", callback_data="vividisk_cb")
mdisk_btn_a = InlineKeyboardButton("link.urllinkshort.in ☑️", callback_data="mdisk_cb")
mdisk_btn = InlineKeyboardButton("urllinkshort.in", callback_data="mdisk_cb")
back_btn = InlineKeyboardButton("close", callback_data="close_cb")


MDISK_ACTIV_BTN = InlineKeyboardMarkup([[mdisk_btn_a],[vividisk_btn],[back_btn]])
VIVI_ACTIV_BTN = InlineKeyboardMarkup([[mdisk_btn],[vividisk_btn_a],[back_btn]])




