#!/usr/bin/ python
# coding=utf-8
"""
*Author: team of develop platform(vmaxx)
*Date:2018-10
*The source code made by our team is opened
*Take care of it please and welcome to update it 
"""
import multiprocessing
import sys
import os
import threading
from multiprocessing import Process
from pdf_daily_data import PdfDailyData

from pdf_lib.pdf_date import PdfDate
sys.path.append('../')
from Pdf_Daily import PdfDaily
import logging
import argparse
import json
import time
from sendemail.send_email import SendEmail
from pdf_lib.pdf_config import PdfConfig

parser = argparse.ArgumentParser()
parser.add_argument("--date", help="pdf date")
args = parser.parse_args()
pdf_date = args.date
report_output_log_path = './log'

if not os.path.exists(report_output_log_path):
    try:
        os.mkdir(report_output_log_path, 0777)
        os.chmod(report_output_log_path, 0777)
    except Exception as e:
        print e

email_config_path = os.path.join(os.getcwd(), "../receiver_config.json")
email_recever = []
if os.path.exists(email_config_path):
    with open(email_config_path) as f:
        alert_time_config = json.loads(f.read())
        email_recever = alert_time_config["email_recever"]

if __name__ == "__main__":
    if not pdf_date:
        print "ERROR please input  right arguments or input ./Pdf_launcher -h"
    else:
        config_object = PdfConfig.param_init(pdf_date)
        print config_object.pdf_time

        config_object.pdf_time_type = "Daily"
        config_object.pdf_report_type = "Pedestrain"
        # email_object = SendEmail()

        pdf_start_time = time.ctime()

        PdfDaily_object = PdfDaily(config_object)

        logging.basicConfig(filename='./{}/{}.log'.format(report_output_log_path, PdfDaily_object.pdf_name),
                            filemode='a+',
                            level=logging.INFO,
                            format='\n %(asctime)s %(filename)s %(funcName)s[line:%(lineno)d] %(levelname)s %(message)s \n',
                            datefmt='%a, %d %b %Y %H:%M:%S')
        logger = logging.getLogger(__name__)
        PdfDaily_object.draw_page_one()
        pass
        PdfDaily_object.draw_page_end()
        PdfDaily_object.pdf_save()
        pdf_url = PdfDaily_object.pdf_upload(debug=config_object.pdf_enironment)
        if not pdf_url:
            print "upload error"
            logger.error("upload error")
        else:
            print pdf_url
            logger.info(pdf_url)
            flag = PdfDaily_object.daily_report_insert_database(pdf_url, PdfDaily_object.daily_report_start_time)
            if not flag:
                logger.error("generate report error")
            else:
                print "generate report successful"
                logger.info("generate report successful")

        pdf_end_time = time.ctime()
