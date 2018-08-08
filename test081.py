#! /usr/bin/env python
#! -*- coding: utf-8 -*-
#调用接口去实现

import smtplib
from email.mime.text import MIMEText
from email.header import Header

#第三方 SMTP 服务
mail_host = "smtp.qq.com" #设置服务器
mail_user = "38833263@qq.com" #用户名
mail_pass = "Hhz14572400" #秘钥

sender = '走你'
receivers = ['haozhehan@e-to-china.com'] #接受邮件
message = MIMEText('python 邮件发送测试。。。', 'plain', 'utf-8')
message['From'] = Header('测试邮件','utf-8')
message['To'] = Header ('测试', 'utf-8')

subject = 'python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj =smtplib.SMTP()
    smtpObj.connect(mail_host, 587)  # 25为SMTP端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print ('邮件发送成功')
except smtplib.SMTPException:
    print ('Error: 无法发送邮件')