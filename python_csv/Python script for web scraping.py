# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 20:24:45 2021

@author: Erika
"""

#%%
#this is to activate panda/beautifulsoup to web scrape
#bs4 is a web crawler for html and xml to connect data
import pandas as pd
from bs4 import BeautifulSoup #

#%%
#read html files
wikitable = pd.read_html('https://en.wikipedia.org/wiki/Comma-separated_values') 
#we choose [1] as list shown in Variable Explorer has 2 different elements. 
#index 0 is another table
wikitable[1] 

#%%
#storing the table into another object to extract
wikitablefinal = wikitable[1]
wikitablefinal.to_csv('python_web_scraping.csv')

#%%
import csv 
with open('python_web_scraping.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)