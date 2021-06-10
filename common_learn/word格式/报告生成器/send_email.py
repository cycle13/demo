#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 16:47
# @Author  : Yanjun Wang
# @Site    : 
# @File    : send_email.py
# @Software: PyCharm


import smtplib    #发邮件
from email.mime.text import MIMEText   #邮件文字
from email.mime.multipart import MIMEMultipart


def sendemail(to_email,file_name,text):
    msg=MIMEMultipart()
    msg['from'] = '1419169425@qq.com'+'<'+'王彦军'+'>'
    msg['to'] = to_email
    msg['subject'] = '邮件标题：用python自动发送的邮件'
    txt=MIMEText(text,'plain','utf-8')
    msg.attach(txt)
    #构造附件1
    att1=MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="file.docx"'   #这里的filename可以任意写，写什么名字，邮件中显示什么名字
    msg.attach(att1)
    try:
        server = smtplib.SMTP_SSL('smtp.qq.com')      #构造邮件传输服务
        server.connect(host='smtp.qq.com',port=465)   #连接qq邮件host
        server.login('1419169425@qq.com','pkomkdidkgkzghai')#前为用户名，后为密码
        server.sendmail(msg['from'], msg['to'],msg.as_string())   #从哪到哪，传邮件
        server.quit()  #退出邮件服务
        print('发送成功')
    except Exception as e:
        print(str(e))
    exit()
