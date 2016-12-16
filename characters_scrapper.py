import scrapy
from scrapy.selector import Selector

class BlogSpider(scrapy.Spider):
    name = 'characterspider'
    start_urls = ['https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Personnage_d\'animation']

    def parse(self, response):
        for link in response.css('div#mw-pages div.mw-content-ltr li'):
            yield {'character': link.css('a ::text').extract_first()}

#         next_pages = response.css('div.pagination.row > a').extract()
#         for index, page in enumerate(next_pages):
#             if 'class="active"' in page:
#                 n_page = next_pages[index + 1]
#                 next_page = Selector(text=n_page).xpath('//a/@href').extract()
#                 next_page_url = next_page[0]
#                 if index == (len(next_pages) - 1):
#                     next_page = False
        
#         if next_page:
#            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)
# #EOF