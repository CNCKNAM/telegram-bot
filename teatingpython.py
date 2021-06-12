import os
import re
import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


try:
    from telethon.sync import TelegramClient
    from telethon import TelegramClient,events,sync
    from telethon import functions,types
except:
    os.system('pip install telethon')
    from telethon.sync import TelegramClient
    from telethon import TelegramClient,events,sync
    from telethon import functions,types
from datetime import date
from datetime import datetime

# Remember to use your own values from my.telegram.org!
api_id = "5943911"
api_hash = '22718cdcda3def8d32497b2c2a0a61bf'
phone = "+85251049768"
client = TelegramClient('anon', api_id, api_hash)
client.start()

allowchannel = ["-1001296795110", "-1001471598328"]

#time
@client.on(events.NewMessage(incoming= True,outgoing=True,pattern=r'(?i).*^/time$'))
async def handler(event):
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    await event.reply("現在時間"+dt_string)   

#date
@client.on(events.NewMessage(incoming= True,outgoing=True,pattern=r'(?i).*^/date$'))
async def handler(event):
    today = date.today()
    d1 = today.strftime("%Y年%m月%d日")
    await event.reply("今日係"+d1)   

#teapot    
@client.on(events.NewMessage(incoming= True,outgoing=True,pattern=r'(?i).*^@teapot|teapot$'))
async def handler(event):
    chat_id = event.chat_id
    msg = event.id
    await client.send_file(chat_id, file='teapot.mp3',voice_note=True,reply_to=event.id)
    await event.reply('咩事，我是茶壺肥又矮呀🫖🫖🫖')  

#monpo    
@client.on(events.NewMessage(incoming= True,outgoing=True,pattern=r'(?i).*^monpo$'))
async def handler(event):
    chat_id = event.chat_id
    msg = event.id
    await client.send_file(chat_id, file='teapot.mp3',voice_note=True,reply_to=event.id)
    await event.reply('禾唔係')  
 
#gun
@client.on(events.NewMessage(incoming= True,outgoing=True,pattern=r'(?i).*^\.gun$'))
async def handler(event):
    await event.reply('dim gun')    

#笑死
@client.on(events.NewMessage(incoming= True,outgoing=False,pattern=r'(?i).*^笑死$'))
async def handler(event):
    await event.reply('笑笑笑,有咩咁好笑呀') 

#點跟
@client.on(events.NewMessage(incoming= True,outgoing=False,pattern=r'(?i).*^點跟$'))
async def handler(event):
    await event.reply('等陣,跟唔到')       

#早晨
@client.on(events.NewMessage(incoming= True,outgoing=False,pattern=r'(?i).*^早晨呀!$'))
async def handler(event):
    await event.reply('等陣,跟唔到')  

#錦鯉
@client.on(events.NewMessage(incoming= True,outgoing=True,pattern=r'(?i).*^錦鯉$'))
async def handler(event):
    await event.reply('幾時死??')  

#やめてください
@client.on(events.NewMessage(incoming= True,outgoing=True,pattern=r'(?i).*^\$yamete$'))
async def handler(event):
    chat_id = event.chat_id
    msg = event.id
    await client.send_file(chat_id, file='YameteKudasai.mp3',voice_note=True,reply_to=event.id)

#ahh
@client.on(events.NewMessage(incoming= True,outgoing=True,pattern=r'(?i).*^\$ahh$'))
async def handler(event):
    chat_id = event.chat_id
    msg = event.id
    await client.send_file(chat_id, file='Ahh.ogg',voice_note=True,reply_to=event.id)

#loveu
@client.on(events.NewMessage(incoming= True,outgoing=True,pattern=r'(?i).*^\$loveu$'))
async def handler(event):
    chat_id = event.chat_id
    msg = event.id
    await client.send_file(chat_id, file='loveu.mp3',voice_note=True,reply_to=event.id)

#sor9ry
@client.on(events.NewMessage(incoming= True,outgoing=True,pattern=r'(?i).*^\$sor9ry$'))
async def handler(event):
    chat_id = event.chat_id
    msg = event.id
    await client.send_file(chat_id, file='sor9ry.mp3',voice_note=True,reply_to=event.id)
    
#paydresponse
@client.on(events.NewMessage(incoming= True,outgoing=True,pattern=r'(?i).*^\$sor9ry$'))
async def handler(event):
    chat_id = event.chat_id
    msg = event.id
    await client.send_file(chat_id, file='paydresponse.mp3',voice_note=True,reply_to=event.id)    

#salty
@client.on(events.NewMessage(incoming= True,outgoing=True,pattern=r'(?i).*^\$saltygrp$'))
async def handler(event):
    chat_id = event.chat_id
    msg = event.id
    await client.send_file(chat_id, file='saltygrp.mp3',voice_note=True,reply_to=event.id) 
    
#mud9group
@client.on(events.NewMessage(incoming= True,outgoing=True,pattern=r'(?i).*^\$mud9grp$'))
async def handler(event):
    chat_id = event.chat_id
    msg = event.id
    await client.send_file(chat_id, file='mud9grp.mp3',voice_note=True,reply_to=event.id) 

#laughmud9
@client.on(events.NewMessage(incoming= True,outgoing=True,pattern=r'(?i).*^\$laughmud9$'))
async def handler(event):
    chat_id = event.chat_id
    msg = event.id
    await client.send_file(chat_id, file='laughmud9.mp3',voice_note=True,reply_to=event.id) 

#tospeech
@client.on(events.NewMessage(incoming= True,outgoing=True,pattern=r'(?i).*^\$tospeech$'))
async def handler(event):
    chat_id = event.chat_id
    if event.is_reply:
        replied = await event.get_reply_message()
        reply_raw_text = replied.raw_text
        engine.save_to_file(reply_raw_text, 'speech.mp3')
        engine.runAndWait()
        await client.send_file(chat_id, file='speech.mp3',voice_note=True,reply_to=event.id)

#totext
@client.on(events.NewMessage(incoming= True,outgoing=True,pattern=r'(?i).*^\$totext$'))
async def handler(event):
    chat_id = event.chat_id
    if event.is_reply:
        path = await message.download_media()
        print('File saved to', path) 
        

#check channel id
@client.on(events.NewMessage())
async def handler(event):
    #await client.send_file('me', 'test.mp3')
    entity = await client.get_entity('https://t.me/joinchat/9qhSImo0cChjMjZl')
    print(entity)
    print()

#print channel id
@client.on(events.NewMessage(incoming= True,outgoing=True,pattern=r'(?i).*^/cid$'))
async def handler(event):
    chat_id = event.chat_id
    await client.send_message(chat_id,"The channel id is "+ str(chat_id))

#print user id
@client.on(events.NewMessage(incoming= True,outgoing=True,pattern=r'(?i).*^/uid$'))
async def handler(event):
    chat_id = event.chat_id
    if event.is_reply:
        replied = await event.get_reply_message()
        sender = replied.sender_id
        await client.send_message(chat_id,"The user id is "+ str(sender))
  

#check join group          
@client.on(events.ChatAction)
async def handler(event):
    # Welcome every new user
    if event.user_joined:
        await event.reply('Welcome to the group!😘😘😘')

client.run_until_disconnected()