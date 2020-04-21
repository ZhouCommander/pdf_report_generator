#!/usr/bin/ python
# coding=utf-8
"""
/*******************************************************************************
 * Deep North Confidential
 * Copyright (C) 2018 Deep North Inc. All rights reserved.
 * The source code for this program is not published
 * and protected by copyright controlled
 *******************************************************************************/
"""

import logging
import pytz
import datetime
import time
import os
import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

# ===== Step 2: scheduler config

schedule_log_path = './schedule_log'
if not os.path.exists(schedule_log_path):
    try:
        os.mkdir(schedule_log_path, 777)
        os.chmod(schedule_log_path, 777)
    except Exception as e:
        print e

schedule_pathname = 'schedule_log'
schedule_time = time.strftime('%Y-%m-%d', time.localtime())

logging.basicConfig(filename='./{}/{}.log'.format(schedule_pathname, schedule_time),
                    filemode='w',
                    level=logging.INFO,
                    format='\n %(asctime)s %(filename)s %(funcName)s[line:%(lineno)d] %(levelname)s %(message)s \n',
                    datefmt='%a, %d %b %Y %H:%M:%S')
logger = logging.getLogger('Schedule')

executors = {
    'default': ThreadPoolExecutor(100),
    'processpool': ProcessPoolExecutor(100)
}

job_defaults = {
    'coalesce': False,
    'max_instances': 100,
    'misfire_grace_time': None
}


def log_subprocess_output(pipe):
    for line in pipe.readline:
        print line
        # logging.info('got line from subprocess: %r', line)


def DailyJob():
    logger.info('process start')
    report_time_end = datetime.datetime.now(pytz.timezone('America/New_York'))
    report_time_start = report_time_end + datetime.timedelta(days=-1)
    report_time_start = datetime.datetime.strftime(report_time_start, "%Y-%m-%d")
    os.chdir('/home/ubuntu/thd_project/customizable-report/Daily/')
    print os.getcwd()
    cm = "python Pdf_Daily_generator.py --date {}".format(report_time_start)

    logger.info('process command ready')
    try:
        logger.info('step into trycatch successful')
        command_line_process = subprocess.Popen(cm, shell=True)
        logger.info('process finish successful')
    except Exception as e:
        print e
        logger.error('process step into trycatch error', e)


scheduler = BlockingScheduler(executors=executors, job_defaults=job_defaults, timezone='America/New_York')

scheduler.add_job(DailyJob, 'cron', day_of_week='mon-sun', hour=9, minute=0)

scheduler.start()
