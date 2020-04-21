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
import time
import logging
import sys
import multiprocessing
from multiprocessing import Process

from reportlab.lib.colors import Color

sys.path.append('../')
from pdf_lib.pdf_ui import *
from pdf_lib.pdf_date import PdfDate
from pdf_daily_data import PdfDailyData

logger = logging.getLogger(__name__)


class PdfDaily(PdfUI, PdfDate, PdfDailyData):

    def __init__(self, pdf_config_object):
        self.pdf_config_object = pdf_config_object
        PdfUI.__init__(self, pdf_config_object)
        PdfDate.__init__(self, self.pdf_config_object.pdf_time)
        PdfDailyData.__init__(self)
        self.__daily_data_init()

    def __daily_data_init(self):
        self.__report_start_hour = " 06:00:00"
        self.__report_end_hour = " 22:59:59"
        self.report_start_hour_1 = " @ 06:00 AM"
        self.report_end_hour_1 = " @ 09:59 PM"

        self.daily_start_time_week_month_day_year, self.daily_end_time_week_month_day_year = self.get_daily_range_time_week_month_day_year(
            self.pdf_config_object.pdf_time)
        self.__daily_start_time_month_day, self.__daily_end_time_month_day_ = self.get_daily_range_time_month_day(
            self.pdf_config_object.pdf_time)
        self.daily_start_time_month_day_year, self.daily_end_time_month_day_year = self.get_daily_range_time_month_day_year(
            self.pdf_config_object.pdf_time)
        self.daily_start_time_month_day = self.__daily_start_time_month_day + self.report_start_hour_1
        self.daily_end_time_month_day = self.__daily_end_time_month_day_ + self.report_end_hour_1

        self.daily_report_start_time, self.daily_report_end_time = self.get_daily_rangetime(
            self.pdf_config_object.pdf_time)
        self.__daily_report_start_time = self.daily_report_start_time + self.__report_start_hour
        self.__daily_report_end_time = self.daily_report_end_time + self.__report_end_hour

        self.daily_start, self.daily_end = self.get_month_rangetime()
        self.daily_start = self.get_daily_range_time_day_month(self.daily_start)
        self.daily_start = self.get_daily_range_time_day_month(self.daily_end)
        self.daily_start = self.daily_start + self.__report_start_hour
        self.daily_end = self.daily_start + self.__report_end_hour
        self.daily_start_time = self.get_daily_range_time_day_month(self.daily_start)
        self.daily_end_time = self.get_daily_range_time_day_month(self.daily_end)

        self.__zone_data_list = self.get_zone_id_name()

    def draw_page_one(self):
        self.pdf_page_object.setFillColor(HexColor(0X8FAADC))
        self.pdf_page_object.rect(45, 2950, 2460, 300, fill=True, stroke=False)
        client_logo_path = self.pdf_config_object.pdf_client_profile["logo"]["image_path"]
        company_logo_path = self.pdf_config_object.pdf_company_profile["company_logo1"]["image_path"]

    ## 逻辑部分：使用现有画图工具展示数据。

    def draw_page_end(self):
        pass
