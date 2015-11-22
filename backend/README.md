Spider Documentation
====================================

1. What we need to crawl
------------------------

We need to crawl manga/comic and its chapters listed at [#2](#2-list-of-mangacomic). There are 2 kinds of items needed to collect: mini_item and item.

* manga_comic -> yield mini_item
    * **_id**: **string**, on-going consideration: automatically generating/manually assigning
    * **title**: **string**, title of the manga/comic
    * **author**: **string**, author's name of the manga/comic
    * **translators**: **list** of strings, name of translators
    * **status**: **string**, current status (on-going/finished)
    * **type**: **list**, list of types (horor, romantic, etc.)
    * **story_line**: **string**, the plot of the manga/comic
    * **cover_img**: **string**, url to the cover image
    * **source**: **string**, url to website in which the manga/comic belongs

* chapter -> yield item
    * **_id**: **string**, on-going consideration: automatically generating/manually assigning
    * **story_id**: **string**, id of the manga/comic in which the chapter belongs to
    * **title**: **string**, title of the chapter
    * **hero_img**: **string**, url to the hero image
    * **imgs**: **list**, list of urls to all the images of the chapter

2. List of comic/manga
----------------------

* Doraemon: http://doraemon.com
* Dragon Ball: http://dragonball.com

3. Exporting data
-----------------

Presently, all data will be exported in json format.











