import copy
import re

import scrapy
from ..items import ScrapyfItem


class SzywSpider(scrapy.Spider):
    name = "szyw"
    allowed_domains = ["szpt.edu.cn"]
    start_urls = ["https://www.szpt.edu.cn/old/szxw/szyw.htm"]

    def parse(self, response):
        items = ScrapyfItem()
        lis = response.css('.list li ')
        for li in lis:
            title = li.css('a::text')[0].extract()
            date = li.css('span::text')[0].extract()
            link = li.css('a::attr(href)')[0].extract()
            link = link[3:]
            # print(type(link))
            items['title'] = title
            items['date'] = date
            items['link'] = link
            yield scrapy.Request(
                url= 'https://www.szpt.edu.cn/old/' + link,
                callback= self.datail,
                meta={'items_data': copy.deepcopy(items)}
            )

        # next_url = response.css('.p_next.p_fun > a::attr(href)')[0].extract()
        # if next_url[0] != 's':
        #     next_url = "https://www.szpt.edu.cn/old/szxw/szyw/" + next_url
        # else:
        #     next_url = "https://www.szpt.edu.cn/old/szxw/" + next_url

        # yield scrapy.Request(
        #     url=next_url,
        #     callback=self.parse
        # )


    def datail(self, response):
        ps = response.css('.v_news_content p::text')
        contents = [i.extract() for i in ps]
        content = ''.join(contents)
        items = response.meta['items_data']
        items['content'] = content
        print(items)


