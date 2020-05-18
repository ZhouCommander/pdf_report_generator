#!/usr/bin/ python
# coding=utf-8
"""
*Author: team of develop platform(vmaxx)
*Date:2018-10
*The source code made by our team is opened
*Take care of it please and welcome to update it 
"""
import os
import json
import logging

cur_dir = os.path.dirname(__file__)
# config_path = os.path.join(cur_dir, "pdf_info.json")
config_path = "../pdf_info.json"


class PdfConfig(object):
    '''
     @function:
        1.pdf config file class:
        2.if you want to use this class,first you must transfer the  param_init() function
            example:
                config_object = PdfConfig.param_init(pdf_date)
    '''

    def __init__(self):

        self.pdf_path = None
        self.pdf_time = None
        self.pdf_name = None
        self.pdf_width = None
        self.pdf_height = None
        self.pdf_company = None
        self.pdf_property = None
        self.account_name = None
        self.account_key = None
        self.pdf_time_type = None
        self.pdf_report_type = None
        self.pdf_url = None
        self.pdf_enironment = None
        self.pdf_upload_path_name = None
        self.pdf_client_profile = None

    @classmethod
    def param_init(cls, pdf_date):

        '''
            @function: this function is a classmethod,and it will acquire the necessary 
            paramaters when generating a pdf file,then it will return a PdfConfig object
            @args:
                1.pdf_date: pdf start time

        '''

        json_pdf_config = None
        try:
            if os.path.exists(config_path):
                with open(config_path, "rb") as f:
                    pdf_config = f.read()
                    json_pdf_config = json.loads(pdf_config)
        except Exception as e:
            print e
            return None
        if not json_pdf_config:
            return
        config_object = PdfConfig()
        config_object.pdf_time = pdf_date
        config_object.pdf_path = json_pdf_config["temp_path"]
        config_object.pdf_name = json_pdf_config["pdf_name_prefix"]
        config_object.pdf_width = json_pdf_config["PageWidth"]
        config_object.pdf_height = json_pdf_config["PageHeight"]
        config_object.pdf_company = json_pdf_config["company_name"]
        config_object.pdf_property = json_pdf_config["property_name"]
        config_object.account_name = json_pdf_config["account_name"]
        config_object.account_key = json_pdf_config["account_key"]
        config_object.pdf_upload_path_name = json_pdf_config["upload_path_name"]
        config_object.pdf_url = json_pdf_config["pdf_url"]
        config_object.pdf_enironment = json_pdf_config["debug"]
        config_object.pdf_client_profile = json_pdf_config["client_profile"]
        config_object.pdf_company_profile = json_pdf_config["company_profile"]

        try:
            if not os.path.exists(config_object.pdf_path):
                os.mkdir(config_object.pdf_path)
        except Exception as e:
            print e
            return None
        return config_object
