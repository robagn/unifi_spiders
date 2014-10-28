import scrapy
from scrapy.spider import Spider
from scrapy.item import Item, Field
from unifi.items import UnifiItem
from scrapy.selector import Selector
from scrapy.http import FormRequest, Request
from scrapy.selector import HtmlXPathSelector

class UnifiSpider2(Spider):
    name = "unifi_form"
    #allowed_domains = ["unifi.it"]
    start_urls = ["http://www.unifi.it/cercachi-searchp.html"]
	# def after_submit(self,response):
		# #hxs = HtmlXPathSelector(response)
		# #text_of_result = hxs.select('//div[@id=\'scrape\']/text()'
		# print response
		# return
		
    def parse(self, response):
        print[FormRequest.from_response(
				response,
				formdata={"cognome": 'a'},
				)]
				#callback=self.aftersearch)]
				
	def aftersearch(self):
		hxs = HtmlXPathSelector(response)
		print hxs


	
	

    