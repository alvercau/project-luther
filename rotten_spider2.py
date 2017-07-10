import scrapy
import numpy as np
import pandas as pd


class ExampleSpider(scrapy.Spider):
    name = 'rotten_spider2'

    custom_settings = {
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 3,
        "HTTPCACHE_ENABLED": True
    }

    df = pd.read_pickle('/Users/aleksandra/ds/metis/project_luther/all_data.pkl')
    start_urls = df.url.tolist()

    # def parse(self, urls):
    #     for href in urls:
    #         # For each festival link, call 'parse_festival' (defined later)
    #         yield scrapy.Request(
    #             url=href,
    #             callback=self.parse_movie,
    #             meta={'url':href}
    #         )

    def parse(self, response):
        url = response.url
        score_c = response.xpath('//a[@id="tomato_meter_link"]/span/span/text()').extract_first()
        rating_c = response.xpath('//*[contains(text(), "Average Rating")]/following-sibling::text()').extract_first().strip()
        n_reviews_c = response.xpath('//*[contains(text(), "Reviews Counted")]/following-sibling::span/text()').extract_first()
        fresh_c = response.xpath('//*[contains(text(), "Fresh")]/following-sibling::span/text()').extract_first()
        rotten_c = response.xpath('//*[contains(text(), "Rotten")]/following-sibling::span/text()').extract_first()
        score_u = response.xpath('//div[@class="meter-value"]/span/text()').extract_first()
        rating_u = response.xpath('//*[contains(text(), "Average Rating")]/following-sibling::text()').extract()[1].strip()
        n_reviews_u = response.xpath('//*[contains(text(), "User Ratings")]/following-sibling::text()').extract_first().strip()
        director = response.xpath('//*[contains(text(), "Directed By")]/following-sibling::div/a/text()').extract_first()
        box_office = response.xpath('//*[contains(text(), "Box Office:")]/following-sibling::div/text()').extract_first()
        runtime = response.xpath('//*[contains(text(), "Runtime")]/following-sibling::div/time/@datetime').extract_first()
        in_theatre = response.xpath('//*[contains(text(), "In Theaters")]/following-sibling::div/time/@datetime').extract_first()
        on_disc = response.xpath('//*[contains(text(), "On Disc")]/following-sibling::div/time/@datetime').extract_first()
        audience = response.xpath('//*[contains(text(), "Rating")]/following-sibling::div/text()').extract_first()
        studio = response.xpath('//*[contains(text(), "Studio")]/following-sibling::div/a/text()').extract_first()

        yield {
            'url': url,
            'score_c': score_c,
            'rating_c': rating_c,
            'n_reviews_c' : n_reviews_c,
            'fresh_c': fresh_c,
            'rotten_c': rotten_c,
            'score_u':score_u,
            'rating_u': rating_u,
            'n_reviews_u': n_reviews_u,
            'director': director,
            'box_office': box_office,
            'runtime': runtime,
            'in_theatre': in_theatre,
            'on_disc': on_disc,
            'audience': audience,
            'studio': studio}

