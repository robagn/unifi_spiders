import scrapy
#from __future__ import absolute_import 
from unifi.items import UnifiItem
from scrapy.selector import Selector

class UnifiSpider(scrapy.Spider):
	name="unifi_it"
	allowed_domains = ["unifi.it"]
	start_urls = ["http://www.unifi.it/vp-9333-scuole.html"]        
	
	def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('//ul/li')
		items = []
#		item=UnifiItem()
#		filename = response.url.split("/")[-2]
# 		with open(filename, 'wb') as f:
#  			f.write(response.body)
		for site in sites:
			#for sel in response.xpath('//ul/li'):
 			item=UnifiItem()
 			item['name'] = site.xpath('strong/a/text()').extract()
 			item['url'] = site.xpath('strong/a/@href').extract()
 			item['ref'] = site.xpath('a[contains(@href,"cercachi")]/text()').extract()#.re('-\s[^\n]*\\r')
 			if len(item['name'])>0:
				items.append(item)
			print 'pppp'
		return items	
			





