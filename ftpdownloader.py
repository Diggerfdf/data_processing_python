# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:02:06 2018

@author: digger
"""
from ftplib import FTP
import os

def ftpDownloader(filename, host = 'ftp.pyclass.com', user = 'student@pyclass.com', passwd = 'student123'):
    ftp = FTP(host)
    ftp.login(user, passwd)
    ftp.cwd('Data')
    os.chdir('./CS')    
    with open(filename, 'wb') as file:
        ftp.retrbinary('RETR %s' % filename, file.write)
        