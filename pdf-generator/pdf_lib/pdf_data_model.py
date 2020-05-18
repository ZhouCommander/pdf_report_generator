# !/usr/bin/ python
# coding=utf-8
"""
*Author: team of develop platform(vmaxx)
*Date:2018-10
*The source code made by our team is opened
*Take care of it please and welcome to update it 
"""
import numpy as np


class BaseEntity(object):

    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.time_type = None


class Entry(BaseEntity):

    def __init__(self):

        super(Entry, self).__init__()
        self.exit = []
        self.enter = []
        self.occupancy = []
        self.hour = []
        self.day = []
        self.dwell = 0
        self.max_occupancy = []
        self.min_occupancy = []
        self.avg_occupancy = []
        self.id = 0

    def get_peak_occupancy(self):

        if self.max_occupancy:
            return max(self.max_occupancy)
        else:
            return -1

    def get_peak_enter(self):

        if self.enter:
            return max(self.enter)
        else:
            return -1

    def get_peak_exit(self):

        if self.exit:
            return max(self.exit)
        else:
            return -1

    def get_peak_enter_hour(self, peak_enter):

        if peak_enter:
            return self.hour[self.enter.index(peak_enter)]
        else:
            return None

    def get_peak_occupancy_hour(self, peak_occupancy):

        if peak_occupancy:
            return self.hour[self.max_occupancy.index(peak_occupancy)]
        else:
            return None

    def get_peak_exit_hour(self, peak_exit):

        if peak_exit:
            return self.hour[self.exit.index(peak_exit)]
        else:
            return None

    def get_avg_enteries(self):

        if self.enter:
            return np.mean(self.enter)
        else:
            return 0

    def get_avg_occupancy(self):

        if self.occupancy:
            return np.mean(self.occupancy)
        else:
            return -1

    def get_avg_exit(self):

        if self.exit:
            return np.mean(self.exit)
        else:
            return -1

    def get_total_enteries(self):

        if self.enter:
            return sum(self.enter)
        else:
            return 0

    def get_total_oppupancy(self):

        if self.occupancy:
            return max(self.occupancy)
        else:
            return 0

    def get_total_exit(self):

        if self.exit:
            return sum(self.exit)
        else:
            return 0


class PropertyEntry(Entry):

    def __init__(self):
        super(PropertyEntry, self).__init__()
        pass


class Gender(BaseEntity):

    def __init__(self):

        super(Gender, self).__init__()
        self.male_gender = 0
        self.female_gender = 0

    def get_male_percent(self):

        if self.male_gender and self.female_gender:
            return self.male_gender / (self.female_gender + self.male_gender)
        else:
            return 0
        pass

    def get_female_percent(self):

        if self.male_gender and self.female_gender:
            return self.female_gender / (self.female_gender + self.male_gender)
        else:
            return 0


class Age(BaseEntity):

    def __init__(self):
        super(Age, self).__init__()
        self.sum_age = 0
        self.male_less_thirty = 0
        self.male_thirty_to_fourtyfive = 0
        self.male_fourtyfive_to_sixty = 0
        self.male_more_sixty = 0
        self.female_less_thirty = 0
        self.female_less_thirty = 0
        self.female_thirty_to_fourtyfive = 0
        self.female_fourtyfive_to_sixty = 0
        self.female_more_sixty = 0


class Zone(object):

    def __init__(self):
        self.zone_name = None


class Entrance(object):

    def __init__(self):
        self.entrance_name = None


class Dwell(Zone, BaseEntity):

    def __init__(self):

        super(Dwell, self).__init__()
        self.dwell_time = []
        self.hour = []
        self.day = []
        self.avg_dwell_time = None

    def second_to_minute(self, second):
        if not second:
            return '0:00'
        if second / 60 >= 60:
            print 'error:checkout and linewait time more than 1h!!'
        min = int(second) // 60
        sec = int(second) % 60
        minute = str(min) + ':' + str(sec).zfill(2)
        return minute

    def get_avg_dwell_time(self):

        if self.dwell_time:
            return np.mean(self.dwell_time)
        else:
            return -1

    def get_peak_dwell_time(self):

        if self.dwell_time:
            return max(self.dwell_time)
        else:
            return -1

    def get_peak_dwell_hour(self, peak_dwell_time):

        if self.dwell_time:
            return self.hour[self.dwell_time.index(peak_dwell_time)]
        else:
            return None


class ZoneData(Entry, Dwell):

    def __init__(self):
        super(ZoneData, self).__init__()
        pass


class EntranceData(Entry, Entrance):

    def __init__(self):
        super(EntranceData, self).__init__()
        pass


class HeatMap(object):

    def __init__(self):
        self.url = None


class Weather(object):

    def __init__(self):
        self.hour = []
        self.day = []
        self.weather_text = []
        self.weather_temperature = []
