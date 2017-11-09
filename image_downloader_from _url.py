# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:06:20 2017

@author: spidy
"""

import time
import csv
from urllib import request

request.urlretrieve("http://www.merinolaminates.com/prodImg/Product/22293%20SF.jpg", "hello.jpeg")

ifile = open("undownloaded_image.csv", "w")
writer = csv.writer(ifile)

with open("merino.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    i = 0    
    for row in csvreader:
        print(row[1])
        i += 1
        if (i%180==0):
            print(i)
            time.sleep(120)
        try:
            row[0] = row[0].replace("/Merino_Boards/", "")            
            request.urlretrieve(row[1], row[0])
        except ValueError as e:
            print(e)
            writer.writerow([row[0], row[1]])

ifile.flush()
ifile.close()