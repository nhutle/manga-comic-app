# utf-8

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class Translator(models.Model):
    name = models.CharField(max_length=100)


class Manga(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    # authors = models.ManyToManyField(
    #     Author, through='MangaAuthor',
    #     through_fields=('manga', 'author'))
    translator = models.CharField(max_length=200)
    # translators = models.ManyToManyField(
    #     Translator, through='MangaTranslator',
    #     through_fields=('manga', 'translator'))
    status = models.CharField(max_length=100)
    story_line = models.TextField(max_length=10000)
    cover_img_url = models.TextField(max_length=500)
    source = models.TextField(max_length=100)


class Chapter(models.Model):
    manga = models.ForeignKey(Manga)
    title = models.CharField(max_length=200)


class Image(models.Model):
    chapter = models.ForeignKey(Chapter)
    img_url = models.CharField(max_length=1000)


class MangaAuthor(models.Model):
    manga = models.ForeignKey(Manga)
    author = models.ForeignKey(Author)


class MangaTranslator(models.Model):
    manga = models.ForeignKey(Manga)
    translator = models.ForeignKey(Translator)
