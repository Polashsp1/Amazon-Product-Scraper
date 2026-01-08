BOT_NAME = 'amazon_scraper'

SPIDER_MODULES = ['amazon_scraper.spiders']
NEWSPIDER_MODULE = 'amazon_scraper.spiders'

# Disable obeying robots.txt (for educational purpose only)
ROBOTSTXT_OBEY = False

# Configure item pipelines (optional)
ITEM_PIPELINES = {
    'amazon_scraper.pipelines.AmazonScraperPipeline': 300,
}

# Download delay to prevent IP ban
DOWNLOAD_DELAY = 5
