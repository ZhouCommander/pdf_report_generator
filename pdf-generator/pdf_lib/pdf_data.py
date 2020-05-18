#!/usr/bin/ python
# coding=utf-8
"""
*Author: team of develop platform(vmaxx)
*Date:2018-10
*The source code made by our team is opened
*Take care of it please and welcome to update it 
"""
from Mysql import Mysql
from pdf_data_model import *
import time
import datetime
import logging

logger = logging.getLogger(__name__)


class PdfData(Mysql):

    def __init__(self):

        super(PdfData, self).__init__()
        self.db_connect()

    def init_hour_list(self, time_start, time_end):

        hour_list = []
        start_hour = time.strftime("%I %p", time.strptime(str(time_start), "%Y-%m-%d %H:%M:%S"))
        time_start = datetime.datetime.strptime(time_start, "%Y-%m-%d %H:%M:%S")
        time_end = datetime.datetime.strptime(time_end, "%Y-%m-%d %H:%M:%S")
        time_range = int((time_end - time_start).total_seconds() / 3600) + 1
        for i in range(0, time_range):
            start_hour = datetime.datetime.strptime(start_hour, "%I %p")
            next_hour = (start_hour + datetime.timedelta(hours=1)).strftime("%I %p")
            start_hour = start_hour.strftime("%I %p")
            hour_list.append(start_hour)
            start_hour = next_hour
        return hour_list

    def init_day_list(self, time_start, time_end):
        day_list = []
        start_day = time.strftime("%Y-%m-%d", time.strptime(str(time_start), "%Y-%m-%d %H:%M:%S"))
        start_end = time.strftime("%Y-%m-%d", time.strptime(str(time_end), "%Y-%m-%d %H:%M:%S"))
        time_start = datetime.datetime.strptime(start_day, "%Y-%m-%d")
        time_end = datetime.datetime.strptime(start_end, "%Y-%m-%d")
        for i in range(0, ((time_end - time_start).days)):
            start_day = datetime.datetime.strptime(start_day, "%Y-%m-%d")
            next_hour = (start_day + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            start_day = start_day.strftime("%Y-%m-%d")
            day_list.append(start_day)
            start_day = next_hour
        return day_list

    def get_property_entry(self, type_id, model_id, time_start, time_end):

        args = (type_id, model_id, time_start, time_end)
        try:
            self.cur_object.callproc("report_entry_data", args)
            for result in self.cur_object.stored_results():
                self.entry_list = result.fetchall()
                break
        except Exception as e:
            raise e
            logger.error(e)
            return None
        property_entry_object = PropertyEntry()
        property_entry_object.hour = self.init_hour_list(time_start, time_end)
        property_entry_object.enter = [0] * len(property_entry_object.hour)
        property_entry_object.exit = [0] * len(property_entry_object.hour)
        property_entry_object.occupancy = [0] * len(property_entry_object.hour)
        for item in self.entry_list:
            try:
                hour = time.strftime("%I %p", time.strptime(str(item[0]), "%H"))
                index = property_entry_object.hour.index(hour)
                property_entry_object.enter[index] = int(item[1])
                property_entry_object.exit[index] = int(item[2])
                if item[3] and int(str(item[3])) > 0:
                    property_entry_object.occupancy[index] = int(item[3])
                else:
                    property_entry_object.occupancy[index] = 0
            except Exception as e:
                print e
                logger.error(e)
        return property_entry_object

    def numTotime(self, num):
        if num / 60 >= 60:
            print 'error:checkout and linewait time more than 1h!!'
        min = num / 60
        sec = num % 60
        string = str(min) + ':' + str(sec).zfill(2)
        return string

    def get_dwell_time(self, model_id, time_start, time_end):

        dwell_time_data_object_list = []
        for zone_id in model_id:
            args = (zone_id, time_start, time_end)
            try:
                self.cur_object.callproc("report_zone_dwell", args)
                for result in self.cur_object.stored_results():
                    self.dwell_time_data_list = result.fetchall()
                    if not self.dwell_time_data_list:
                        break
                dwell_time_data_object = Dwell()
                dwell_time_data_object.zone_name = None
                dwell_time_data_object.hour = self.init_hour_list(time_start, time_end)
                dwell_time_data_object.dwell_time = [0] * len(dwell_time_data_object.hour)

                for item in self.dwell_time_data_list:
                    try:
                        dwell_time_data_object.zone_name = item[0]
                        if not item[1]:
                            continue
                        hour = time.strftime("%I %p", time.strptime(str(item[1]), "%H"))
                        index = dwell_time_data_object.hour.index(hour)
                        dwell_time_data_object.dwell_time[index] = int(item[2])
                    except Exception as e:
                        print e
                        logger.error(e)
                dwell_time_data_object_list.append(dwell_time_data_object)
            except Exception as e:
                raise e
                logger.error(e)
                return None
        return dwell_time_data_object_list

    def get_agender_age(self, time_start, time_end):

        args = (time_start, time_end)
        try:
            self.cur_object.callproc("report_age", args)
            for result in self.cur_object.stored_results():
                self.agendr_age_result = result.fetchone()
                break
        except Exception as e:
            print e
            raise
            logger.error(e)
            return None
        gender_object = Gender()
        age_object = Age()
        try:
            gender_object.male_gender = self.agendr_age_result[0]
            gender_object.female_gender = self.agendr_age_result[5]
            if not gender_object.male_gender:
                gender_object.male_gender = 0
            if not gender_object.female_gender:
                gender_object.female_gender = 0
            age_object.male_less_thirty = self.agendr_age_result[1]
            age_object.male_thirty_to_fourtyfive = self.agendr_age_result[2]
            age_object.male_fourtyfive_to_sixty = self.agendr_age_result[3]
            age_object.male_more_sixty = self.agendr_age_result[4]
            age_object.female_less_thirty = self.agendr_age_result[6]
            age_object.female_fourtyfive_to_sixty = self.agendr_age_result[7]
            age_object.female_thirty_to_fourtyfive = self.agendr_age_result[8]
            age_object.female_more_sixty = self.agendr_age_result[9]
        except Exception as e:
            print e
            logger.error(e)
            gender_object.male_gender_percent = 0
            gender_object.female_gender = 0
            age_object.male_less_thirty = 0
            age_object.male_thirty_to_fourtyfive = 0
            age_object.male_fourtyfive_to_sixty = 0
            age_object.male_more_sixty = 0
            age_object.female_less_thirty = 0
            age_object.female_fourtyfive_to_sixty = 0
            age_object.female_thirty_to_fourtyfive = 0
            age_object.female_more_sixty = 0
        return gender_object, age_object

    def get_zone_data(self, type_id, model_id, time_start, time_end):

        zone_data_object_list = []
        for zone_id in model_id:
            args = (type_id, zone_id, time_start, time_end)
            try:
                self.cur_object.callproc("report_zone_data", args)
                for result in self.cur_object.stored_results():
                    self.zone_data_list = result.fetchall()
                    if not self.zone_data_list:
                        break
                zone_data_object = ZoneData()
                zone_data_object.zone_name = None
                zone_data_object.hour = self.init_hour_list(time_start, time_end)
                zone_data_object.enter = [0] * len(zone_data_object.hour)
                zone_data_object.exit = [0] * len(zone_data_object.hour)
                zone_data_object.occupancy = [0] * len(zone_data_object.hour)
                for item in self.zone_data_list:
                    try:
                        zone_data_object.zone_name = item[0]
                        if not item[1]:
                            continue
                        hour = time.strftime("%I %p", time.strptime(str(item[1]), "%H"))
                        index = zone_data_object.hour.index(hour)
                        zone_data_object.enter[index] = int(item[2])
                        zone_data_object.exit[index] = int(item[3])
                        if item[4] and int(str(item[4])) > 0:
                            zone_data_object.occupancy[index] = int(item[4])
                        else:
                            zone_data_object.occupancy[index] = 0
                    except Exception as e:
                        print e
                        logger.error(e)
                zone_data_object_list.append(zone_data_object)
            except Exception as e:
                raise e
                logger.error(e)
                return None

        return zone_data_object_list

    def get_weather_per_hour(self, property_id, time_start, time_end):

        args = (property_id, time_start, time_end)
        weather_list = []
        try:
            self.cur_object.callproc("report_weather_hour", args)
            for result in self.cur_object.stored_results():
                weather_list = result.fetchall()
                break
        except Exception as e:
            print e
            return None
        weather_object = Weather()
        weather_object.hour = self.init_hour_list(time_start, time_end)
        weather_object.weather_text = [''] * len(weather_object.hour)
        weather_object.weather_temperature = [0] * len(weather_object.hour)
        for item in weather_list:
            try:
                hour = time.strftime("%I %p", time.strptime(str(item[0]), "%H"))
                index = weather_object.hour.index(hour)
                weather_object.weather_text[index] = item[1]
                weather_object.weather_temperature[index] = item[2]
            except Exception as e:
                print e
                logger.error(e)
        return weather_object

    def get_weather_per_day(self, property_id, time_start, time_end):

        weather_object = None
        weather_list = []
        args = (property_id, time_start, time_end)
        try:
            self.cur_object.callproc("report_weather_day", args)
            for result in self.cur_object.stored_results():
                weather_list = result.fetchall()
                break
        except Exception as e:
            print e
            return None
        weather_object = Weather()
        weather_object.day = self.init_day_list(time_start, time_end)
        weather_object.weather_text = [''] * len(weather_object.day)
        weather_object.weather_temperature = [0] * len(weather_object.day)
        for item in weather_list:
            try:
                day = str(item[0]).strip()
                index = weather_object.day.index(day)
                weather_object.weather_text[index] = item[1]
                weather_object.weather_temperature[index] = item[2]
            except Exception as e:
                print e
                logger.error(e)
        return weather_object

    def get_zone_entrances_name(self, type_id, model_id, type):

        entrance_name_list = []
        args_zone_entrance = (type_id, model_id, type)
        try:
            self.cur_object.callproc("report_zone_entrance", args_zone_entrance)
            for result in self.cur_object.stored_results():
                self.zone_entrance_list = result.fetchall()
                break
        except Exception as e:
            print e
            return None
        for entrance in self.zone_entrance_list:
            try:
                entrance_name = entrance[0]
            except Exception as e:
                print e
                entrance_name = None
            entrance_name_list.append(entrance_name)
        return entrance_name_list

    def get_zone_entrances_data(self, type_id, model_id, type, time_start, time_end):

        entrance_data_object_list = []
        vehicle_entrance_list = self.get_zone_entrances_name(type_id, model_id, type)
        for entrance_name in vehicle_entrance_list:
            entrance_data_object = EntranceData()
            entrance_data_object.entrance_name = entrance_name
            entrance_data_object.hour = self.init_hour_list(time_start, time_end)
            entrance_data_object.enter = [0] * len(entrance_data_object.hour)
            entrance_data_object.exit = [0] * len(entrance_data_object.hour)
            entrance_data_object.occupancy = [0] * len(entrance_data_object.hour)
            args_entrance_data = (type_id, model_id, type, entrance_data_object.entrance_name, time_start, time_end)
            self.cur_object.callproc("report_entrance_data", args_entrance_data)
            for result in self.cur_object.stored_results():
                self.vehicle_entrance_data_list = result.fetchall()
                if not self.vehicle_entrance_data_list:
                    break
            for item in self.vehicle_entrance_data_list:
                try:
                    if not item[1]:
                        continue
                    hour = time.strftime("%I %p", time.strptime(str(item[0]), "%H"))
                    index = entrance_data_object.hour.index(hour)
                    entrance_data_object.enter[index] = int(item[1])
                    entrance_data_object.exit[index] = int(item[2])
                    if item[3] and int(str(item[3])) > 0:
                        entrance_data_object.occupancy[index] = int(item[3])
                    else:
                        entrance_data_object.occupancy[index] = 0
                except Exception as e:
                    print e
                    logger.error(e)
            entrance_data_object_list.append(entrance_data_object)
        return entrance_data_object_list

    def report_insert_database(self, company_id, property_id, report_url, date, type_id, report_type, space_type):

        args = (company_id, property_id, date, report_url, type_id, report_type, space_type)
        try:
            self.cur_object.callproc("report_insert", args)
            for result in self.cur_object.stored_results():
                self.flag = result.fetchone()
                return self.flag
        except Exception as e:
            print e
            logger.error(e)
            return None


if __name__ == '__main__':
    i = PdfData()
    print i.get_weather_per_day(121, '2018-11-12 06:00:00', '2018-11-13 05:59:59').weather_temperature
