#!/usr/bin/python
# filename: run.py
import re
from crawler import Crawler, CrawlerCache

if __name__ == "__main__": 
    # Using SQLite as a cache to avoid pulling twice
    crawler = Crawler(CrawlerCache('maroofcat2.db'))
    root_re = re.compile('^/$').match
    urllist=["https://maroof.sa/BusinessType/BusinessesByTypeList?bid=23&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=14&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=24&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=25&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=16&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=26&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=34&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=35&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=41&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=47&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=48&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=49&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=51&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=39&sortProperty=BestRating&DESC=True",
"https://maroof.sa/BusinessType/BusinessesByTypeList?bid=45&sortProperty=BestRating&DESC=True"]



    # for links in urllist:
    #     print links
    #     crawler.crawl(links, no_cache=root_re)
    crawler.crawl('https://maroof.sa/BusinessType/BusinessesByTypeList?bid=23&sortProperty=BestRating&DESC=True', no_cache=root_re)
    # crawler.crawl('http://gizmodo.com/', no_cache=root_re)
    # crawler.crawl('http://www.zdnet.com/', no_cache=root_re)
    # crawler.crawl('http://www.wired.com/', no_cache=root_re)
    print crawler.content['techcrunch.com'].keys()