#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:40:08 2021

@author: eaindraykhin
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup

link = 'https://en.wikipedia.org/wiki/Comma-separated_values'
cars = requests.get(link)
soup = BeautifulSoup(cars.text, 'lxml')
print(soup)

cars_table = soup.find("table", attrs={"class": "wikitable"})

headers = []

for i in cars_table.find_all("th"):
    title = i.text.strip()
    headers.append(title)
    
df = pd.DataFrame(columns = headers)

for row in cars_table.find_all("tr")[1:]:
    data = row.find_all("td")
    row_data = [td.text.strip() for td in data]
    length = len(df)
    df.loc[length] = row_data

print(df)
df.to_csv('Cars.csv', header=False, index=False)
pd.read_csv('Cars.csv')

