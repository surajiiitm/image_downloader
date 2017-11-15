# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:06:20 2017

@author: spidy
"""

# importing library
import time
import csv
from urllib import request

# file writing list of failed images url
ifile = open("undownloaded_image.csv", "w")
writer = csv.writer(ifile)


# input file name containing url's
filename = "merino.csv"
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
    i = 0    
    for row in csvreader:
        print(row[0])
        i += 1
        
        # sleep after 180 call to website such that it doesn't blocks request
        if (i%180==0):
            print(i)
            time.sleep(60)
        try:            
            request.urlretrieve(row[1], row[0])
        except ValueError as e:
            print(e)
            writer.writerow([row[0], row[1]])

# reflecting the write file and closing it
ifile.flush()
ifile.close()
