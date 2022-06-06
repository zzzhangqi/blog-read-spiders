import re
from scrapy_splash import SplashRequest
import scrapy
from es import ESTransmitData
import blogconfig


class itpub(scrapy.Spider):

    name = "itpub"
    ChannelList = blogconfig.blog_link(name)

    def start_requests(self):
        splash_args = {
            'wait': 0.5,
            'timeout': 90,
            'images': 0,
            'resource_timeout': 10
        }

        for url in self.ChannelList:
            yield SplashRequest(url, self.itpub_result, endpoint='render.html', args=splash_args)

    def itpub_result(self, response):
        """
        :param response:
        :return: itpub read count
        """
        itpubReadTitle = response.xpath('//h1[@class="preview-title "]/text()').getall()
        itpubReadCount = response.xpath('//span[@class="icon-see"]/text()').getall()
        DocName = blogconfig.blog_doc_name(self.name, response.url)
        ESTransmitData(self.name, DocName, itpubReadTitle[0], int(itpubReadCount[0]))
