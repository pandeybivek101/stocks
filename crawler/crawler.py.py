# Databricks notebook source

#stocks
url="https://merolagani.com/BrokerList.aspx"

# COMMAND ----------

import requests
from bs4 import BeautifulSoup

# COMMAND ----------

page = requests.get(url)

# COMMAND ----------

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find('div', id="ctl00_ContentPlaceHolder1_divData")
items=[]

for row in results.findAll('table'):
    # item={}
    # item['id']=row.td.text
    # items.append(item)

print(item)


# COMMAND ----------



# COMMAND ----------

