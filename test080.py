#! /usr/bin/env python
#! -*- coding: utf-8 -*-
#邮件发送
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = ''
receivers = ['adison330@163.com']

# 三个参数： 第一个为文本内容，第二个 plain 设置文本格式， 第三个 utf-8 设置编码
message = MIMEText('python 邮件测试...', 'plain', 'utf-8')
message['From'] = Header ("测试邮件", 'utf-8')  #发送者
message['To'] = Header ('测试', 'utf-8')  #接受者

subject = "python smtp 邮件测试"
message['subject'] = Header(subject, 'utf-8')

try:
    smtpobj = smtplib.SMTP('localhost')
    smtpobj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功！")
except smtplib.SMTPException:
    print ('Error: 无法发送邮件。')