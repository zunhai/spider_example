# -*- coding: utf-8 -*-
# Scrapy settings for RedisSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#更改调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

#更改去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

#不清理redis队列false是清理
# （如果这一项为True，那么在Redis中的URL不会被Scrapy_redis清理掉，这样的好处是：爬虫停止了再重新启动
# 它会从上次暂停的地方开始继续爬取。但是它的弊端也很明显，如果有多个爬虫都要从这里读取URL，需要另外写一段代码来防止重复爬取。
# 如果设置成了False，那么Scrapy_redis每一次读取了URL以后，就会把这个URL给删除。这样的好处是：
# 多个服务器的爬虫不会拿到同一个URL，也就不会重复爬取。但弊端是：爬虫暂停以后再重新启动，它会重新开始爬。）

# SCHEDULER_PERSIST =True;

# REDIS_HOST='127.0.0.1';

# REDIS_PORT=6379;


REDIS_URL = None

BOT_NAME = 'RedisSpider'

SPIDER_MODULES = ['RedisSpider.spiders']
NEWSPIDER_MODULE = 'RedisSpider.spiders'


# -----------启用scrapyredis的重复过滤器模块，原有重复过滤器将停用
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# -----------启用scrapyredis中的调度器，该调度器具有与redis数据库交互的功能，原有的调度器将停用
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# -----------设置调度器请求队列保持，可以实现爬虫的断点续爬
SCHEDULER_PERSIST = True

# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    # 'JD.pipelines.ExamplePipeline': 300,
    # ---------scrapyredis管道
    'scrapy_redis.pipelines.RedisPipeline': 400,
}
# ------------指定redis数据库地址
REDIS_URL = 'redis://192.168.1.52:6379'

LOG_LEVEL = 'DEBUG'




# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Tianqi (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'Tianqi.middlewares.TianqiSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'Tianqi.middlewares.TianqiDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'Tianqi.pipelines.TianqiPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
