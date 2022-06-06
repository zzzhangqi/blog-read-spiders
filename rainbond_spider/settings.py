# Scrapy settings for rainbond_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = 'rainbond_spider'

SPIDER_MODULES = ['rainbond_spider.spiders']
NEWSPIDER_MODULE = 'rainbond_spider.spiders'

LOG_LEVEL = os.getenv("LOG_LEVEL", default="ERROR")

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

SPLASH_URL = 'http://192.168.3.162:8050'

# Deduplication filter
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

# Using Splash's Http cache
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

# Configure the middle key
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
SPIDER_MIDDLEWARES = {
     # Set up scrapy_splash Parameters
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}