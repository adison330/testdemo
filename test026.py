#! /usr/bin/env python

while True:
    # TODO 显示系统主菜单

    action = input("请选择操作功能： ")

    print("您选择的操作是 %s" % action)

    #根据用户输入决定后续操作
    if action in ["1","2","3"]:
        pass
    elif action == "0":
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print("输入错误，请重新输入")