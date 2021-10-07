import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv

URL = "https://en.wikipedia.org/wiki/Comma-separated_values"
information = requests.get(URL)
root = BeautifulSoup(information.content,"html.parser")

table = root.find("table",{"class":"wikitable"})
Data = table.find_all("tr")

Headings = Data[0].find_all("th")
Headings = [tag.text for tag in Headings]

contents = []
for row in Data[1:]:
    cols = row.find_all("td")
    cols = [tag.text for tag in cols]
    contents.append([tag for tag in cols])

Answer = pd.DataFrame(contents,columns = Headings)
Answer

with open("python.csv","w",encoding = "UTF8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(Headings)
    for tag in contents:
        writer.writerow(tag)
