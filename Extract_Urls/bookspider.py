#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:41:02 2019

@author: amalvnair
"""
################ URL Extraction ##################

import scrapy

class BookSpider(scrapy.Spider):
    
    name = 'bookurls'
    #links = []
    allowed_domains = ['']
    start_urls = ['']
    
    def parse(self, response):
        temp = []
        links_div = response.css('div.s-result-list.s-search-results.sg-row')  
        links_div = links_div.css('h2.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-2') 
        temp = links_div.css('a::attr(href)').extract()
        print(temp)
        #self.links = self.links + links_div.css('a::attr(href)').extract() 
        
        with open('Urls.csv','a+') as f:  
            for ls in temp :
                f.write("https://www.example.com{}\n".format(ls)) # write items
        
        next_page = response.css('li.a-last').css('a::attr(href)').extract()
                
        if next_page:
            next_href = next_page[0]
            next_page_url = "https://www.example.com" + next_href
            with open('pages.csv','a+') as f:
                f.write("{}\n".format(next_page_url)) # write items
            request = scrapy.Request(url=next_page_url)
            yield request
        
