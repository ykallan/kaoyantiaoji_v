# -*- coding: utf-8 -*-
import scrapy
import datetime
from kaoyantiaoji.items import KaoyantiaojiItem
from lxml import etree


class KySpider(scrapy.Spider):
    name = 'ky'
    # allowed_domains = ['ky.com']
    start_urls = ['http://ky.com/']
    base_url = 'https://common-mini.okaoyan.com/api/adjust/info/list?province_name=&university_name=&major_name=&learn_style=&page_num={}&page_size=20&year=2020'

    def start_requests(self):
        for i in range(10000):
        # for i in range(1):
            # yield scrapy.Request(url=self.base_url.format(i+1),callback=self.parse)
            yield scrapy.Request(url=self.base_url.format(i),callback=self.parse)

    def parse(self, response):
        false = False
        true = True
        req_url = 'https://common-mini.okaoyan.com/api/adjust/info/{}'
        # print(response.text)
        resp_dict = eval(response.text)
        # print(resp_dict['message'])
        # print(resp_dict['data'].keys())
        # print(resp_dict['data']['adjustInfoList'])
        for i in resp_dict['data']['adjustInfoList']:
            # print('i:::::',i)
            # print(type(i))
            # print(i.keys())
            # print(i['articleId'])
            meta={
                'provinceName': i['provinceName'],
                'universityName': i['universityName'],
                'majorName': i['majorName'],
                'publishDate': i['publishDate'],
                'learnStyle': i['learnStyle'],
                'articleId': i['articleId'],
                'title': i['title'],
                'isNew': i['isNew'],
            }
            yield scrapy.Request(url=req_url.format(i['articleId']), callback=self.parse_detial)

    def parse_detial(self,response):
        item = KaoyantiaojiItem()
        false = False
        true = True
        # meta = response.meta
        # print('meta:::',meta)

        resp_dict = eval(response.text)
        # print(resp_dict)
        # print(resp_dict.keys())
        # print(resp_dict['data'].keys())
        item['provinceName'] = resp_dict['data']['provinceName']
        item['universityName'] = resp_dict['data']['universityName']
        item['majorName'] = resp_dict['data']['majorName']
        item['publishDate'] = datetime.datetime.fromtimestamp(resp_dict['data']['publishDate']).strftime("%Y-%m-%d %H:%M:%S")
        item['learnStyle'] = resp_dict['data']['learnStyle']
        item['articleId'] = resp_dict['data']['articleId']
        item['favorite'] = resp_dict['data']['favorite']
        item['subscribeUniversity'] = resp_dict['data']['subscribeUniversity']
        item['title'] = resp_dict['data']['title']
        # item['content'] = resp_dict['data']['content'].replace('<p>','').replace('</p>','').replace(' \n','').replace('\n','').replace(' \n','')
        html = etree.HTML(resp_dict['data']['content'])
        item['content'] = ''.join(i.replace('\n', '') for i in html.xpath('//*/text()'))
        print(item['content'])
        item['isNew'] = resp_dict['data']['isNew']
        print(type(item['content']))
        yield item

