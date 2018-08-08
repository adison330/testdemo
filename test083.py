#! /usr/bin/env python
#! -*- coding: utf-8 -*-

url = 'https://game.weixin.qq.com/cgi-bin/gamewap/getpubgmdatacenterindex?' \
      'openid=%s&plat_id=0&uin=&key=&pass_ticket=%s' % (openid, settings.pass_ticket)
r = requests.get(url = url, cookies = settings.def_cookies, headers = settings.def_headers,
                 timeout = (5.0,5.0))
tmp = r.json()
wfile = os.path.join(settings.Res_UserInfo_Dir, '%s.txt' % (rediskeys.user(openid)))

with codecs.open(wfile,'w','utf-8') as wf:
    wf.write(simplejson.dumps(tmp,indent = 2, sort_keys = True, ensure_ascii = False))



def user_battle_list(openid)
    return 'ubl_%s' % (openid)

#在提取battle list 之前，首先判断这名用户的数据是否已经提取过了
if settings.DaraRedis.get(rediskeys.user_battle_list(openid))
    return True
# 在提取battle list之后，需要自redis中记录用户信息
settings.DataRedis.set(rediskeys.user_battle_list(openid))
