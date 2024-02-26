import pymysql

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyfPipeline:
    def process_item(self, item, spider):
        print(item)
        return item

    def sss(self, spider):
        print('aaa', spider)


class LanjiaPipeline:
    def open_spider(self, spider):
        print('开始爬虫')
        self.mysql = pymysql.connect(host='localhost', user='root', password='451123770', database='testdb', port=3306)
        self.cur = self.mysql.cursor()
        query = f"SHOW TABLES LIKE 'fj'"
        self.cur.execute(query)
        result = self.cur.fetchall()
        if result:
            self.cur.execute('drop table fj')
        create_table = """
            create table fj(
            title varchar(30),
            price int,
            unitPrice int,
            house varchar(20),
            lever varchar(20),
            area varchar(20),
            label varchar(20),
            areaName varchar(20),
            username varchar(20),
            phone varchar(20))
            """
        self.cur.execute(create_table)



    def close_spider(self, spider):
        self.cur.close()
        self.mysql.commit()
        self.mysql.close()
        print('结束爬虫')


    def process_item(self, item, spider):
        query = "insert into fj values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        lis = (item['title'], item['price'], item['unitPrice'], item['house'], item['lever'], item['area'], item['label'], item['areaName'], item['username'], item['phone'])
        self.cur.execute(query, lis)
        return item
