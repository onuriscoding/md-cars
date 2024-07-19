from scrapy import Spider, Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowed_domains = ["autoscout24.be"]
    start_urls = ["https://www.autoscout24.be/fr/lst/audi?atype=C&cy=B&desc=0&sort=standard&source=homepage_search-mask&ustate=N%2CU"]

    rules = (
        Rule(LinkExtractor(restrict_css='a[title="Suivant"]'), follow=True),
        Rule(LinkExtractor(restrict_css='a.Link_link__Ajn7I'), callback='parse_item', follow=True),
)


    def parse_item(self, response):
        yield{
            "make": response.css(".StageTitle_boldClassifiedInfo__sQb0l::text").get().strip(),
            "model_name": response.css(".StageTitle_model__EbfjC::text").get().strip(),
            "model_name_info": response.css(".StageTitle_modelVersion__Yof2Z::text").get().strip(),
            "price": response.css(".PriceInfo_price__XU0aF::text").get().strip(),
            #"make_year": response.css(".VehicleOverview_itemText__AI4dA::text").get(),
            #"mileage": response.css(".VehicleOverview_itemText__AI4dA::text")[0].get(),
            "url": response.url
            
        }
