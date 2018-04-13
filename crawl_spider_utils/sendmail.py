# -*- coding:utf-8 -*-

"""
File Name : 'intf_sendmail'.py
Description:
Author: 'wangtao'
Date: '2015/12/22' '11:11'
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

import os


def example_intf_send_mail():
    """
    样例代码
    :return:
    """
    to = ['mime-spider@mi-me.com']
    subject = u'脚本运行提醒'
    text = u'脚本运行提醒'
    # files = ['sendmail.py']
    # intf_send_mail(to,subject,text,files)
    intf_send_mail(to, subject, text)


def intf_send_mail(to, subject, text, files=[]):
    """
    发送邮件的接口，支持添加附件
    :param to:       邮件接收方
    :param subject:  邮件主题
    :param text:     邮件内容
    :param files:    附件路径
    :return:
    """
    server = {'name':'smtp.sina.com', 'user':'mime_spider@sina.com', 'passwd':'Mime@s_159_p', 'port':25}
    fro = 'mime_spider@sina.com'
    send_mail(server, fro, to, subject, text, files=[])


def send_mail(server, fro, to, subject, text, files=[]):
    assert type(server) == dict
    assert type(to) == list
    assert type(files) == list

    msg = MIMEMultipart()
    msg['From'] = fro
    msg['Subject'] = subject
    msg['To'] = COMMASPACE.join(to) # COMMASPACE==', '
    msg['Date'] = formatdate(localtime=True)
    msg.attach(MIMEText(text, 'plain', 'utf-8'))

    for f in files:
        part = MIMEBase('application', 'octet-stream') # 'octet-stream': binary data
        part.set_payload(open(f, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)

    smtp = smtplib.SMTP(server['name'], server['port'])
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(server['user'], server['passwd'])
    smtp.sendmail(fro, to, msg.as_string())
    smtp.close()


if __name__ == '__main__':
    example_intf_send_mail()
