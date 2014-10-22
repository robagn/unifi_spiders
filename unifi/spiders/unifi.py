import scrapy
#from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
	name="unifi"
	allowed_domains = ["dmoz.org"]
	start_urls = ["http://www.unifi.it/vp-9333-scuole.html"]        
	
	def parse(self, response):
		filename = response.url.split("/")[-2]
		with open(filename, 'wb') as f:
 			f.write(response.body)
		# for sel in response.xpath('//ul/li'):
# 			item=DmozItem()
# 			item['title'] = sel.xpath('a/text()').extract()
# 			item['link'] = sel.xpath('a/@href').extract()
# 			item['desc'] = sel.xpath('text()').re('-\s[^\n]*\\r')
# 			yield item