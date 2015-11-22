# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img_url', models.CharField(max_length=1000)),
                ('chapter', models.ForeignKey(to='manga_comic_app.Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=100)),
                ('story_line', models.TextField(max_length=10000)),
                ('cover_img_url', models.TextField(max_length=500)),
                ('source', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MangaAuthor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.ForeignKey(to='manga_comic_app.Author')),
                ('manga', models.ForeignKey(to='manga_comic_app.Manga')),
            ],
        ),
        migrations.CreateModel(
            name='MangaTranslator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manga', models.ForeignKey(to='manga_comic_app.Manga')),
            ],
        ),
        migrations.CreateModel(
            name='Translator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='mangatranslator',
            name='translator',
            field=models.ForeignKey(to='manga_comic_app.Translator'),
        ),
        migrations.AddField(
            model_name='manga',
            name='authors',
            field=models.ManyToManyField(to='manga_comic_app.Author', through='manga_comic_app.MangaAuthor'),
        ),
        migrations.AddField(
            model_name='manga',
            name='translators',
            field=models.ManyToManyField(to='manga_comic_app.Translator', through='manga_comic_app.MangaTranslator'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='manga',
            field=models.ForeignKey(to='manga_comic_app.Manga'),
        ),
    ]
