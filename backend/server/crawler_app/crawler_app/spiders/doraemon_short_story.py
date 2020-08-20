# -*- coding: utf-8 -*-

"""
Scrapy spider for doraemon short stories.

@author: Nhut Le
"""

import urlparse

from scrapy.http.request import Request
from scrapy.spider import Spider
from scrapy.selector import Selector

from crawler_app.items import MangaMiniItem, MangaItem


class DoraemonShortStorySpider(Spider):
    name = 'doraemon_short_story'
    long_name = 'Doraemon Short Story'
    base_url = 'http://mangak.net/doremon/'

    def start_requests(self):
        yield Request(
            url=self.base_url,
            callback=self.parse_chapters)

    def parse_chapters(self, response):
        """
        Parse chapters

        @url http://mangak.net/doremon/
        @returns requests 1 100
        """

        sel = Selector(response)

        mini_item = MangaMiniItem()
        # mini_item['_id'] = '001'
        mini_item['cover_img_url'] = sel.css('.info_image')\
                                        .xpath('img/@src').extract()[0]
        mini_item['title'] = self.long_name

        mini_item['authors'] = []
        for author in sel.css('.truyen_info_right')\
                         .xpath('li[position()=2]/a'):
            mini_item['authors'].append(author.xpath('text()').extract()[0])

        mini_item['manga_type'] = []
        for manga_type in sel.css('.truyen_info_right')\
                             .xpath('li[position()=3]/a'):
            mini_item['manga_type'].append(
                manga_type.xpath('text()').extract()[0])

        mini_item['status'] = sel.css('.truyen_info_right')\
                                 .xpath('li[position()=4]/a/text()')\
                                 .extract()[0]

        mini_item['translator'] = sel.css('.truyen_info_right')\
                                     .xpath('li[position()=5]/text()')\
                                     .extract()[0]
        mini_item['story_line'] = ''.join(sel.css('.entry-content').xpath(
            'p[position()=1]/text()').extract())
        mini_item['source'] = sel.css('.logo').xpath('text()').extract()[0]

        yield mini_item

        for chapter in sel.css('.chapter-list .row'):
            chapter_url = chapter.xpath('span/a/@href').extract()[0]

            yield Request(
                url=urlparse.urljoin(self.base_url, chapter_url),
                # meta={'manga_id': mini_item['_id']},
                callback=self.parse_chapter
            )

    def parse_chapter(self, response):
        """
        Extract detail

        @url http://mangak.net/doremon-chap-1/
        @returns items 1
        """

        sel = Selector(response)
        # manga_id = response.meta.get('manga_id', '')

        item = MangaItem()
        # item['manga_id'] = manga_id
        item['title'] = sel.css('.name_chapter').xpath('text()').extract()[0]\
            .split(u'\u2013')[0].strip()

        item['img_urls'] = []
        for img in sel.css('.vung_doc').xpath('img'):
            if img.css('.caucav1'):
                continue

            item['img_urls'].append(img.xpath('@src').extract()[0])

        yield item
