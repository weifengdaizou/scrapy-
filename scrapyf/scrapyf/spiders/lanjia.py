import re
import scrapy
from ..items import LanjiaModel

class LanjiaSpider(scrapy.Spider):
    name = "lanjia"
    allowed_domains = ["sz.lianjia.com"]
    start_urls = [f"https://sz.lianjia.com/ershoufang/pg{i}/" for i in range(1, 101)]

    def parse(self, response):
        lis = response.css('ul.sellListContent li')
        for li in lis:
            title = li.css('.title a::text').extract_first()
            if title:
                new_url = li.css('.title a::attr(href)').extract_first()
                yield scrapy.Request(
                    url=new_url,
                    callback=self.next_func,
                )

    def next_func(self, response):
        items = LanjiaModel()
        title = response.css('h1.main::attr(title)').extract_first()
        price1 = response.css('div.price > span.total::text').extract_first()
        if price1:
            # 获取单位
            price2 = response.css('div.price > span.unit span::text').extract_first()
            price = price1
        else:
            # price = ''
            price = 0
        unitPrice1 = response.css('div.unitPrice > span::text').extract_first()
        if unitPrice1:
            #  获取单位
            unitPrice2 = response.css('div.unitPrice > span > i::text').extract_first()
            unitPrice = unitPrice1
        else:
            # unitPrice = ''
            unitPrice = 0
        house = response.css('div.mainInfo::text').extract_first()
        lever = response.css('div.subInfo::text').extract_first()
        area = response.css('div.area > div.mainInfo::text').extract_first()
        label = response.css('div.communityName > a.info::text').extract_first()
        areaName = response.css('div.areaName > span.info a::text').extract()
        areaName1 = response.css('div.areaName > a::text').extract_first()

        if areaName1:
            areaName.append(areaName1)
        areaName = '-'.join(areaName)

        username = response.css('div.ke-agent-sj-info > a::text').extract_first()
        phone = response.css('div.ke-agent-sj-phone::text').extract()
        phone = ''.join(phone)
        phone = re.sub('\s', '', phone)

        items['title'] = title
        items['price'] = price
        items['unitPrice'] = unitPrice
        items['house'] = house
        items['lever'] = lever
        items['area'] = area
        items['label'] = label
        items['areaName'] = areaName
        items['username'] = username
        items['phone'] = phone
        yield items
# 30