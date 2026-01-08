import scrapy

class AmazonSpiderItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    reviews = scrapy.Field()
    link = scrapy.Field()
    asin = scrapy.Field()
