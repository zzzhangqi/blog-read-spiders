import re

from scrapy_splash import SplashRequest
import scrapy
from es import ESTransmitData
import blogconfig


class csdn(scrapy.Spider):

    name = "csdn"
    ChannelList = blogconfig.blog_link(name)

    def start_requests(self):
        splash_args = {
            'wait': 0.5,
            'timeout': 90,
            'images': 0,
            'resource_timeout': 10
        }

        for url in self.ChannelList:
            yield SplashRequest(url, self.csdn_result, endpoint='render.html', args=splash_args)

    def csdn_result(self, response):
        """
        :param response:
        :return: csdn Read Count
        """
        CsdnReadTitle = response.xpath('//h1[@id="articleContentId"]/text()').extract()
        CsdnReadCount = response.xpath('//span[@class="read-count"]/text()').extract()
        CsdnReadCountNum = CsdnReadCount[0]
        DocName = blogconfig.blog_doc_name(self.name, response.url)
        ESTransmitData(self.name, DocName, CsdnReadTitle[0], int(CsdnReadCountNum))
