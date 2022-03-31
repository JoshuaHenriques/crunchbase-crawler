import scrapy


class CrunchbaseSpider(scrapy.Spider):
    name = 'crunchbase'
    allowed_domains = ["crunchbase.com"]
    start_urls = (
        'https://www.crunchbase.com',
    )

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })

    def parse(self, response):
        test = response.xpath("/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/authentication-page/page-layout/div/div/div[2]/authentication/mat-card/mat-tab-group/div/mat-tab-body[1]/div/login/form/button/span[1]//text()")
        print(f'THIS IS TEST: {test}')