
"""
Created on Tue Dec 11 15:38:55 2018

@author: digger
"""

import os
from ftplib import FTP, error_perm

def ftpDownloader(stationId, startYear, endYear, url = 'ftp.pyclass.com', user = 'student@pyclass.com', passwd = 'student123'):
    ftp = FTP(url)
    ftp.login(user, passwd)
    if not os.path.exists('./in'):
        os.makedirs('./in')
    os.chdir('./in')
    
    for year in range(startYear, endYear + 1):
        fullpath = '/Data/%s/%s-%s.gz' % (year, stationId, year)
        filename = os.path.basename(fullpath)
        try:
            with open(filename, 'wb') as file:
                ftp.retrbinary('RETR %s' % fullpath, file.write)
                print('{} sucessfully downloaded'.format(filename))
        except error_perm:
            print("{} is not availabe".format(filename))
            os.remove(filename)    

# If the remote file does not exist, the empty file created "with" will be deletade here
    ftp.close()


# ids = ["010010-99999", "010014-99999", "010015-99999", "010020-99999"]

# for name in ids:
#    ftpDownloader(name, 2010, 2014)