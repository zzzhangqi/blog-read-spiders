import re
import time

from scrapy_splash import SplashRequest
import scrapy
from es import ESTransmitData
import blogconfig


class tencent(scrapy.Spider):
    name = "tencent"
    ChannelList = blogconfig.blog_link(name)

    def start_requests(self):
        splash_args = {
            'wait': 0.5,
            'timeout': 90,
            'images': 0,
            'resource_timeout': 10
        }

        for url in self.ChannelList:
            yield SplashRequest(url, self.tencent_result, endpoint='render.html', args=splash_args)

    def tencent_result(self, response):
        """
        :param response:
        :return: tencent read count
        """

        TencentReadTitle = response.xpath('//h1[@class="article-title J-articleTitle"]')
        for h1 in TencentReadTitle.xpath('.//span/text()'):
            TencentReadTitle = h1.get()

        TencentReadCountList = response.xpath('//span[@class="article-info"]/text()').getall()
        DocName = blogconfig.blog_doc_name(self.name, response.url)

        ESTransmitData(self.name, DocName, TencentReadTitle, int(TencentReadCountList[1]))
