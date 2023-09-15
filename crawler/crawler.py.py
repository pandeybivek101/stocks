# Databricks notebook source
import requests
from bs4 import BeautifulSoup

def f_crawl_item(url:str)->list:

    """
    function takes url input and returns
    lists of crawled items
    """
    page = requests.get(url)
    html = BeautifulSoup(page.text, "html.parser")
    quotes = html.find('table')
    items=[]
    for index, tr in enumerate(html.findAll('table')[0].findAll('tr')):
        if index != 0:
            broker_id_tag = tr.td.a
            broker_name_tag = broker_id_tag.find_parent().findNextSibling()
            broker_phone_tag = broker_name_tag.findNextSibling()
            broker_address_tag=broker_phone.findNextSibling()
            broker_tuple=(broker_id_tag.text, broker_name_tag.text, broker_phone_tag.text, broker_address_tag.text)
            items.append(broker_tuple)
    return items



url="https://merolagani.com/BrokerList.aspx"
print(f_crawl_item(url))

# COMMAND ----------


a=('name', )

# COMMAND ----------


