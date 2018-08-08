#! /usr/bin/env python
#! -*- coding: utf-8 -*-

@app.task(name = 'get_battle_list')

def get_battle_list(openid, plat_id = None, after_time = 0, update_time = None):
    # 判断是否已经取过用户战绩列表信息
    if settings.DataRedis.get(rediskeys.user_battle_list(openid)):
        return True

    if not plat_id:
        try:
            #提取用户信息
            us = handles.get_user_info_handles(openid)
            plat_id = us['plat_id']
        except Exception as e:
            print ('can not get user plat_id',openid, traceback.format_exc())
            return False
    #提取战绩列表
    battle_list = handles.get_battle_list_handle(openid,plat_id,after_time = 0, update_time = None)

    #为每一场战斗创建异步获取详情任务
    for room_id in battle_list:
        if not settings.DataRedis.get(rediskeys.user_battle(openid,room_id)):
            get_battle_info.delay(openid, plat_id, room_id)

    return True