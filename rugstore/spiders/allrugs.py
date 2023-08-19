import scrapy


class AllrugsSpider(scrapy.Spider):
    name = "allrugs"
    allowed_domains = ["therugshop.co.uk"]
    start_urls = ["https://www.therugshopuk.co.uk/rugs-by-type/rugs.html"]

    def parse(self, response):
        for item in response.css('div.product-item-info'):
            yield {
                'name': item.css('img.product-image-photo.image::attr(alt)').get(),
                'price': item.css('div.price-box.price-final_price::text').get(),
                'url': item.css('a.product-item-link::attr(href)').get()
            }
            
            next_page = response.css('a[title=Next]::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback = self.parse)

