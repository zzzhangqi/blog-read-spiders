import logging
from scrapy_splash import SplashRequest
import scrapy
from es import ESTransmitData
import blogconfig


class sf(scrapy.Spider):
    name = "sf"
    # ChannelList = blogconfig.blog_link(name)

    def start_requests(self):
        splash_args = {
            'wait': 0.5,
            'timeout': 90,
            'images': 0,
            'resource_timeout': 10
        }

        for url in self.ChannelList:
            yield SplashRequest(url, self.sf_result, endpoint='render.html', args=splash_args)

    def sf_result(self, response):
        """
        :param response:
        :return: sf read count
        """
        result = response.xpath('//div')
        if result:
            SFReadTitle = ''
            SFReadTitleList = response.xpath('//div[@class="p-lg-30 position-relative card-body"]')
            for div in SFReadTitleList.xpath('.//a[@class="text-body"]/text()'):
                SFReadTitle = div.getall()

            SFReadCount = response.xpath('//div[@class="col"]/span/text()').getall()
            SFReadCountNum = int(SFReadCount[1])
            DocName = blogconfig.blog_doc_name(self.name, response.url)
            ESTransmitData(self.name, DocName, SFReadTitle[0], SFReadCountNum)
        else:
            logging.error('The returned data is empty')
            # self.start_requests
