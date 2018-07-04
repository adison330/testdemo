#!/usr/bin/env python
#编写两个代码 c_score 和 python_score,编写代码判断成绩
python_score = int(input("请输入python成绩： "))
c_score = int(input("请输出c 成绩： "))

#  要求只要一门成绩 >60 就算合格
if python_score > 60 or c_score > 60:
    print ("考试通过")
else:
    print ("再接再厉")