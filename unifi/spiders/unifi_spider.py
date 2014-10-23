import scrapy
#from __future__ import absolute_import 
from unifi.items import UnifiItem

class UnifiSpider(scrapy.Spider):
	name="unifi_it"
	allowed_domains = ["unifi.it"]
	start_urls = ["http://www.unifi.it/vp-9333-scuole.html"]        
	
	def parse(self, response):
		filename = response.url.split("/")[-2]
# 		with open(filename, 'wb') as f:
#  			f.write(response.body)
		for sel in response.xpath('//ul/li'):
 			item=UnifiItem()
 			item['name'] = sel.xpath('/@name').extract()
 			item['url'] = sel.xpath('a/@href').extract()
 			item['ref'] = sel.xpath('br/a/text()').re('-\s[^\n]*\\r')
 			yield item
			print 'k'