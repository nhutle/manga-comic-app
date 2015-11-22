# -*- coding: utf-8 -*-

"""
Custom pipelines

@author: Nhut Le
"""

from unidecode import unidecode

from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline


class DownloadImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        try:
            yield Request(
                url=item['cover_img_url'],
                meta={
                    'item': item,
                    'is_cover_img': True})
        except:
            pass

        try:
            for img_index, img_url in enumerate(item['img_urls']):
                yield Request(
                    url=img_url,
                    meta={
                        'item': item,
                        'is_cover_img': False,
                        'img_index': img_index})
        except:
            pass

    def file_path(self, request, response=None, info=None):
        item = request.meta.get('item')
        is_cover_img = request.meta.get('is_cover_img')
        img_index = request.meta.get('img_index', 0)
        subdir = info.spider.name

        if is_cover_img:
            img_path = '%s_cover.jpg' % self.remove_asccents(item['title'])
        else:
            img_path = '%s/%s_%s.jpg' % (
                self.remove_asccents(item['title']), self.remove_asccents(
                    item['title']), img_index)

        return '%s/%s' % (subdir, img_path)

    def remove_asccents(self, text):
        return unidecode(
            u'%s' % text.lower()).replace(' ', '_')
