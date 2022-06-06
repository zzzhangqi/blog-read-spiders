import re

from scrapy_splash import SplashRequest
import scrapy
from es import ESTransmitData
import blogconfig


class cto(scrapy.Spider):

    name = "51cto"
    ChannelList = blogconfig.blog_link(name)

    def start_requests(self):
        splash_args = {
            'wait': 0.5,
            'timeout': 90,
            'images': 0,
            'resource_timeout': 10
        }

        for url in self.ChannelList:
            yield SplashRequest(url, self.cto_result, endpoint='render.html', args=splash_args)

    def cto_result(self, response):
        """
        :param response:
        :return: 51cto Read Count
        """
        CtoReadTitle = ''
        CtoReadTitleList = response.xpath('//div[@class="title"]')
        for em in CtoReadTitleList.xpath('.//h1/text()'):
            CtoReadTitle = em.get()
        CtoReadCountList = response.xpath('//p[@class="clearfix mess-tag"]')

        CtoReadCount = ''
        for b in CtoReadCountList.xpath('.//b[@class="fl"]/text()'):
            CtoReadCount = b.get()

        DocName = blogconfig.blog_doc_name(self.name, response.url)
        ESTransmitData(self.name, DocName, CtoReadTitle, int(CtoReadCount))
