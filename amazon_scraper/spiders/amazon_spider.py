import scrapy
from amazon_scraper.items import AmazonSpiderItem

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    
    # Placeholder URL only (educational)
    start_urls = [
        "https://www.amazon.com/s?k=product-placeholder"
    ]

    def parse(self, response):
        products = response.css('div[data-component-type="s-search-result"]')

        for product in products:
            item = AmazonSpiderItem()

            name = product.css(
                'h2.a-size-medium.a-spacing-none.a-color-base.a-text-normal::text'
            ).get() or ""
            name = name.replace('Sponsored Ad - ', '').strip()

            whole_part = product.css('.a-price-whole::text').get()
            fraction_part = product.css('.a-price-fraction::text').get()
            if whole_part:
                price = whole_part.strip()
                if fraction_part:
                    price = f"{price}.{fraction_part.strip()}"
            else:
                price = "No Price"

            rating = product.css('.a-icon-alt::text').get()
            if rating:
                rating = rating.split(' ')[0]
            else:
                rating = "No Rating"

            reviews = product.css('.a-size-base::text').get() or "No Reviews"

            link = product.css('.s-image::attr(src)').get() or ""
            asin = product.attrib.get('data-asin') or "No ASIN"

            item['name'] = name
            item['price'] = price
            item['rating'] = rating
            item['reviews'] = reviews
            item['link'] = link
            item['asin'] = asin

            yield item

        # Pagination (educational only)
        next_page = response.css("a.s-pagination-next::attr(href)").get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)
