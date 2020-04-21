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
from mysql import connector
import json
import os
import aes

logger = logging.getLogger(__name__)
current_dir = os.path.dirname(__file__)
# db_config_json = os.path.join(current_dir, "db_connection.json")
db_config_path = "../db_connection.json"
with open(db_config_path, mode='r') as f:
    db_dict = json.loads(f.read())

config = {
    'host': db_dict.get("db_host"),
    'user': db_dict.get("db_user"),
    'password': db_dict.get("db_password"),
    'port': db_dict.get("db_port"),
    'database': db_dict.get("db_name"),
    'charset': 'utf8'
}


class Mysql(object):

    def __init__(self):
        self.conn_object = None
        self.cur_object = None

    def db_connect(self):
        try:
            self.conn_object = connector.connect(**config)
        except Exception as e:
            print e
            logger.error(e)
            return False

        if self.conn_object == None:
            return False
        else:
            try:
                self.cur_object = self.conn_object.cursor()
            except Exception as e:
                self.conn_object.close()
                print e
                logger.error(e)
                return False
            if self.cur_object != None:
                return True

    def db_close(self):
        if self.conn_object != None and self.cur_object != None:
            self.conn_object.close()
            self.cur_object.close()
            return True
        else:
            return False

    def db_query(self, sql_query):
        if sql_query == None:
            return None
        else:
            try:
                self.cur_object.execute(sql_query)
                return self.cur_object.fetchall()
            except Exception as e:
                print e
                logger.error(e)
                return None

    def db_change(self, sql_change):
        if sql_change == None:
            return False
        else:
            try:
                self.cur_object.execute(sql_change)
                self.conn_object.commit()
                return True
            except Exception as e:
                self.conn_object.rollback()
                return False
