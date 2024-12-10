from typing import Any

import scrapy
from scrapy.http import Response


class RztkSpider(scrapy.Spider):
    name = "rozetka"
    start_urls = ["https://rozetka.com.ua/ua/wishlist/aa723160c54053078/"]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        wishlist_items = response.css("div.goods-tile")
        for item in wishlist_items:
            item_id = item.css("div.g-id::text").get()
            item_title = item.css("span.goods-tile__title")
            prices = item.css("div.goods-tile__prices")
            yield {
                "id": item_id,
                "brand": item_title.css("strong.ng-star-inserted::text").get(),
                "title": item_title.css("::text").getall()[-1].strip(),
                "price_old": prices.css("div.goods-tile__price--old::text").get("").replace(u'\xa0', u' '),
                "price_current": prices.css("span.goods-tile__price-value::text").get("").replace(u'\xa0', u' '),
            }
