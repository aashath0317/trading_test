
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

string = "BQCtCiTZEOcE50X0ht6xsaXZFFQTKEFwARj1cz8FHS_KzKdhrXWENYI7-pZCI-vMPqv2ZEhsXoAPwpwRKMkRTzU6tZ6Hgr9Xw8DGGsfy1BeuK1XX3iuxXbakHD_iv8MZlT40hap6VDff16lk7GTvbPn851gtMRjrUCKEHt-8LLBSS8f7Qq-zh18qG8imp_RiBKJVJvujLuCAU2YSXsdNGJvF6Y5le4O3qpllxXjHJkGhbzgNNpkvRE8SsaLc8Cggl56Qdg-MQTrpIpGsS84ChgLNVxJ5-5cLu_nf0z2LfwoiS6Mdedf-G6LXbQF4_oE2jt5e5zbV0Za_vFBnCwFMlhdXS-cCEgA"
bot = Client(string, api_id = 3030128,api_hash = 'cfc3885f5d2cbdbc5f10e6a643de2711')


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
    send_channel = message.chat.title
    photo_uid = message.chat.photo.big_photo_unique_id
    u_name = message.chat.username
    pair = ""
    m = 1375658509
    filetype = message.photo
    filetype_text = message.text
    need = 0 
    '''                                      # GETTING TP ,SL, ORDER, Professor pair and setting working only signal
    msg = str(message)
    with open('title.txt', 'w') as f:
        f.writelines(msg)      
    bot.send_document(chat_id=chat_id, document="title.txt", caption="from "+send_channel)
    '''
    if send_channel == "DOLLARHEIST" or u_name == "dollarheistofficial" and not filetype == None:   #dolor_heist
        try:
            mssg = message.caption
            bot.send_message(chat_id=m, text=mssg, parse_mode=telegram.ParseMode.HTML)
            signal_s = message.caption.split("\n")
            order_s = signal[0].split("@")[0].strip(" ")        
            price_s = str(signal[0].split("@")[1].strip(" "))
            tp_s = str(signal[2].split(" ")[2])
            mssg = signal_s+"\n"+order_s+"\n"+price_s+"\n"+tp_s
            bot.send_message(chat_id=m, text=mssg, parse_mode=telegram.ParseMode.HTML)
            img_name = "dolor_heist.jpg"
            text_file = "dolor_hiest_text"  
            signal = message.caption.split("\n")
            order = signal[0].split("@")[0].strip(" ")        
            price = float(signal[0].split("@")[1].strip(" "))
            tp = float(signal[2].split(" ")[2])
            try:
                sl = float(signal[5].split(" ")[4])
            except IndexError:
                sl = float(signal[5].split(" ")[2])
            if price < tp and price > sl and order == "BUY NOW":
                need = 1
            elif price > tp and price < sl and order == "SELL NOW":
                need = 1
            else:
                msg = "Something wrong is this signal Order.. not triggered From DollorHiest"
                bot.send_message(chat_id=m, text=msg, parse_mode=telegram.ParseMode.HTML)
                need = 0
        except IndexError:
            need = 0
            

 
    elif send_channel == "PIPS30" or u_name == "PIPS30official" and not filetype == None:
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
                bot.send_message(chat_id=m, text=msg, parse_mode=telegram.ParseMode.HTML)
            tp = float(signal[2].split(" ")[1])
            sl = float(signal[5].split(" ")[2])

            if price < tp and price > sl and order == "BUY NOW":
                need = 1
            elif price > tp and price < sl and order == "SELL NOW":
                need = 1
            else:
                msg = "Something wrong is this signal Order.. not triggered From PIPS30"
                bot.send_message(chat_id=m, text=msg, parse_mode=telegram.ParseMode.HTML)
                need = 0
        except IndexError or ValueError:
            need = 0

    elif send_channel == "M15 Signals" and not filetype == None:
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
                bot.send_message(chat_id=m, text=msg, parse_mode=telegram.ParseMode.HTML)
                need = 0
            tp = float(signal[2].split(" ")[1])
            sl = float(signal[5].split(" ")[1])            
            if price < tp and price > sl and order == "BUY NOW":
                need = 1
            elif price > tp and price < sl and order == "SELL NOW":
                need = 1
            else:
                msg = "Something wrong is this signal Order.. not triggered From M15"
                bot.send_message(chat_id=m, text=msg, parse_mode=telegram.ParseMode.HTML)
                need = 0
        except IndexError or ValueError:
            need = 0

    elif send_channel == "Forex Trading Professor" or u_name == "professoroff" and filetype == None and not filetype_text == None:
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
                bot.send_message(chat_id=m, text=msg, parse_mode=telegram.ParseMode.HTML)
                need = 0
        except IndexError or AttributeError:
            need =0


    # Process               DollorHiest Complete
    if send_channel == "DOLLARHEIST" or u_name == "dollarheistofficial" and need == 1:
        price = str(price)
        bot.download_media(file_name=img_name,message=message)
        subprocess.run(["tesseract","--dpi", "70","downloads/"+img_name,text_file])
        text= text_file+".txt"
        f = open(text,'r')
        pair = f.readlines()        
                                  # CHECKING PAIR IN DOLLOR_HIEST
        if pair == ['m2\n', 'iN\n', '\n', ' \n', '\n', 'Satie eye lites Japanese Yen\n', 'Ora\n', '@DollarHeistOfficial #DollarHeist WEIST\n', '\x0c']:
             pair = "GBPJPY"
             text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom DollorHiest"
             bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
        elif pair == [' \n', '\x0c']:
             pair = "EURAUD"
             text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom DollorHiest"
             bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
        elif pair == [' \n', '\n', 'Australian Dollar American Dollar\n', '\n', 'a\n', 'ST OAR)\n', 'Bice\n', '\n', '@DollarHeistOfficial #DollarHeist\n', '\x0c']:
             pair = "AUDUSD"
             text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom DollorHiest"
             bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
        elif pair == [' \n', '\n', 'Euro Japanese Yen\n', '\n', 'ee ea\n', 'OLLA\n', 'SC a\n', '\n', '@DollarHeistOfficial #DollarHeist\n', '\x0c']:
             pair = "EURJPY"
             text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom DollorHiest"
             bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
        elif pair == [' \n', '\n', '2\n', 'q\n', '\n', 'Satie eye lites Australian Dollar\n', 'Sg\n', '@DollarHeistOfficial #DollarHeist Eh y\n', '\x0c']:
             pair = "GBPAUD"
             text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom DollorHiest"
             bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
        elif pair == [' \n', '\n', '|\n', ':\n', ',- FE\n', '_~ ££\n', '\n', 'New Zealand Dollar American Dollar\n', '\n', 'a\n', 'ST OAR)\n', 'Bice\n', '\n', '@DollarHeistOfficial #DollarHeist\n', '\x0c']:      
             pair = "NZDUSD"
             text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom DollorHiest"
             bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
        else:
            caption = f'I cant resolve this photo From {send_channel} \n\n'
            photo = "downloads/"+img_name
            caption += f'Uniq string is:\n( {str(pair)} )'
            bot.send_photo(chat_id=m, caption=caption, photo=photo)
            bot.send_document(chat_id=m, document=text_file+".txt", caption="This is File Uniq string file")
            msg = str(message)
            with open('title.txt', 'w') as f:
                    f.writelines(msg)      
            bot.send_document(chat_id=m, document="title.txt", caption="from "+send_channel)
            msg = "What is this i don't know about this From DollorHeist\n\n"
            msg += text
            bot.send_message(chat_id=m, text=msg, parse_mode=telegram.ParseMode.HTML)
                           
     
    # pips30 Complete
    elif send_channel == "PIPS30" or u_name == "PIPS30official" and need == 1:
        price = str(price)
        bot.download_media(file_name=img_name,message=message)
        subprocess.run(["tesseract","--dpi", "70","downloads/"+img_name,text_file])
        text= text_file+".txt"
        f = open(text,'r')
        pair = f.readlines()
        if pair == ['#PIPS30\n', '\n', 'a\n', 'a\n', 're}\n', 'oO\n', '\n', ' \n', '\n', 'AMERICAN DOLLAR\n', '\n', 'Fe\n', '\n', "PIPS'\n", '\x0c'] or ['#PIPS3O0\n', '\n', 'fay\n', 'a\n', 'ce}\n', 'oO\n', '\n', ' \n', '\n', 'AMERICAN DOLLAR\n', '\n', 'Fe\n', '\n', "PIPS'\n", '\x0c']:
            pair = "XAUUSD"
            text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom PIPS 30"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        elif pair ==  ['#PIPS3O\n', '\n', 'POUND STERLING\n', '\n', 'A\n', '\n', 'JAPANESE YEN\n', '\n', ' \n', '\n', 'lo\n', '.\n', '\x0c']:
            pair = "GBPJPY"
            text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom PIPS 30"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        elif pair ==  ['oa #PIPS30\n', '\n', ' \n', '\n', 'NEW ZEALAND DOLLAR\n', '\n', ' \n', '\n', ' \n', '\n', 'AMERICAN DOLLAR\n', '\n', ' \n', '\n', ' \n', '\x0c'] :
            pair = "NZDUSD"
            text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom PIPS 30"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        elif pair == ['#PIPS3O\n', '\n', 'P\n', '\n', 'POUND STERLING\n', '\n', '0 14 piu GEST)\n', '\n', ' \n', '\n', 'AMERICAN DOLLAR\n', '\n', ' \n', '\n', ' \n', '\n', 'aa\n', '\x0c']:
            pair = "GBPUSD"
            text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom PIPS 30"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
  
        #elif pair == "lk":
        #    pair = "XAUUSD"
        #    text = order+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom PIPS 30"
        #    bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

        else:
            caption = f'I cant resolve this photo From {send_channel} \n\n'
            photo = "downloads/"+img_name
            caption += f'Uniq string is:\n( {str(pair)} )'
            bot.send_photo(chat_id=m, caption=caption, photo=photo)
            bot.send_document(chat_id=m, document=text_file+".txt", caption="This is File Uniq string file")  
            msg = str(message)
            with open('title.txt', 'w') as f:
                f.writelines(msg)      
            bot.send_document(chat_id=m, document="title.txt", caption="from "+send_channel)
 
    elif send_channel == "Forex Trading Professor" or u_name == "professoroff" and need == 2:
        price = str(price)                
        text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom Professor"
        bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
            
    elif send_channel == "M15 Signals" and need == 1:
        price = str(price)    
        bot.download_media(file_name=img_name,message=message)
        subprocess.run(["tesseract","--dpi", "70","downloads/"+img_name,text_file])
        text= text_file+".txt"
        f = open(text,'r')
        pair = f.readlines()
        if pair == ['= og\n', '\n', 'USD / CHF\n', '\x0c']:
            pair = "USDCHF"
            text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
        elif pair == [' \n', '\n', 'EUR / JPY\n', '\x0c']:
            pair = "EURJPY"
            text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
        elif pair == ['\x0c']:
            subprocess.run(["tesseract","downloads/"+img_name,text_file])
            text= text_file+".txt"
            f = open(text,'r')
            pair = f.readlines()
            if pair == ['WA a\n', '\n', 'GBP / USD\n', '\n', 'SW\n', '\x0c']:
                        pair = "GBPUSD"
                        text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
                        bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)      
            else:
                        pair = "GBPJPY"
                        text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
                        bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)    
        elif pair == [' \n', '\n', 'EUR / AUD\n', '\x0c']:
            pair = "EURAUD"
            text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)            
        elif pair == [' \n', '\n', 'NZD / CAD\n', '\x0c']:
            pair = "NZDCAD"
            text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML) 
        elif pair == [' \n', '\n', 'NZD / JPY\n', '\x0c']:
            pair = "NZDJPY"
            text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML) 
        elif pair == ['=—— @\n', '\n', 'USD / JPY\n', '\x0c']:
            pair = "USDJPY"
            text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML) 
        elif pair ==  ['mF\n', 'Zin\n', '\n', 'GBP / AUD\n', '\n', ' \n', '\x0c']:
            pair = "GBPAUD"
            text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML) 
        elif pair == ['ivi Ea\n', '\n', 'CAD / CHF\n', '\x0c']:
            pair = "CADCHF"
            text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML) 
        elif pair ==  ['AUD / CAD\n', '\n', ' \n', '\x0c']:
            pair = "AUDCAD"
            text = order+","+price+","+pair+","+str(tp)+","+str(sl)+" "+"  Triggering...\nFrom M15"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML) 
        else:
            print(pair)
            caption = f'I cant resolve this photo From {send_channel} \n\n'
            photo = "downloads/"+img_name
            caption += f'Uniq string is:\n( {str(pair)} )'
            bot.send_photo(chat_id=m, caption=caption, photo=photo)
            bot.send_document(chat_id=m, document=text_file+".txt", caption="This is File Uniq string file")
            msg = str(message)
            with open('title.txt', 'w') as f:
                f.writelines(msg)      
            bot.send_document(chat_id=m, document="title.txt", caption="from "+send_channel)
    else:
        pass


bot.run()
