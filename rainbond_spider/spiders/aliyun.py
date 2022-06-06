from scrapy_splash import SplashRequest
import scrapy
from es import ESTransmitData
import blogconfig


class aliyun(scrapy.Spider):
    name = "aliyun"
    ChannelList = blogconfig.blog_link(name)

    def start_requests(self):
        splash_args = {
            'wait': 0.5,
            'timeout': 90,
            'images': 0,
            'resource_timeout': 10
        }

        for url in self.ChannelList:
            yield SplashRequest(url, self.aliyun_result, endpoint='render.html', args=splash_args)

    def aliyun_result(self, response):
        """
        :param response:
        :return: aliyun read count
        """
        AliyunReadTitle = response.xpath('//h1[@class="article-title"]/text()').getall()
        AliyunReadTitleStr = AliyunReadTitle[0]
        AliyunReadCount = response.xpath('//span[@class="article-info-read"]/text()').getall()
        AliyunReadCountNum = int(AliyunReadCount[0])
        DocName = blogconfig.blog_doc_name(self.name, response.url)
        ESTransmitData(self.name, DocName, AliyunReadTitleStr, AliyunReadCountNum)
