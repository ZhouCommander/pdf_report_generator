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

from reportlab.pdfgen import canvas
from azure.storage.blob import BlockBlobService
from azure.storage.blob.models import ContentSettings
import os
import time
import logging
import aes


class Pdf(object):
    '''
        @function:
            1.pdf base class:
            2.if you want to use this class,and you need to inherit this class 
                example:
                class NewPdf(pdf):
                    def __init__(self,pdf_config_object):
                        pdf_config_object.pdf_time_type = time_type
                        pdf_config_object.pdf_report_type = report_type
                        super(NewPdf,self).__init__(pdf_config_object)
    '''

    def __init__(self, pdf_config_object):

        '''
            @function: init a pdf file object and set the pdf save path and the pdf name
            @args:
                pdf_config_object : it is a config  object 
        '''
        self.pdf_name = None
        self.pdf_page_object = None
        self.pdf_config_object = pdf_config_object
        self.pdf_name = self.pdf_config_object.pdf_time_type + "_" + self.pdf_config_object.pdf_name + "_" + self.pdf_config_object.pdf_report_type + "_" + self.pdf_config_object.pdf_time + ".pdf"
        self.pdf_name = self.pdf_name.replace(' ', '_')
        try:
            self.pdf_page_object = canvas.Canvas(self.pdf_config_object.pdf_path + "/" + self.pdf_name, pagesize=(
            self.pdf_config_object.pdf_width, self.pdf_config_object.pdf_height))
            self.pdf_page_object.setTitle(self.pdf_name)
        except Exception as e:
            raise e
            print e

    def pdf_save(self):

        '''
            @function: it will save the pdf file to  pdf_path
        '''
        try:
            if self.pdf_page_object:
                self.pdf_page_object.save()
                return True
            else:
                return False
        except Exception as e:
            raise e
            return False

    def pdf_add_page(self):

        '''
            @function :it will add a new pdf page on the pdf file . 
        '''
        if self.pdf_page_object:
            self.pdf_page_object.showPage()
            return True
        else:
            return False

    def pdf_clean(self):

        '''
            @function: delete the pdf file . 
        '''
        try:
            os.system("rm -f %s/*" % self.pdf_config_object.pdf_path)
            return True
        except Exception as e:
            print e
            raise e
            return False

    def pdf_upload(self, debug):

        '''
            @function: upload pdf file.
            @args:
                1. debug :  debug is "False"  the pdf file will be deleted.
                            debug is "True"  the pdf file will not be deleted.
        '''

        aes_pdfname = aes.encrypt_str(self.pdf_config_object.pdf_company) + "/" + aes.encrypt_str(
            self.pdf_config_object.pdf_property) + "/" + self.pdf_name
        self.pdf_url = self.pdf_config_object.pdf_url + aes_pdfname
        try:
            blob_service = BlockBlobService(self.pdf_config_object.account_name, self.pdf_config_object.account_key)
            blob_service.create_blob_from_path(self.pdf_config_object.pdf_upload_path_name, aes_pdfname,
                                               self.pdf_config_object.pdf_path + "/" + self.pdf_name,
                                               content_settings=ContentSettings(content_type='application/pdf'))
            if debug == "False":
                self.pdf_clean()
            return self.pdf_url
        except Exception as e:
            raise e
            return None


# if __name__ == '__main__':
#     run = Pdf()
