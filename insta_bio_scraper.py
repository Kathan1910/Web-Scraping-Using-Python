import scrapy


class InstaBioScraperSpider(scrapy.Spider):
    name = "insta_bio_scraper"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
