#!/usr/bin/ python
# coding=utf-8
"""
*Author: team of develop platform(vmaxx)
*Date:2018-10
*The source code made by our team is opened
*Take care of it please and welcome to update it 
"""

import smtplib
import logging
import time
import os
from email.mime.text import MIMEText
from email.header import Header
import socket
import json
cur_dir = os.path.dirname(__file__)
# email_info_path = os.path.join(os.getcwd(), "sendemail/email_info.json")
email_info_path = "../sendemail/email_info.json"
logger = logging.getLogger(__name__)

class SendEmail(object):

    """The SendEmail API .
    Use this object to send email.  For example:
        email_object = SendEmail(email_sender,email_username, email_passwd, email_server, int(email_server_port))
        email_object.send_one_email(email_subject, receiver, email_content,timeout)
    """


    def __init__(self):

        try:
            if os.path.exists(email_info_path):
                with open(email_info_path,"r") as f:
                    email_info = f.read()
                    json_email_info = json.loads(email_info)
            else:
                print "email not find"
        except Exception as e:
            print email_info_path
            raise e
        email_sender = json_email_info["email_sender"]
        email_username = json_email_info["email_username"]
        email_passwd = json_email_info["email_passwd"]
        email_server = json_email_info["email_server_type"]
        email_server_port = json_email_info["email_server_port"]
        self.email_sender = email_sender
        self.email_username = email_username
        self.email_passwd = email_passwd
        self.email_server = email_server
        self.email_server_port = int( email_server_port)



    def send_email(self, email_subject, email_receiver, email_content,email_content_type,timeout):


        """
        args:
        @email_subject      (type:str)                  :email subject
        @email_receiver     (type:list)                 :email's receiver 
        @email_content                                  :email's content ,and he's type depends on email_content_type
        @email_content_type (type:"html" or "plain")    :email's content type
        @timeout            (type:int)                  :during the send email ,the maximum allowable timeout 
        """

        socket.setdefaulttimeout(timeout)
        email_server_object = self.email_server
        email_content_object = MIMEText(email_content, email_content_type, 'utf-8')
        email_content_object['Subject'] = Header(email_subject, 'utf-8')
        email_content_object['From'] = Header(self.email_sender)
        email_content_object['To'] = Header(','.join([]))
        email_content_object['Bcc'] = Header(','.join(email_receiver))
        try:
            smtp_object = smtplib.SMTP()
            smtp_object.connect(host=email_server_object, port=self.email_server_port)
            smtp_object.starttls()
            smtp_object.login(self.email_username, self.email_passwd)
            smtp_object.sendmail(self.email_username, email_receiver, email_content_object.as_string())
            smtp_object.close()
            return True
        except Exception as e:
            print e
            raise e
            return False





