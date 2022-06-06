import re

from scrapy_splash import SplashRequest
import scrapy
from es import ESTransmitData
import blogconfig


class k8s(scrapy.Spider):

    name = "k8s"
    ChannelList = blogconfig.blog_link(name)

    def start_requests(self):
        splash_args = {
            'wait': 0.5,
            'timeout': 90,
            'images': 0,
            'resource_timeout': 10
        }

        for url in self.ChannelList:
            yield SplashRequest(url, self.k8s_result, endpoint='render.html', args=splash_args)

    def k8s_result(self, response):
        """
        :param response:
        :return: k8s Read Count
        """
        k8sReadTitleList = response.xpath('//h1[@class="article-title"]')
        for a in k8sReadTitleList.xpath('.//a/text()'):
            k8sReadTitle = a.get()
        k8sReadCount = response.xpath('//span[@class="item post-views"]/text()').get()
        k8sReadCountRp = k8sReadCount.replace('阅读', '').replace('(', '').replace(')', '')
        DocName = blogconfig.blog_doc_name(self.name, response.url)
        ESTransmitData(self.name, DocName, k8sReadTitle, int(k8sReadCountRp))
