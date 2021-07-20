import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# res = requests.get(
#     'http://www.rajasthanindustries.org/ViewCompanyProfile.aspx?id=All&typet=alpha')

# soup = BeautifulSoup(res.content, 'lxml')

rt1 = open('main.html','r')

soup = BeautifulSoup(rt1, 'lxml')
tables = soup.find_all("table", {"style":"width: 100%; vertical-align: top;"})

# for i in tables:
    # df = pd.read_html(i)
    # print(df)

df = pd.read_html(tables[0])
df.to_csv('ot.csv', index=False)

# df = pd.read_html('main.html')

# print(df.head(5))
# df.to_csv('ot.csv')#, in
