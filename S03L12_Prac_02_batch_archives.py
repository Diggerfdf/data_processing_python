# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 18:43:54 2018

@author: digger
"""
import os
import glob
import patoolib

def extractFiles(indir = "/home/digger/Classes/Python/Data_Processing/in", out = "/home/digger/Classes/Python/Data_Processing/in"):
    os.chdir(indir)
    archives = glob.glob("*.gz")
    
    if not os.path.exists(out):
        os.makedirs(out)
    
    files = os.listdir('Extracted')
    
    for archive in archives:
        if archive[: -3] not in files:
            patoolib.extract_archive(archive, outdir = out)
        