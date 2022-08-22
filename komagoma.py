#coding:UTF-8
import discord
from discord.ext import tasks
import datetime
import re
import random
import time
import sys
sys.setrecursionlimit(10000)
from asobi_list import kawaii_list
from asobi_list import ziho_list
from asobi_list import gacha_list
from asobi_list import gaba_list
import os

TOKEN = "TOKEN" #トークン
CHANNEL_ID = 12345 #チャンネルID
TEST_ID = 67890

# 接続に必要なオブジェクトを生成
client = discord.Client()

next_time = True

async def reply(message):
     if client.user != message.author:
        sakebu = message.author.display_name + "ｻﾝｶﾜｲｲﾔｯﾀｰ！"   # 返信メッセージの作成
        await message.channel.send(sakebu) # 返信メッセージを送信

# 60秒に一回ループ
@tasks.loop(seconds=5)
async def loop():
     await client.wait_until_ready()
     global next_time
     # 現在の時刻
     now = datetime.datetime.now().strftime('%H:%M')
     now_Japan = (datetime.datetime.now() + datetime.timedelta(hours = 9)).strftime('%H:%M')
     channel = client.get_channel(CHANNEL_ID)

     if re.fullmatch("[0-2][0-9]:00", now):
          if next_time:
               await channel.send("今ﾊ" + now_Japan + "ﾃﾞｽ")
               if now == "15:00":# 12時
                    await channel.send('〇〇ｻﾝｶﾜｲｲﾔｯﾀｰ!')
                    next_time = False

               elif now == "03:00":
                    await channel.send('〇〇ｻﾝｶﾜｲｲﾔｯﾀｰ!')
                    next_time = False
                    
               elif now == "18:00":# 18時と6時を指定すれば、3時に囀る
                    await channel.send('△△ｻﾝｶﾜｲｲﾔｯﾀｰ!')
                    next_time = False
                              
               elif now == "06:00":
                    await channel.send('△△ｻﾝｶﾜｲｲﾔｯﾀｰ!')
                    next_time = False

               elif now == "09:00":
                    m = random.choice(gaba_list) + "ｻﾝｶﾞﾊﾞｲｲﾔｯﾀｰ!"
                    await channel.send(m)
                    next_time = False

               elif now == "21:00":
                    m = random.choice(gaba_list) + "ｻﾝｶﾞﾊﾞｲｲﾔｯﾀｰ!"
                    await channel.send(m)
                    next_time = False

               else:
                    m = random.choice(ziho_list) + "ｻﾝｶﾜｲｲﾔｯﾀｰ!"
                    await channel.send(m)
                    next_time = False
                    
     else:
          next_time = "True"

@client.event
async def on_voice_state_update(member, before, after):

    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel(CHANNEL_ID)
        
        # 入室通知
        if after.channel.id == 1234567890:
            await botRoom.send("寝落ちした" + member.name + "さんｶﾜｲｲﾔｯﾀｰ!")

@client.event
async def on_message(message):

     if client.user in message.mentions: # 話しかけられたかの判定
          await reply(message) # 返信する非同期関数を実行

     else:
          if re.match("(さえず|囀)って|サエズッテ|ｻｴｽﾞｯﾃ", message.content):
               if client.user != message.author:
                    # メッセージを書きます
                    m = "〇〇ｻﾝｶﾜｲｲﾔｯﾀｰ！"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
                    return

          if re.match("(さえず|囀)るな|サエズルナ|ｻｴｽﾞﾙﾅ", message.content):
               if client.user != message.author:
                    m = "ｿﾝﾅｰ"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
                    return

          if re.search("(アルジ|主|ｱﾙｼﾞ)(ｻﾏ|サマ)", message.content):
               if client.user != message.author:
                    m = "ｱﾙｼﾞｻﾏ……"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
                    return
                
          if message.content.startswith("/kawaii"):
               if client.user != message.author:
                    m = message.content[7:] + "ｶﾜｲｲﾔｯﾀｰ！"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
                    return

          if message.content.startswith("/ikemen"):
               if client.user != message.author:
                    m = message.content[7:] + "ｶｯｺｲｲﾔｯﾀｰ！"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
                    return

          if message.content in kawaii_list:
               if client.user != message.author:
                    # メッセージを書きます
                    m = "ｵﾏｴﾓｶﾜｲｲ"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
                    return

          if 'ｶﾜｲｸﾅｲ' in message.content:
               if client.user != message.author:
                    m = "ﾊ?ｵﾏｴﾓｶﾜｲｲｶﾞ?"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
                    return

          if re.search("(私|わた.*し|ワタ.*シ|ﾜﾀ.*ｼ).*((以外|イガイ|ｲｶﾞｲ)(ノ|ﾉ|の)|((除|のぞ|ﾉｿﾞ)(い|イ|ｲ)(た|タ|ﾀ|て|テ|ﾃ)))", message.content):
               if message.author.id == 880592434554363934:
                    m = "ﾊ?ｵﾏｴﾓｶﾜｲｲｶﾞ?"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
                    return
               
          if re.match("(テスト|ﾃｽﾄ)…", message.content):
               if client.user != message.author:
                    m = "ﾃｽﾄｫ……"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
                    return

          if re.fullmatch("(エルフ|ｴﾙﾌ)(ｰ|ー|─)+(ﾝ|ン)", message.content):
               if client.user != message.author:
                    await message.channel.send("<:migawari:1003265684916154449><:Elfuun:1004356482663465012>")
                    return

          if re.match("〇〇(ｻﾝ|ﾁｬﾝ)ｶﾜｲｲﾔｯﾀｰ", message.content):
               if client.user != message.author:
                    await message.channel.send("<:emoji_8:957623561147809822>")
                    return

          if ':emoji_8:' in message.content:
               if client.user != message.author:
                    m = "ｴｰﾌｨｶﾜｲｲﾔｯﾀｰ!"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
                    return

          if re.search("イケメン、(参上|見参|登場)", message.content):
               if client.user != message.author:
                    await message.channel.send("<:emoji_3:950640769969061918>")
                    return

          if re.search("(天国|パライソ)夜雀", message.content):
               if client.user != message.author:
                    await message.channel.send("<:emoji_3:950640769969061918>ﾖﾝﾀﾞ？")
                    return

          if ':emoji_3:' in message.content in message.content:
               if client.user != message.author:
                    m = "参上、退場、あぁ無常"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
                    return

          if 'ﾀｲｼｨ' in message.content:
               if client.user != message.author:
                    m = "ﾀｲｼｨ……"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
                    return

          if ':_Enji_:' in message.content:
               if client.user != message.author:
                    m = "ｴﾝｼﾞｨ……"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
                    return

          if ':_Taishi01_:' in message.content:
               if client.user != message.author:
                    m = "ﾀｲｼｨ……"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
                    return

          if re.search("(み|に)ゃ", message.content):
               if message.author.id == user1 or message.author.id == user2 or message.author.id == user3:
                    m = "ﾈｺﾁｬﾝｶﾜｲｲﾔｯﾀｰ!"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
                    return
               
          if re.search("(m|n)ya", message.content):
               if message.author.id == user1 or message.author.id == user2 or message.author.id == user3:
                    m = "ﾈｺﾁｬﾝｶﾜｲｲﾔｯﾀｰ!"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
                    return

          if 'ｶﾜｲｲﾔｯﾀ' in message.content:
               if client.user != message.author:
                    if message.content.startswith("女の子ｶﾜｲｲﾔｯﾀｰ") or message.content.startswith("○ﾁｬﾝｶﾜｲｲﾔｯﾀｰ"):
                         # メッセージを書きます
                         m = "ｿﾚﾅ"
                         # メッセージが送られてきたチャンネルへメッセージを送ります
                         await message.channel.send(m)
                         return
                         
                    else:
                         m = "ﾜｶﾘﾐﾆｱﾌﾚﾙ"
                         # メッセージが送られてきたチャンネルへメッセージを送ります
                         await message.channel.send(m)
                         return

          if '時刻確認' in message.content:
               if client.user != message.author:
                    now = datetime.datetime.now().strftime('%H:%M')
                    now_Japan = (datetime.datetime.now() + datetime.timedelta(hours=9)).strftime('%H:%M')
                    await message.channel.send(random.choice(ziho_list))
                    await message.channel.send(now)
                    await message.channel.send(now_Japan)
                    await message.channel.send(next_time)

          if 'ガチャがしたい' in message.content:
               if client.user != message.author:
                    m = random.choice(gacha_list) + "ｻﾝｶﾜｲｲﾔｯﾀｰ!"
                    await message.channel.send(m)

          if message.content.endswith("をあがめよ"):
               if client.user != message.author:
                    m = message.content[:-5] + "ﾏｼﾞﾄｳﾄｲ……"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
                    return

          if message.content.endswith("を崇めよ"):
               if client.user != message.author:
                    m = message.content[:-4] + "ﾏｼﾞﾄｳﾄｲ……"
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)
                    return

          if re.search("(焼|や|ヤ|ﾔ)(き|ｷ|キ)(鳥|トリ|とり|ﾄﾘ)", message.content):
               if client.user != message.author:
                    await message.channel.send("ﾔﾝﾉｶｵﾗｰ")
                    return

          if re.search("(よし|ヨシ|ﾖｼ)(よし|ヨシ|ﾖｼ)+|(なで|ナデ|ﾅﾃﾞ)(なで|ナデ|ﾅﾃﾞ)+", message.content):
               if client.user != message.author:
                    if message.author.id != 873818631669182484:
                        m = message.author.display_name
                        await message.channel.send(m + "ﾏﾏｰ")
                        return

          if re.search("(廻鴉)(さん)*こっちです", message.content):
               if client.user != message.author:
                    gazoupath = os.path.abspath('mawarigarasu.png')
                    print(gazoupath)
                    file_obj = discord.File(gazoupath,filename="mawarigarasu.png")
                    await message.channel.send(file = file_obj)
                    return

          if re.fullmatch("110|１１０", message.content):
               if client.user != message.author:
                    gazoupath = os.path.abspath('mawarigarasu.png')
                    file_obj = discord.File(gazoupath,filename="mawarigarasu.png")
                    await message.channel.send(file = file_obj)
                    return

          if "スタッフクレジット" in message.content:
               if client.user != message.author:
                    await message.channel.send('スタッフクレジット')

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
