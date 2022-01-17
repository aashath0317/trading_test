
import time
import telegram
from telegram.ext import Updater
import telegram.ext
from telegram.ext import CommandHandler
from time import sleep
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.message import Message
from telegram.update import Update
from telegram.error import RetryAfter
from pyrogram.errors import FloodWait
from pyrogram import Client
from pyrogram import filters
import sys, traceback
import os
import subprocess
from datetime import datetime
import glob
import requests

bot = Client('pyrogram', api_id=3030128, api_hash="cfc3885f5d2cbdbc5f10e6a643de2711", bot_token="5066559573:AAHpW3kVR3yZEIzKPvMlDPkgxXaHSN_NDoo")

channels = {-1787560665: {'type': 'channel', 'trading': 'str_long', 'url': '@myforexc2ptech'},
            -1601274303: {'type': 'channel', 'trading': 'scalping', 'url': '@dolor_hiest'},
            -1660396935: {'type': 'channel', 'trading': 'scalping', 'url': '@pips30_c2p'},
            -1631407380: {'type': 'channel', 'trading': 'scalping', 'url': '@c2p_pro'},
            -1662289372: {'type': 'channel', 'trading': 'scalping', 'url': '@c2p_fmfx'},
            -1795072861: {'type': 'channel', 'trading': 'scalping', 'url': '@pips15_c2p'}}  

@bot.on_message(filters.channel)              #ERROR HANDLING
def my_handler(client, message):
    try:
        os.mkdir("downloads")
    except FileExistsError:
        pass
    path = "downloads"
    up_path = glob.glob(os.path.join(path, '*'))
    if not up_path == []:
        subprocess.run(["rm","-r","downloads"])
    chat_id = -1001787560665
    message = message
    send_channel = message.sender_chat.username
    pair = ""
    filetype = message.photo
    filetype_text = message.text
    need = 0                                           # GETTING TP ,SL, ORDER, Professor pair and setting working only signal
    if send_channel == "dolor_hiest" and not filetype == None:
        try:
            signal = message.caption.split("\n")
            order = signal[0].split("@")[0].strip(" ")
            price = float(signal[0].split("@")[1].strip(" "))
            tp = float(signal[2].split(" ")[2])
            sl = float(signal[5].split(" ")[4])
            img_name = "dolor_heist.jpg"
            text_file = "dolor_hiest_text"
            if price < tp and price > sl and order == "BUY NOW":
                need = 1
            elif price > tp and price < sl and order == "SELL NOW":
                need = 1
            else:
                msg = "Something wrong is this signal Order.. not triggered From DollorHiest"
                bot.send_message(chat_id=chat_id, text=msg, parse_mode=telegram.ParseMode.HTML)
                need = 0
        except IndexError:
            need = 0

 
    elif send_channel == "pips30_c2p" and not filetype == None:
        try:
            signal = message.caption.split("\n")
            order = signal[0].split(" ")[0]
            text_file = "pips30_c2p"
            img_name = "pips30_c2p.jpg"
            price = float(signal[0].split(" ")[2])
            if order == "Buy":
                order = "BUY NOW"
            elif order == "Sell":
                order = "SELL NOW"
            else:
                msg = "order not tiggered Reason: Unable resolve order type"
                bot.send_message(chat_id=chat_id, text=msg, parse_mode=telegram.ParseMode.HTML)
            tp = float(signal[2].split(" ")[1])
            sl = float(signal[5].split(" ")[2])

            if price < tp and price > sl and order == "BUY NOW":
                need = 1
            elif price > tp and price < sl and order == "SELL NOW":
                need = 1
            else:
                msg = "Something wrong is this signal Order.. not triggered From PIPS30"
                bot.send_message(chat_id=chat_id, text=msg, parse_mode=telegram.ParseMode.HTML)
                need = 0
        except IndexError:
            need = 0

        
    elif send_channel == "c2p_fmfx" and not filetype == None:
        try:
            img_name = "c2p_fmfx.jpg"
            text_file = "c2p_fmfx"
            signal = message.caption.split("\n")
            order = signal[0].split("@")[0].strip(" ")
            price = float(signal[0].split("@")[1].strip(" "))
            tp = float(signal[2].split(" ")[1])
            sl = float(signal[5].split(" ")[1])
            if price < tp and price > sl and order == "BUY NOW":
                need = 1
            elif price > tp and price < sl and order == "SELL NOW":
                need = 1
            else:
                msg = "Something wrong is this signal Order.. not triggered From FMFX"
                bot.send_message(chat_id=chat_id, text=msg, parse_mode=telegram.ParseMode.HTML)
                need = 0
        except IndexError:
            need = 0                

    elif send_channel == "pips15_c2p" and not filetype == None:
        try:
            img_name = "pips15_c2p.jpg"
            text_file = "pips15_c2p"
            signal = message.caption.split("\n")
            order = signal[0].split(" ")[0]
            price = float(signal[0].split(" ")[1])
            if order == "BUY":
                order = "BUY NOW"
            elif order == "SELL":
                order = "SELL NOW"
            else:
                msg = "Something wrong is this signal Order.. unable to resolve Order type not triggered From M15"
                bot.send_message(chat_id=chat_id, text=msg, parse_mode=telegram.ParseMode.HTML)
                need = 0
            tp = float(signal[2].split(" ")[1])
            sl = float(signal[5].split(" ")[1])            
            if price < tp and price > sl and order == "BUY NOW":
                need = 1
            elif price > tp and price < sl and order == "SELL NOW":
                need = 1
            else:
                msg = "Something wrong is this signal Order.. not triggered From M15"
                bot.send_message(chat_id=chat_id, text=msg, parse_mode=telegram.ParseMode.HTML)
                need = 0
        except IndexError:
            need = 0

    elif send_channel == "c2p_pro" and filetype == None:
        try:
            signal = filetype_text.split("\n")
            need = 2
            pair = signal[0].split(" / ")[0]+signal[0].split(" / ")[1]
            order = signal[2].split(" ")[0]
            price = float(signal[2].split(" ")[1])
            print(price)
            if order == "BUY":
                order = "BUY NOW"
            elif order == "SELL":
                order = "SELL NOW"        
            tp = float(signal[4].split(" ")[1])
            sl = float(signal[7].split(" ")[1])
            if price < tp and price > sl and order == "BUY NOW":
                need = 2
            elif price > tp and price < sl and order == "SELL NOW":
                need = 2
            else:
                msg = "Something wrong is this signal Order.. not triggered From Professor"
                bot.send_message(chat_id=chat_id, text=msg, parse_mode=telegram.ParseMode.HTML)
                need = 0
        except IndexError:
            need =0



    # Process               DollorHiest Complete
    if send_channel == "dolor_hiest" and need == 1:
        bot.download_media(file_name=img_name,message=message)
        subprocess.run(["tesseract","downloads/"+img_name,text_file])
        text= text_file+".txt"
        f = open(text,'r')
        pair = f.readlines()        
        try:                          # CHECKING PAIR IN DOLLOR_HIEST
            if pair == ['NY\n', 'q\n', '\n', ' \n', '\n', 'Sotriemicoeliite Japanese Yen\n', 'SyO nm\n', '@DollarHeistOfficial #DollarHeist LBLYD\n', '\x0c']:
                pair = "GBPJPY"
                text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom DollorHiest"
                bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
            elif pair == [' \n', '\x0c']:
                pair = "EURAUD"
                text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom DollorHiest"
                bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
            elif pair == [' \n', '\n', 'Australian Dollar American Dollar\n', '\n', 'a a\n', 'BVO\n', 'ak)\n', '\n', '@DollarHeistOfficial #DollarHeist\n', '\x0c']:
                pair = "AUDUSD"
                text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom DollorHiest"
                bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
            elif pair == [' \n', '\n', 'Euro Japanese Yen\n', '\n', '— 7\n', 'BVO)\n', 'ak)\n', '\n', '@DollarHeistOfficial #DollarHeist\n', '\x0c']:
                pair = "EURJPY"
                text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom DollorHiest"
                bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
            elif pair == [' \n', '\n', 'Pound Sterling Australian Dollar\n', '\n', '— 7\n', 'STO) nV)\n', 'ak)\n', '\n', '@DollarHeistOfficial #DollarHeist\n', '\x0c']:
                pair = "GBPAUD"
                text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom DollorHiest"
                bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
            elif pair == [' \n', '\n', 'New Zealand Dollar American Dollar\n', '\n', 'a a\n', 'BVO\n', 'ak)\n', '\n', '@DollarHeistOfficial #DollarHeist\n', '\x0c']:
                pair = "NZDUSD"
                text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom DollorHiest"
                bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
            else:
                caption = f'I cant resolve this photo From {send_channel} \n\n'
                photo = "downloads/"+img_name
                caption += f'Uniq string is:\n( {str(pair)} )'
                bot.send_photo(chat_id=chat_id, caption=caption, photo=photo)
                bot.send_document(chat_id=chat_id, document=text_file+".txt", caption="This is File Uniq string file")  
        except:
            msg = "What is this i don't know about this From DollorHeist\n\n"
            msg += text
            bot.send_message(chat_id=chat_id, text=msg, parse_mode=telegram.ParseMode.HTML)
                           
     
    # pips30 Complete
    elif send_channel == "pips30_c2p" and need == 1:
        bot.download_media(file_name=img_name,message=message)
        subprocess.run(["tesseract","downloads/pips30_c2p.jpg",text_file])
        text= text_file+".txt"
        f = open(text,'r')
        pair = f.readlines()
        if pair == ['#PIPS30\n', '\n', 'a\n', 'a\n', 'fe)\n', 'oO\n', '\n', ' \n', '\n', 'AMERICAN DOLLAR\n', '\x0c']:
            pair = "XAUUSD"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom PIPS 30"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        elif pair == [' \n', '\n', 'RO 4) #PIPS30\n', '\n', 'POUND STERLING\n', '\n', 'JAPANESE YEN\n', '\n', ' \n', '\n', ' \n', '\n', 'uo\n', 'SG\n', '\x0c']:
            pair = "GBPJPY"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom PIPS 30"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        elif pair == [' \n', '\n', 'MES La) #PIPS30\n', '\n', ' \n', '\n', 'NEW ZEALAND DOLLAR\n', '\n', ' \n', '\n', 'AMERICAN DOLLAR\n', '\n', ' \n', '\n', ' \n', '\x0c']:
            pair = "NZDUSD"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom PIPS 30"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        elif pair == ['ee) #PIPS30\n', '\n', ' \n', '\n', '2010) SP R-9 a 1518 Te)\n', '\n', ' \n', '\n', 'AMERICAN DOLLAR\n', '\n', ' \n', '\n', ' \n', '\x0c']:
            pair = "GBPUSD"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom PIPS 30"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
  
        #elif pair == "lk":
        #    pair = "XAUUSD"
        #    text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom PIPS 30"
        #    bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        else:
            caption = f'I cant resolve this photo From {send_channel} \n\n'
            photo = "downloads/"+img_name
            caption += f'Uniq string is:\n( {str(pair)} )'
            bot.send_photo(chat_id=chat_id, caption=caption, photo=photo)
            bot.send_document(chat_id=chat_id, document=text_file+".txt", caption="This is File Uniq string file")  
    
    #getting fmfx
    elif send_channel == "c2p_fmfx" and need == 1:
        bot.download_media(file_name=img_name,message=message)
        subprocess.run(["tesseract","downloads/"+img_name,text_file])
        text= text_file+".txt"
        f = open(text,'r')
        pair = f.readlines()
        if pair == ['wad\n', '\n', '    \n', '\n', '|\n', 'Canadian dollar\n', '|\n', '\n', '!\n', '|\n', '\n', 'Sag\n', '\n', '@fmfxofficial #FMPFXofficial #FULLMARGIN\n', '\x0c']:
            pair = "EURCAD"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom FMFX"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        elif pair == ['wad\n', '\n', '@fmfxofficial\n', '\n', ' \n', '\n', 'ustralian dollar\n', 'i\n', 'i\n', '\n', '#FMPFXofficial\n', '\n', '#FULLMARGIN\n', '\x0c']:
            pair = "EURAUD"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom FMFX"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        elif pair == ['wad\n', '\n', 'CAD\n', '\n', '  \n', '      \n', '\n', '|\n', '\n', '|\n', '\n', '|\n', '\n', 'Japanese yen\n', '|\n', '\n', '!\n', '!\n', '\n', '|\n', '\n', '(Ohi ehiilereU #FMPFXofficial #FULLMARGIN\n', '\x0c']:
            pair = "CADJPY"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom FMFX"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        elif pair == ['za\n', '\n', 'GBP\n', '\n', '  \n', '\n', '(ine ehiilereu #FMFXofficial #FULLMARGIN\n', '\x0c']:
            pair = "GBPAUD"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom FMFX"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        elif pair == ['FMFX\n', '\n', 'GBP\n', '\n', ' \n', '     \n', '\n', 'Japanese yen\n', '|\n', '\n', 'i\n', 'I\n', '\n', '@fmfxofficial #FMPFXofficial #FULLMARGIN\n', '\x0c']:
            pair = "GBPJPY"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom FMFX"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        elif pair == ['wae\n', '\n', ' \n', '\n', '#FULLMARGIN\n', '\n', '#FMFXofficial\n', '\n', '@fmfxofficial\n', '\x0c']:
            pair = "EURUSD"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom FMFX"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
        elif pair == ['FMFX\n', '\n', 'a EUR\n', '\n', '     \n', '\n', '|\n', 'Japanese yen\n', '\n', '@fmfxofficial #FMFXofficial #FULLMARGIN\n', '\x0c']:
            pair = "EURJPY"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom FMFX"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)                        
        else:
            caption = f'I cant resolve this photo From {send_channel} \n\n'
            photo = "downloads/"+img_name
            caption += f'Uniq string is:\n( {str(pair)} )'
            bot.send_photo(chat_id=chat_id, caption=caption, photo=photo)
            bot.send_document(chat_id=chat_id, document=text_file+".txt", caption="This is File Uniq string file")  
        #bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

    elif send_channel == "c2p_pro" and need == 2:
        text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom Professor"
        bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
    elif send_channel == "pips15_c2p" and need == 1:
        bot.download_media(file_name=img_name,message=message)
        subprocess.run(["tesseract","downloads/"+img_name,text_file])
        text= text_file+".txt"
        f = open(text,'r')
        pair = f.readlines()
        if pair == ['=\n', 'USD / CHF\n', '\x0c']:
            pair = "USDCHF"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
        if pair == ['NA =\n', 'Ry WN ———|\n', '\n', 'GBP / USD\n', '\x0c']:
            pair = "GBPUSD"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
        if pair == ['NZ\n', 'Fain\n', '\n', ' \n', '\n', 'GBP / AUD\n', '\x0c']:
            pair = "GBPAUD"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
        else:
            print(pair)
            caption = f'I cant resolve this photo From {send_channel} \n\n'
            photo = "downloads/"+img_name
            caption += f'Uniq string is:\n( {str(pair)} )'
            bot.send_photo(chat_id=chat_id, caption=caption, photo=photo)
            bot.send_document(chat_id=chat_id, document=text_file+".txt", caption="This is File Uniq string file")  
    else:
        pass


subprocess.run(["rm","*.session","*.session-journal"])
bot.run()