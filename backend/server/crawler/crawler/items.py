# -*- coding: utf-8 -*-

"""
Scrapy model

@author Nhut Le
"""

from scrapy.item import Item, Field
# from scrapy_djangoitem import DjangoItem
# from


# # class MangaItemDjango(DjangoItem):
#     django_model = Manga


class MangaMiniItem(Item):
    # _id = Field(type='str')
    title = Field(type='str')
    authors = Field(type='list')
    translator = Field(type='str')
    status = Field(type='str')
    manga_type = Field(type='list')
    story_line = Field(type='str')
    cover_img_url = Field(type='str')
    source = Field(type='str')


class MangaItem(Item):
    # _id = Field(type='str')
    # manga_id = Field(type='str')
    title = Field(type='str')
    img_urls = Field(type='list')
