#!/usr/bin/ python
# coding=utf-8
"""
*Author: team of develop platform(vmaxx)
*Date:2018-10
*The source code made by our team is opened
*Take care of it please and welcome to update it 
"""
import datetime
import json
import multiprocessing
import os
from multiprocessing import Lock
import sys
import time

import pytz

sys.path.append('../')
from pdf_lib.pdf_data import *

logger = logging.getLogger(__name__)


class PdfDailyData(PdfData):

    def __init__(self):

        super(PdfDailyData, self).__init__()
        # self.employee_id_list = self.get_enter_employee(time_start, time_end)

    def get_daily_property_entry(self, time_start, time_end):

        model_id = 121
        type_id = 62
        daily_property_object = None
        try:
            daily_property_object = self.get_property_entry(type_id, model_id, time_start, time_end)
        except Exception as e:
            print e
            logger.error(e)
        return daily_property_object

    def daily_report_insert_database(self, report_url, date):

        # company_id = 21
        # property_id = 121
        # type_id = 20
        # space_type = 24
        # report_type = 203
        company_id = 1
        property_id = 1
        type_id = 20
        space_type = 24
        report_type = 192
        flag = False
        try:
            flag = self.report_insert_database(company_id, property_id, report_url, date, type_id, report_type,
                                               space_type)
        except Exception as e:
            print e
            logger.error(e)
        return flag

    def get_zone_id_name(self):
        args = (17,)
        try:
            self.cur_object.callproc("report_zone_id", args)
            for result in self.cur_object.stored_results():
                self.zone_data = result.fetchall()
                break
        except Exception as e:
            logger.error(e)

        return self.zone_data

    def get_dwell_by_hour(self, zone_id, time_start, time_end):
        args = ('z', zone_id, time_start, time_end)
        hourly_dwell_list = []
        try:
            self.cur_object.callproc("fc_2_hourly_dwell", args)
            for result in self.cur_object.stored_results():
                self.hourly_dwell_list = result.fetchall()
                break
        except Exception as e:
            print e
        if self.hourly_dwell_list:
            hourly_dwell_list = self.hourly_dwell_list
        tmp_list = []
        for item in hourly_dwell_list:
            hour = str(item[1])
            hour = datetime.datetime.strptime(hour, '%Y-%m-%d %H:%M:%S')
            hour = hour.strftime('%I %p')
            dwell = int(item[2])
            tmp_list.append([hour, dwell])
        return tmp_list

if __name__ == '__main__':
    run = PdfDailyData()
   
