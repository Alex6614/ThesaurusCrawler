import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from thesaurus.items import ThesaurusItem

class MySpider(CrawlSpider):
    #def __init__(self, lookup="", *args, **kwargs):
     #   super(MySpider, self).__init__(*args, **kwargs)
      #  self.lookup = lookup
    name = 'thesaurusspider'
    def __init__(self, *args, **kwargs): 
        self.start_urls = ["http://www.thesaurus.com/browse/%s" %kwargs.get('start_url')] 
        self.allowed_domains = ["thesaurus.com"]
        self.rules = (
            Rule(LinkExtractor(restrict_xpaths=("//div[id='paginator']//a/@href"))),
            Rule(LinkExtractor(allow=('http://www.thesaurus.com/browse/%s/.$' %kwargs.get('start_url'), 'http://www.thesaurus.com/browse/%s/..$' %kwargs.get('start_url'))), callback='parse_item', follow=True)
        )
        super(MySpider, self).__init__(*args, **kwargs) 
    # try and delete %s then add in bug
    #start_urls = [
    #    "http://www.thesaurus.com/browse/%s" %lookup
    #]

    def parse_start_url(self, response):
        for sel in response.xpath("//div[contains(@class, 'syn_of_syns')]"):
            print(sel)
            item = ThesaurusItem()
            item['mainsynonym'] = sel.xpath("div/div/div/a/text()").extract()
            item['definition'] = sel.xpath("div/div/div[@class='def']/text()").extract()
            item['secondarysynonym'] = sel.xpath('div/div/ul/li/a/text()').extract()
            yield item

    def parse_item(self, response):
        for sel in response.xpath("//div[contains(@class, 'syn_of_syns')]"):
            print(sel)
            item = ThesaurusItem()
            item['mainsynonym'] = sel.xpath("div/div/div/a/text()").extract()
            item['definition'] = sel.xpath("div/div/div[@class='def']/text()").extract()
            item['secondarysynonym'] = sel.xpath('div/div/ul/li/a/text()').extract()
            yield item
