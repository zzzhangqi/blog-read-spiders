from scrapy_splash import SplashRequest
import scrapy
from es import ESTransmitData
import blogconfig


class cnblog(scrapy.Spider):
    name = "cnblog"
    ChannelList = blogconfig.blog_link(name)

    def start_requests(self):
        splash_args = {
            'wait': 0.5,
            'timeout': 90,
            'images': 0,
            'resource_timeout': 10
        }

        for url in self.ChannelList:
            yield SplashRequest(url, self.cnblog_result, endpoint='render.html', args=splash_args)

    def cnblog_result(self, response):
        """
        :param response:
        :return: cnblog Read Count
        """
        CnblogReadTitleList = response.xpath('//a[@id="cb_post_title_url"]')
        for span in CnblogReadTitleList.xpath('.//span/text()'):
            CnblogReadTitle = span.get()
        CnblogReadCount = response.xpath('//span[@id="post_view_count"]/text()').extract()
        DocName = blogconfig.blog_doc_name(self.name, response.url)
        ESTransmitData(self.name, DocName, CnblogReadTitle, int(CnblogReadCount[0]))
