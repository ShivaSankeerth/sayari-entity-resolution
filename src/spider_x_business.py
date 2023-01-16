import json
import scrapy
from scrapy.crawler import CrawlerProcess

class XBusinessSpider(scrapy.Spider):
    name = "x_business"
    def __init__(self):
        super().__init__()
        self.results = {}
        self.start_urls = ['https://firststop.sos.nd.gov/api/Records/businesssearch']
        self.data = {
            'SEARCH_VALUE': 'X',
            'STARTS_WITH_YN': 'true',
            'ACTIVE_ONLY_YN': 'true'
        }
        
    def start_requests(self):
        yield scrapy.http.JsonRequest(url=self.start_urls[0], callback=self.parse, method='POST', data=self.data)
    
    def parse(self, response):
        text = json.loads(response.text)        
        for key,value in text['rows'].items():
            self.results[key] = {
                'Business Name': value['TITLE'][0],
            }   
            yield scrapy.http.JsonRequest('https://firststop.sos.nd.gov/api/FilingDetail/business/' + key + '/false', 
                                          callback=self.helper, cb_kwargs={'row': key}, method='GET')
    
    def helper(self, response, row):
        text = json.loads(response.text)
        detail_list = text['DRAWER_DETAIL_LIST']
        for item in detail_list:
            self.results[row][item['LABEL']] = item['VALUE']
    
    @staticmethod
    def close(spider, reason):
        print('Closing here',spider.results)
        with open('data/x_business.json', 'w') as f:
            json.dump(spider.results, f)
    
# run spider
if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(XBusinessSpider)
    process.start()

    