import re
from scrapy_splash import SplashRequest
import scrapy
from es import ESTransmitData
import blogconfig


class juejin(scrapy.Spider):
    name = "juejin"
    ChannelList = blogconfig.blog_link(name)

    def start_requests(self):
        splash_args = {
            'wait': 0.5,
            'timeout': 90,
            'images': 0,
            'resource_timeout': 10
        }

        for url in self.ChannelList:
            yield SplashRequest(url, self.juejin_result, endpoint='render.html', args=splash_args)

    def juejin_result(self, response):
        """
        :param response:
        :return: juejin read count
        """
        JJReadTitle = response.xpath('//meta[@itemprop="headline"]/@content').getall()

        ReadCountPattern = re.compile(r'viewsCount.[0-9]{1,100}')
        JJReadCountList = response.xpath('//script').getall()
        ReadCountStr = JJReadCountList[7]
        JJReadCount = ReadCountPattern.search(ReadCountStr).group()
        JJReadCountRp = JJReadCount.replace('viewsCount:', '')

        DocName = blogconfig.blog_doc_name(self.name, response.url)
        ESTransmitData(self.name, DocName, JJReadTitle[0], int(JJReadCountRp))
