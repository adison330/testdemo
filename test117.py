#! /usr/bin/env python
#! -*- coding: utf-8 -*-

from wxpy import *

turing = Tuling(api_key = '你的apikey')
bot = Bot()

#只在某个群内聊天，比如群名为
xianding = bot.groups().search('敢想敢干－机器人')
@bot.register(chats = xianding)
def communite(msg):
    turing.do_reply(msg)

bot.join()