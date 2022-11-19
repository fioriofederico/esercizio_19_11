#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 14:59:15 2022

@author: iannello
"""

import json

def leggi_file_JSON(fname):
    try:
        fin = open(fname)
        data_to_be_read = json.load(fin)
        fin.close()
        return data_to_be_read
    except OSError as message:
        raise Exception(f'*** OS error *** {message}')
    except json.decoder.JSONDecodeError as message:
        raise Exception(f'*** json error *** {message}')


def scrivi_file_JSON(data_to_be_written, fname):
    try:
        fout = open(fname, 'w')
        json.dump(data_to_be_written, fout, indent=3)
        fout.close()
    except OSError as message:
        raise Exception(f'*** OS error *** {message}')
    except json.decoder.JSONEncodeError as message:
        raise Exception(f'*** json error *** {message}')
