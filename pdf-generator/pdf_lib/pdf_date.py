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
import datetime
import calendar


class PdfDate(object):

    def __init__(self, pdf_time):

        self.pdf_time = pdf_time

    def get_hour(self, pdf_time):

        try:
            time_hour = time.strftime("%I:00 %p", time.strptime(str(pdf_time), "%Y-%m-%d %H:%M:%S"))
            return time_hour
        except Exception as e:
            print e
            return None

    def get_next_hour(self, hour):

        if not hour:
            next_hour = None
        try:
            next_hour = datetime.datetime.strptime(hour, "%I %p")
            next_hour = (next_hour + datetime.timedelta(hours=1)).strftime("%I %p")
        except Exception as e:
            print e
            next_hour = None
        return next_hour

    def get_last_hour(self, hour):

        if not hour:
            next_hour = None
        try:
            next_hour = datetime.datetime.strptime(hour, "%I %p")
            next_hour = (next_hour + datetime.timedelta(hours=-1)).strftime("%I %p")
        except Exception as e:
            print e
            next_hour = None
        return next_hour

    def get_last_day(self, day):

        if not day:
            next_day = None
        try:
            next_day = datetime.datetime.strptime(day, "%Y-%m-%d")
            next_day = (next_day + datetime.timedelta(hours=-1)).strftime("%Y-%m-%d")
        except Exception as e:
            print e
            next_day = None
        return next_day

    def get_daily_time_start_format(self, year_month_day):
        start_time_date = datetime.datetime.strptime(year_month_day, '%Y-%m-%d')
        start_time_str = start_time_date.strftime('%m/%d/%Y')
        return start_time_str

    def get_hourly_timeformat(self):
        '''
        @function: get an hourly time and the format is " 05:00 PM 05:59 PM   "
        :return:
        '''
        # hour = self.get_hour(self.pdf_time)
        hour = self.pdf_time
        print 'hour:', hour
        if not hour:
            next_hour = None
        try:
            last_hour = datetime.datetime.strptime(hour, "%Y-%m-%d %H:%M:%S")
            last_hour_date = last_hour + datetime.timedelta(hours=-1)
            print last_hour_date
            last_hour = last_hour_date.strftime("%I:00 %p")
            # next_hour = (last_hour + datetime.timedelta(hours=-1)).strftime("%I:00 %p")
            print 'last_hour:', last_hour
            # next_hour = datetime.datetime.strptime(next_hour,"%I:00 %p")

            next_hour = (last_hour_date + datetime.timedelta(hours=1) - datetime.timedelta(seconds=1)).strftime(
                "%I:59 %p")
            print 'next_hour', next_hour
            first_num = int(next_hour.split(' ')[0].split(':')[0])
            second_num = next_hour.split(' ')[1]
            next_hour = str(first_num) + ':59' + ' ' + second_num

            last_hour = last_hour.split(' ')[0].split(':')[0] + ' ' + last_hour.split(' ')[1]
            first_num = int(last_hour.split(' ')[0].split(':')[0])
            second_num = last_hour.split(' ')[1]
            last_hour = str(first_num) + ' ' + second_num
        except Exception as e:
            print e
            next_hour = None
            last_hour = None
        return last_hour, next_hour

    def get_last_hourly_timeforamt(self, hour):
        '''
        @function: get an hourly time and the format is " 04:00 PM 04:59 PM   "
        :return:
        '''
        if not hour:
            next_hour = None
        try:
            last_hour = datetime.datetime.strptime(hour, "%I %p")
            last_hour = (last_hour + datetime.timedelta(hours=-1)).strftime("%I %p")
            last_hour = last_hour.split(' ')[0] + ':00' + ' ' + last_hour.split(' ')[1]
            next_hour = datetime.datetime.strptime(last_hour, "%I:00 %p")
            next_hour = (next_hour + datetime.timedelta(hours=1) - datetime.timedelta(seconds=1)).strftime("%I:59 %p")
            first_num = int(next_hour.split(' ')[0].split(':')[0])
            second_num = next_hour.split(' ')[1]
            next_hour = str(first_num) + ':59' + ' ' + second_num

            last_hour = last_hour.split(' ')[0].split(':')[0] + ' ' + last_hour.split(' ')[1]
            first_num = int(last_hour.split(' ')[0].split(':')[0])
            second_num = last_hour.split(' ')[1]
            last_hour = str(first_num) + ' ' + second_num
        except Exception as e:
            print e
            next_hour = None
            last_hour = None
        return last_hour, next_hour

    def cover_hourly_date(self):
        hourly_date = time.strptime(self.pdf_time, '%Y-%m-%d %H:%M:%S')
        hourly_date = time.localtime(int(time.mktime(hourly_date)) + 1800)
        hourly_date = time.strftime("%I %p", hourly_date)
        # print hourly_date
        return hourly_date

    def get_hourly_time_week_month_day_year(self):

        '''
        @function: get a hourly time and the format is " Mon, Sep 17, 2018"
        :return:
        '''
        hourly_date = time.strptime(self.pdf_time, '%Y-%m-%d %H:%M:%S')
        hourly_date = time.localtime(int(time.mktime(hourly_date)) - 3600)
        hourly_date = time.strftime("  %a, %b %d, %Y", hourly_date)
        # print hourly_date
        return hourly_date

    def get_hourly_time_month_day_year(self):
        '''
        @function: get a hourly time and the format is " Mon, Sep 17, 2018"
        :return:
        '''
        hourly_date = time.strptime(self.pdf_time, '%Y-%m-%d %H:%M:%S')
        hourly_date = time.localtime(int(time.mktime(hourly_date)))
        hourly_date = time.strftime(" %b %d, %Y", hourly_date)
        # print hourly_date
        return hourly_date

    def get_hourly_timerange(self):
        '''
        @function: get a hourly time range and the format is " (2018-10-18 18:00:00, 2018-10-18 18:59:59)"
        :return:
        '''

        start_time = time.strptime(self.pdf_time, "%Y-%m-%d %H:%M:%S")
        end_time = time.localtime(int(time.mktime(start_time) - 1))
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", end_time)
        start_time = time.localtime(int(time.mktime(start_time)) - 3600)
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", start_time)
        # print start_time, end_time
        return start_time, end_time

    def get_last_hourly_timerange(self):
        start_time = time.strptime(self.pdf_time, "%Y-%m-%d %H:%M:%S")
        end_time = time.localtime(int(time.mktime(start_time) - 3601))
        start_time = time.localtime(int(time.mktime(start_time) - 7200))
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", end_time)
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", start_time)
        # print start_time, end_time
        return start_time, end_time

    def get_hourly_timerange_from_begin_to_now(self):
        '''
        @function: get a hourly time range and the format is " (2018-10-18 09:00:00, 2018-10-18 18:00:00)"
        :return:
        '''
        end_time = time.strptime(self.pdf_time, "%Y-%m-%d %H:%M:%S")
        end_time = time.localtime(int(time.mktime(end_time) - 1))
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", end_time)
        start_time = self.pdf_time.split(" ")[0] + ' 06:00:00'
        # print start_time, end_time
        return start_time, end_time

    def get_last_year_day_hourly_timerange(self):
        start_time = time.strptime(self.pdf_time, "%Y-%m-%d %H:%M:%S")
        end_time = time.localtime(int(time.mktime(start_time) - 31449600 - 1))
        start_time = time.localtime(int(time.mktime(start_time) - 31449600 - 3600))
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", end_time)
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", start_time)
        # print start_time, end_time
        return start_time, end_time

    def get_last_year_day_last_hourly_timerange(self):
        start_time = time.strptime(self.pdf_time, "%Y-%m-%d %H:%M:%S")
        end_time = time.localtime(int(time.mktime(start_time) - 31449600 - 3601))
        start_time = time.localtime(int(time.mktime(start_time) - 31449600 - 7200))
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", end_time)
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", start_time)
        # print start_time, end_time
        return start_time, end_time

    def get_daily_range_time_week_month_day_year(self, year_month_day):

        '''
            @function: get a daily time and the format is " Mon, Sep 17, 2018"
        '''
        start_time = time.strptime(year_month_day, "%Y-%m-%d")
        end_time = time.localtime(int(time.mktime(start_time) + 86400))
        end_time = time.strftime("  %a, %b %d, %Y", end_time)
        start_time = time.strftime("  %a, %b %d, %Y", start_time)
        return start_time, end_time

    def get_daily_range_time_week_day_month_year(self, year_month_day):

        '''
            @function: get a daily time and the format is " Mon, Sep 17, 2018"
        '''
        start_time = time.strptime(year_month_day, "%Y-%m-%d")
        end_time = time.localtime(int(time.mktime(start_time) + 86400))
        end_time = time.strftime("  %a %d %b, %Y", end_time)
        start_time = time.strftime("  %a %d %b, %Y", start_time)
        return start_time, end_time

    def get_daily_range_time_month_day_year(self, year_month_day):

        start_time = time.strptime(year_month_day, "%Y-%m-%d")
        end_time = time.localtime(int(time.mktime(start_time) + 86400))
        end_time = time.strftime("  %b %d, %Y", end_time)
        start_time = time.strftime(" %b %d, %Y", start_time)
        return start_time, end_time

    def get_daily_range_time_month_day(self, year_month_day):

        start_time = time.strptime(year_month_day, "%Y-%m-%d")
        end_time = time.localtime(int(time.mktime(start_time)))
        end_time = time.strftime("  %b %d", end_time)
        start_time = time.strftime(" %b %d", start_time)
        return start_time, end_time

    def get_daily_rangetime(self, year_month_day):

        start_time = time.strptime(year_month_day, "%Y-%m-%d")
        end_time = time.localtime(int(time.mktime(start_time)))
        end_time = time.strftime("%Y-%m-%d", end_time)
        start_time = time.strftime("%Y-%m-%d", start_time)
        print start_time, end_time
        return start_time, end_time

    def get_last_daily_rangetime(self, last_day):

        end_time = time.strptime(last_day, "%Y-%m-%d")
        start_time = time.localtime(int(time.mktime(end_time) - 86400))
        start_time = time.strftime("%Y-%m-%d", start_time)
        end_time = time.strftime("%Y-%m-%d", end_time)
        print start_time, end_time
        return start_time, end_time

    def get_weekly_range_time_week_month_day_year(self):

        start_time = datetime.datetime.strptime(self.pdf_time, "%Y-%m-%d")
        dayscount = datetime.timedelta(days=start_time.isoweekday())
        dayto = start_time - dayscount
        sixdays = datetime.timedelta(days=6)
        dayfrom = dayto - sixdays
        time_start = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day)
        time_end = datetime.datetime(dayto.year, dayto.month, dayto.day)
        time_start = time.strptime(str(time_start), "%Y-%m-%d %H:%M:%S")
        time_start = time.strftime("%a,%b %d,%Y", time_start)
        time_end = time.strptime(str(time_end), "%Y-%m-%d %H:%M:%S")
        time_end = time.strftime("%a,%b %d,%Y", time_end)
        print time_start, time_end
        return time_start, time_end

    def get_weekly_range_time_month_day_year(self):

        start_time = datetime.datetime.strptime(self.pdf_time, "%Y-%m-%d")
        dayscount = datetime.timedelta(days=start_time.isoweekday())
        dayto = start_time - dayscount
        sixdays = datetime.timedelta(days=6)
        dayfrom = dayto - sixdays
        time_start = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day)
        time_end = datetime.datetime(dayto.year, dayto.month, dayto.day)
        time_start = time.strptime(str(time_start), "%Y-%m-%d %H:%M:%S")
        time_start = time.strftime("%b %d,%Y", time_start)
        time_end = time.strptime(str(time_end), "%Y-%m-%d %H:%M:%S")
        time_end = time.strftime("%b %d,%Y", time_end)
        print time_start, time_end
        return time_start, time_end

    def get_weekly_range_time_month_day(self):

        start_time = datetime.datetime.strptime(self.pdf_time, "%Y-%m-%d")
        dayscount = datetime.timedelta(days=start_time.isoweekday())
        dayto = start_time - dayscount
        sixdays = datetime.timedelta(days=6)
        dayfrom = dayto - sixdays
        time_start = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day)
        time_end = datetime.datetime(dayto.year, dayto.month, dayto.day)
        time_start = time.strptime(str(time_start), "%Y-%m-%d %H:%M:%S")
        time_start = time.strftime("%b %d", time_start)
        time_end = time.strptime(str(time_end), "%Y-%m-%d %H:%M:%S")
        time_end = time.strftime("%b %d", time_end)
        print time_start, time_end
        return time_start, time_end

    def get_week_rangetime(self):

        start_time = datetime.datetime.strptime(self.pdf_time, "%Y-%m-%d")
        dayscount = datetime.timedelta(days=start_time.isoweekday())
        dayto = start_time - dayscount
        sixdays = datetime.timedelta(days=6)
        dayfrom = dayto - sixdays
        time_start = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day)
        time_end = datetime.datetime(dayto.year, dayto.month, dayto.day)
        time_start = time.strptime(str(time_start), "%Y-%m-%d %H:%M:%S")
        time_start = time.strftime("%Y-%m-%d", time_start)
        time_end = time.strptime(str(time_end), "%Y-%m-%d %H:%M:%S")
        time_end = time.strftime("%Y-%m-%d", time_end)
        print time_start, time_end
        return time_start, time_end

    def get_month_range_time_month_day(self):

        end_time = time.strptime(self.pdf_time, "%Y-%m-%d")
        time_end = time.strftime("%Y %m 01", end_time)
        time_end = time.strptime(time_end, "%Y %m %d")
        time_end = time.strftime(" %b %d", time_end)
        first_day = datetime.date(int(time.strftime("%Y", end_time)), int(time.strftime("%m", end_time)), 1)
        days_num = calendar.monthrange(first_day.year, first_day.month - 1)[1]
        last_month = first_day - datetime.timedelta(days=days_num)
        time_start = str(datetime.date(last_month.year, last_month.month, 1))
        time_start = time.strptime(time_start, "%Y-%m-%d")
        time_start = time.strftime(" %b 01", time_start)
        print time_start, time_end
        return time_start, time_end

    def get_month_range_time_month_year(self):

        end_time = time.strptime(self.pdf_time, "%Y-%m-%d")
        time_end = time.strftime("%Y %m 01", end_time)
        time_end = time.strptime(time_end, "%Y %m %d")
        time_end = time.strftime(" %b-%Y", time_end)
        first_day = datetime.date(int(time.strftime("%Y", end_time)), int(time.strftime("%m", end_time)), 1)
        days_num = calendar.monthrange(first_day.year, first_day.month - 1)[1]
        last_month = first_day - datetime.timedelta(days=days_num)
        time_start = str(datetime.date(last_month.year, last_month.month, 1))
        time_start = time.strptime(time_start, "%Y-%m-%d")
        time_start = time.strftime(" %b-%Y", time_start)
        print time_start, time_end
        return time_start, time_end

    def get_month_range_time_month_day_year(self):

        end_time = time.strptime(self.pdf_time, "%Y-%m-%d")
        time_end = time.strftime("%Y %m 01", end_time)
        time_end = time.strptime(time_end, "%Y %m %d")
        time_end = time.strftime(" %b %d, %Y ", time_end)
        first_day = datetime.date(int(time.strftime("%Y", end_time)), int(time.strftime("%m", end_time)), 1)
        days_num = calendar.monthrange(first_day.year, first_day.month - 1)[1]
        last_month = first_day - datetime.timedelta(days=days_num)
        time_start = str(datetime.date(last_month.year, last_month.month, 1))
        time_start = time.strptime(time_start, "%Y-%m-%d")
        time_start = time.strftime(" %b 01, %Y ", time_start)
        print time_start, time_end
        return time_start, time_end

    def get_month_range_time_week_month_day_year(self):

        end_time = time.strptime(self.pdf_time, "%Y-%m-%d")
        time_end = time.strftime("%Y %m 01", end_time)
        time_end = time.strptime(time_end, "%Y %m %d")
        time_end = time.strftime("%a, %b %d, %Y", time_end)
        first_day = datetime.date(int(time.strftime("%Y", end_time)), int(time.strftime("%m", end_time)), 1)
        days_num = calendar.monthrange(first_day.year, first_day.month - 1)[1]
        last_month = first_day - datetime.timedelta(days=days_num)
        time_start = str(datetime.date(last_month.year, last_month.month, 1))
        time_start = time.strptime(time_start, "%Y-%m-%d")
        time_start = time.strftime("%a, %b 01, %Y ", time_start)
        print time_start, time_end
        return time_start, time_end

    def get_month_rangetime(self):

        end_time = time.strptime(self.pdf_time, "%Y-%m-%d")
        time_end = time.strftime("%Y-%m-01", end_time)
        time_end = time.strptime(time_end, "%Y-%m-%d")
        time_end = time.strftime("%Y-%m-%d", time_end)
        first_day = datetime.date(int(time.strftime("%Y", end_time)), int(time.strftime("%m", end_time)), 1)
        days_num = calendar.monthrange(first_day.year, first_day.month - 1)[1]
        last_month = first_day - datetime.timedelta(days=days_num)
        time_start = str(datetime.date(last_month.year, last_month.month, 1))
        time_start = time.strptime(time_start, "%Y-%m-%d")
        time_start = time.strftime("%Y-%m-01", time_start)
        print time_start, time_end
        return time_start, time_end

    def get_specific_day(self, year_month_day, days):

        try:
            specific_day = datetime.datetime.strptime(year_month_day, "%Y-%m-%d")
            specific_day = (specific_day + datetime.timedelta(days=days)).strftime("%Y-%m-%d")
        except Exception as e:
            print e
            specific_day = None
        return specific_day

    def get_specific_hour(self, hour, hours):

        if not hour:
            next_hour = None
        try:
            next_hour = datetime.datetime.strptime(hour, "%I %p")
            next_hour = (next_hour + datetime.timedelta(hours=hours)).strftime("%I %p")
        except Exception as e:
            print e
            next_hour = None
        return next_hour

    def get_daily_range_time_day_month(self, day):
        if not day:
            next_hour = None
        try:
            next_hour = datetime.datetime.strptime(day, "%Y-%m-%d")
            next_hour = next_hour.strftime("%b %d")

        except Exception as e:
            print e
            next_hour = None
        return next_hour


if __name__ == "__main__":
    i = PdfDate('2018-10-16')
    print i.get_daily_range_time_week_month_day_year('2018-11-22')
