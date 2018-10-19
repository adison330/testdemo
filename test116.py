#! /usr/bin/env python
#! -*- coding: utf-8 -*-

from wxpy import *

turing = Tuling(api_key = '你的apikey')
bot = Bot()

#只跟某一个好友聊天，比如你的好友昵称是”甯“
xianding = bot.friends().search('甯')
@bot.register(chats = xianding)
def communite(msg):
    resp = turing.do_reply(msg)
bot.join()