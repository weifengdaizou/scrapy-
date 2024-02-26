import re
import requests
import time
from bs4 import BeautifulSoup
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}


def get_url(url):
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    html = res.text
    # print(res.status_code)

    url_list = re.findall('<a class="" href="(.*?)" target="_blank"', res.text)
    #     print(url_list)
    for url in url_list:
        print(url)
        get_info(url)



def get_info(url):
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    selector = etree.HTML(html)

    # title =re.findall( '<h1>(.*?)</h1>',res.text,re.S)
    title = soup.select('div.content > div > h1')[0].string
    name = soup.select('div.communityName a')[0].string
    # add = soup.select('span.info a')[0].text
    add = selector.xpath('//div[@class="areaName"]')[0].xpath('string(.)')  # 地址
    room = soup.select('div.room div.mainInfo')[0].string  # 户型
    floor = soup.select('div.subInfo')[0].string
    area = soup.select('div.area div.mainInfo')[0].string
    total = soup.select('div.price span')[0].string  # 总价
    # unitprice = soup.select('div.unitPrice span')[0].string  #单价
    unitprice = selector.xpath('//div[@class="unitPrice"]')[0].xpath('string(.)')  # 单价
    agent = soup.select('div.ke-agent-sj-info a')[0].string.strip()  # 经纪人
    tel = selector.xpath('//div[@class="ke-agent-sj-phone "]')[0].xpath('string(.)').replace(' ', '')  # 电话

    print(title)
    print(name)

url = 'https://sz.lianjia.com/ershoufang/pg2'
get_url(url)