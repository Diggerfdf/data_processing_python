# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 20:42:25 2018

@author: digger
"""

import os
import glob
import pandas

def addField(indir="/home/digger/Classes/Python/Data_Processing/S05_Starting_Pandas/Data/Exercise/"):
    os.chdir(indir)
    fileList = glob.glob("*")
    for filename in fileList:
        df = pandas.read_csv(filename, sep = "\s+", header = None)
        df["Station"] = [filename.rsplit('-', 1)[0]]*df.shape[0]
        df.to_csv(filename + ".csv", index = None, header = None)
