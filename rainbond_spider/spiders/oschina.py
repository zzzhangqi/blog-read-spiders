import time

from scrapy_splash import SplashRequest
import scrapy
from es import ESTransmitData
import blogconfig


class oschina(scrapy.Spider):

    name = "oschina"
    ChannelList = blogconfig.blog_link(name)

    def start_requests(self):
        splash_args = {
            'wait': 0.5,
            'timeout': 90,
            'images': 0,
            'resource_timeout': 10
        }

        for url in self.ChannelList:
            yield SplashRequest(url, self.osChina_result, endpoint='render.html', args=splash_args)

    def osChina_result(self, response):
        """
        :param response:
        :return: osChina Read Count
        """
        osChinaReadTitle = ''
        osChinaReadTitleList = response.xpath('//h1[@class="article-box__title"]')
        for a in osChinaReadTitleList.xpath('.//a/text()'):
            osChinaReadTitle = a.get()

        osChinaReadCount = ''
        osChinaReadCountList = response.xpath('//div[@class="article-box__meta"]')
        for divs in osChinaReadCountList.xpath('.//div[@class="item lm"]/text()'):
            osChinaReadCountGet = divs.get()
            osChinaReadCount = osChinaReadCountGet.replace('阅读数', '').replace(' ', '')
        DocName = blogconfig.blog_doc_name(self.name, response.url)

        ESTransmitData(self.name, DocName, osChinaReadTitle, int(osChinaReadCount))
