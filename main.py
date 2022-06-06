from scrapy.utils.log import configure_logging
from twisted.internet import reactor, defer
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner
import blogconfig

configure_logging()
runner = CrawlerRunner(get_project_settings())


@defer.inlineCallbacks
def crawl():
    channelList = blogconfig.blog_channel()
    for List in channelList:
        yield runner.crawl(List)
    # yield runner.crawl('itpub')
    reactor.stop()


if __name__ == "__main__":
    crawl()
    reactor.run()
