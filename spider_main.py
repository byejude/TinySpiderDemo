#!usr/bin/env python2
# -*- coding: UTF-8 -*-
import url_manage
import html_downloader
import html_parse
import html_outputer



class spider_main(object):
    def __init__(self):
        self.urls = url_manage.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parse.HtmlParse()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d:%s'% (count,new_url)
                html_content = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 10:
                    break
                count += 1

            except:
                print 'craw failed'

        self.outputer.output_html()



if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/item/Python'
    spider = spider_main()
    spider.craw(root_url)






