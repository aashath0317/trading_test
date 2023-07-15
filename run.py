import re
import time
import telegram
from telegram.ext import Updater
import telegram.ext
from telegram.ext import CommandHandler
from time import sleep
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
#from telegram.message import Message
#from telegram.update import Update
from telegram.error import RetryAfter
from pyrogram.errors import FloodWait
from pyrogram import Client
from pyrogram import filters
import sys, traceback
import os
import subprocess
import sys
from datetime import datetime
import glob
import requests
import asyncio
import telethon
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.events import NewMessage
from telethon import events

#session_string = "94755039496,BQAuPHAAJTJsYNzJo67WCOcle9jarh7uYxI1nUZBmbQFLJrep6XqYqbfc8_0L9W3KQKpTO6slV2pf5aF2w5WHN_Lh5n8_qYJTHLmwMsbOR7zqQ6FCZtUFNdpXFlAEpF10uFIHZGPLbY2761VP88lDN9a0YmF31fQiGO-7oeS9pP1wjogd_Aw1bLBdPAT87YJepwAMVuBCycDid6hKHmxmEl0McphpYWijWTnWz7y-6XqUQ0ohkB9nYqugtATWldRcjAZ27JYMplYxHGREVR-wh-DaMVAUT_rykgONMOfXktKQbEFtyRRouP5khywrZM6tmvvWoJrb7i4qZOdzy6MJYEun2WlSQAAAABL5wISAA"
#app = Client(session_name="new",api_id = 3030128,api_hash = 'cfc3885f5d2cbdbc5f10e6a643de2711')
#s = await app.export_session_string()
#app.run()
string='1BVtsOIoBuxry5w5N3abV2EToGHe0GFxMJXdlKXC2Y6ea3DLyHLYrXnxUvUTGV4X5quKFHlJJF5PIyc2jkzPlrcv3AQRFyP8gfKsrBOcJFLXLGjlUD_U6itx2yyVfiJZyBRvMC6qon7-LdTUvFm7PMCw0rJL3I7aYmwHs6DbXtZxkdxY_4O_ZcbP_-XpWh_JD7puo9m3DhyHISZ9PVIy-rmA67wtweOcu8-O-aiOr317jm2UNc_XaxLmuz9l-6ELz_wayVVzW89K6EZH2R_GmC2YM-4gtNI7UXyjfEpL4SrKLJ0rfVMtNc-zZXcnNq1wmCgSDwXytuvCvISiZ2X_ShUVxA-Xi1tE='
client = telethon.TelegramClient(StringSession(string),api_id=3030128, api_hash='cfc3885f5d2cbdbc5f10e6a643de2711')
client.connect()

channel_id = -1001963686318
group_id = "@C2P_forex_bot"   #5007713837
igroup = -990951103
client.send_message(group_id, s_message)

@client.on(events.NewMessage(chats=channel_id))
async def my_event_handler(event):
    message = str(event.text)
    #send_channel = message.chat.title
    pair = ""
    string = message
    tstring = string.split("\n")
    def remove_empty_datatypes(list_of_strings):
        new_list = []
        for string in list_of_strings:
            if string:
                new_list.append(string)
        return new_list
    try:
        list_of_strings = tstring
        tstring = remove_empty_datatypes(list_of_strings)
        pao = tstring[0].split(" ")
        pair = pao[0]
        order = pao[1]
        order_check = pao[2].upper()
    except IndexError:
         await client.send_message(igroup, 'Trading Not Placed \n Check this string  \n '+str(tstring))
         return
    if order_check == "NOW":
        sl = str(tstring[1].split(":")[1].strip(" "))
        tp1 = str(tstring[2].split(":")[1].strip(" "))
        tp2 = str(tstring[3].split(":")[1].strip(" "))
        if pair == "GOLD":
            pair = "XAUUSD"
        else:
            pass 
        s_message = order+" "+pair+"\n"+"Entry NOW"+"\n"+"SL "+sl+"\n"+"TP "+tp1
       # s_message = order+" "+pair+"\n"+"Entry NOW"+"\n"+"SL "+sl+"\n"+"TP1 "+tp1+"\n"+"TP2 "+tp2
        await client.send_message(group_id, "/trade")
        await client.send_message(group_id, s_message)
    else:
        await client.send_message(igroup, 'Trading Not Placed \n Check this string  \n '+str(tstring))

channel_2 = "@C2P_forex_bot"
igroup = -990951103

@client.on(events.NewMessage(chats=channel_2))
async def my_event_handler(event):
    message = str(event.text)
    await client.send_message(igroup, message)
if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()
