import scrapy
import os,glob
import logging
class Skyspider(scrapy.Spider):

    name="crawlbot"
    import os
    
    mylist=[os.path.splitext(filename)[0] for filename in os.listdir('D:\\sky3d\\allpic')]
    start_urls=[]
    for i in mylist:
        i="https://3dsky.org/search?query="+i
        start_urls.append(i)

    st=""
    def parse(self,response):
        self.logger.info("Response:"+str(response).lstrip("<200 https://3dsky.org/search?query=").rstrip(">"))
        self.st=str(response).lstrip("<200 https://3dsky.org/search?query=").rstrip(">")
        urls=response.css('div.item > a::attr(href)').extract()
        
        for url in urls:
            url=response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)
            
    def parse_details(self,response):
        self.logger.info("Response 2:"+self.st)
        yield{
              'model_id':"NULL",
              'model_subcategory':response.css('div.eng > ul >li:nth-child(2) >a::text').extract_first().strip().lstrip('\n').rstrip('\n'),
              'style_id':response.css('div.characteristics_block > ul.characteristics_list >li.icon_type > b::text').extract_first().strip().lstrip('\n').rstrip('\n'),
              'model_title':response.css('div.title > h1::text').extract_first().strip().lstrip('\n').rstrip('\n'),
              'description':response.css('div.show_pre_description::text').extract_first(),
              'description_url':response.css('div.show_pre_description > a::text').extract_first(),
              'category':response.css('div.eng > ul >li:nth-child(1) >a::text').extract_first().strip().lstrip('\n').rstrip('\n'),
              'model_tags':response.css('div.characteristics_block > ul.characteristics_list >li.icon_tags > a::text').extract(),
              
        }
        
   
   