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

from Crypto.Cipher import AES
import base64
from binascii import b2a_hex, a2b_hex

key = 'oPysK(2sp)yske#&'


def encrypt_str(source):
    PADDING = '\0'
    # PADDING = ' '
    pad_it = lambda s: s + (16 - len(s) % 16) * PADDING
    iv = key
    generator = AES.new(key, AES.MODE_CBC, iv)
    crypt = generator.encrypt(pad_it(source))
    cryptedStr = base64.b64encode(crypt)
    return b2a_hex(cryptedStr)


def decrypt_str(source):
    PADDING = '\0'
    iv = key
    generator = AES.new(key, AES.MODE_CBC, iv)
    recovery = generator.decrypt(base64.b64decode(a2b_hex(source)))
    return recovery.rstrip(PADDING)


if __name__ == '__main__':
    print encrypt_str('cadillac_KbDL822p366y')
