
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
import sys
from datetime import datetime
import glob
import requests

def spawn_program_and_die(program, exit_code=0):
            subprocess.Popen(program)
            sys.exit(exit_code)

bot = Client('pyrogram', api_id=3030128, api_hash="cfc3885f5d2cbdbc5f10e6a643de2711", bot_token="5066559573:AAHpW3kVR3yZEIzKPvMlDPkgxXaHSN_NDoo")

channels = {-1787560665: {'type': 'channel', 'trading': 'str_long', 'url': '@myforexc2ptech'},
            -1601274303: {'type': 'channel', 'trading': 'scalping', 'url': '@dolor_hiest'},
            -1660396935: {'type': 'channel', 'trading': 'scalping', 'url': '@pips30_c2p'},
            -1631407380: {'type': 'channel', 'trading': 'scalping', 'url': '@c2p_pro'},
            -1662289372: {'type': 'channel', 'trading': 'scalping', 'url': '@c2p_fmfx'},
            -1795072861: {'type': 'channel', 'trading': 'scalping', 'url': '@pips15_c2p'}}  


 
           
@bot.on_message(filters.command("update"))
def update(client, message):
            owner_id = message.chat.id
            if not owner_id == 1273430546:
                        client_id = message.chat.id
                        message = "Sorry Your not a owner this command only work for owner"
                        bot.send_message(chat_id=client_id, text=message, parse_mode=telegram.ParseMode.HTML)
            
            else:
                        spawn_program_and_die(['bash', 'start.sh'])
                        

                        
                     
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
            print(signal)
            order = signal[0].split("@")[0].strip(" ")
            print(order)
            price = float(signal[0].split("@")[1].strip(" "))
            print(price)
            tp = float(signal[2].split(" ")[2])
            try:
                sl = float(signal[5].split(" ")[4])
                print(sl)
            except IndexError:
                sl = float(signal[5].split(" ")[2])
                print(sl)  
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
        print("hi")
        subprocess.run(["tesseract","--dpi", "70","downloads/"+img_name,text_file])
        text= text_file+".txt"
        f = open(text,'r')
        pair = f.readlines()        
        try:                          # CHECKING PAIR IN DOLLOR_HIEST
            if pair == ['m2\n', 'iN\n', '\n', ' \n', '\n', 'Satie eye lites Japanese Yen\n', 'Ora\n', '@DollarHeistOfficial #DollarHeist WEIST\n', '\x0c']:
                pair = "GBPJPY"
                text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom DollorHiest"
                bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
            elif pair == [' \n', '\x0c']:
                pair = "EURAUD"
                text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom DollorHiest"
                bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
            elif pair == [' \n', '\n', 'Australian Dollar American Dollar\n', '\n', 'a\n', 'ST OAR)\n', 'Bice\n', '\n', '@DollarHeistOfficial #DollarHeist\n', '\x0c']:
                pair = "AUDUSD"
                text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom DollorHiest"
                bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
            elif pair == [' \n', '\n', 'Euro Japanese Yen\n', '\n', 'ee ea\n', 'OLLA\n', 'SC a\n', '\n', '@DollarHeistOfficial #DollarHeist\n', '\x0c']:
                pair = "EURJPY"
                text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom DollorHiest"
                bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
            elif pair == [' \n', '\n', '2\n', 'q\n', '\n', 'Satie eye lites Australian Dollar\n', 'Sg\n', '@DollarHeistOfficial #DollarHeist Eh y\n', '\x0c']:
                pair = "GBPAUD"
                text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom DollorHiest"
                bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
            elif pair == [' \n', '\n', '|\n', ':\n', ',- FE\n', '_~ ££\n', '\n', 'New Zealand Dollar American Dollar\n', '\n', 'a\n', 'ST OAR)\n', 'Bice\n', '\n', '@DollarHeistOfficial #DollarHeist\n', '\x0c']:
                pair = "NZDUSD"
                text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom DollorHiest"
                bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
            else:
                print(pair)
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
        subprocess.run(["tesseract","--dpi", "70","downloads/"+img_name,text_file])
        text= text_file+".txt"
        f = open(text,'r')
        pair = f.readlines()
        if pair == ['#PIPS30\n', '\n', 'a\n', 'a\n', 're}\n', 'oO\n', '\n', ' \n', '\n', 'AMERICAN DOLLAR\n', '\n', 'Fe\n', '\n', "PIPS'\n", '\x0c']:
            pair = "XAUUSD"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom PIPS 30"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        elif pair ==  ['#PIPS3O\n', '\n', 'POUND STERLING\n', '\n', 'A\n', '\n', 'JAPANESE YEN\n', '\n', ' \n', '\n', 'lo\n', '.\n', '\x0c']:
            pair = "GBPJPY"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom PIPS 30"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        elif pair ==  ['oa #PIPS30\n', '\n', ' \n', '\n', 'NEW ZEALAND DOLLAR\n', '\n', ' \n', '\n', ' \n', '\n', 'AMERICAN DOLLAR\n', '\n', ' \n', '\n', ' \n', '\x0c'] :
            pair = "NZDUSD"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom PIPS 30"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        elif pair == ['#PIPS3O\n', '\n', 'P\n', '\n', 'POUND STERLING\n', '\n', '0 14 piu GEST)\n', '\n', ' \n', '\n', 'AMERICAN DOLLAR\n', '\n', ' \n', '\n', ' \n', '\n', 'aa\n', '\x0c']:
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
        subprocess.run(["tesseract","--dpi", "70","downloads/"+img_name,text_file])
        text= text_file+".txt"
        f = open(text,'r')
        pair = f.readlines()
        if pair == ['we\n', '\n', 'ro.\n', '\n', ' \n', '\n', 'Oyo #FMPXofficial #FULLMARGIN\n', '\x0c']:
            pair = "EURCAD"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom FMFX"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        elif pair == ['a\n', '\n', ' \n', '\n', 'Oyo #FMPXofficial #FULLMARGIN\n', '\x0c']:
            pair = "EURAUD"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom FMFX"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        elif pair == ['lz\n', '\n', 'CAD\n', '\n', 'Canadian dolla\n', '\n', '    \n', '  \n', ' \n', ' \n', '\n', '{i\n', '|\n', '1\n', 'i\n', '\n', 'Rete NZelAl\n', '!\n', '\n', 'f\n', '\n', 'Oyo #FMPXofficial #FULLMARGIN\n', '\x0c']:
            pair = "CADJPY"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom FMFX"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        elif pair == ['iz\n', '\n', 'GBP\n', '\n', 'Pound sterling\n', '\n', '    \n', '\n', 'Oyo #FMPXofficial #FULLMARGIN\n', '\x0c']:
            pair = "GBPAUD"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom FMFX"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        elif pair == ['ize\n', '\n', 'GBP\n', '\n', 'Pound sterling\n', '\n', '     \n', '  \n', '\n', '|\n', 'Japanese yen\n', '!\n', '\n', 'Oyo #FMPXofficial #FULLMARGIN\n', '\x0c']:
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
        subprocess.run(["tesseract","--dpi", "70","downloads/"+img_name,text_file])
        text= text_file+".txt"
        f = open(text,'r')
        pair = f.readlines()
        if pair == ['= og\n', '\n', 'USD / CHF\n', '\x0c']:
            pair = "USDCHF"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
        elif pair == ['\x0c']:
            subprocess.run(["tesseract","downloads/"+img_name,text_file])
            text= text_file+".txt"
            f = open(text,'r')
            pair = f.readlines()
            text = order+","+str(pair)+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
        elif pair == [' \n', '\n', 'EUR / AUD\n', '\x0c']:
            pair = "EURAUD"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)            
        elif pair == [' \n', '\n', 'NZD / CAD\n', '\x0c']:
            pair = "NZDCAD"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML) 
        elif pair == [' \n', '\n', 'NZD / JPY\n', '\x0c']:
            pair = "NZDJPY"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML) 
        elif pair == ['=—— @\n', '\n', 'USD / JPY\n', '\x0c']:
            pair = "USDJPY"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML) 
        elif pair ==  ['mF\n', 'Zin\n', '\n', 'GBP / AUD\n', '\n', ' \n', '\x0c']:
            pair = "GBPAUD"
            text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML) 
        elif pair == ['ivi Ea\n', '\n', 'CAD / CHF\n', '\x0c']:
            pair = "CADCHF"
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


bot.run()
