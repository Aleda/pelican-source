#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = u'Aleda'
SITENAME = u'Aleda | Make Different'
SITEURL = 'http://aleda.cn'
#SITEURL = "http://cq01-rdqa-dev098.cq01.baidu.com:8000"

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404', 'base'))

MENUITEMS = (
        ('Home', 'index.html'),
        ('Categories', 'categories.html'),
        ('Tags', 'tags.html'),
        ('Archives', 'archives.html'),
        ('Search', 'search.html'),
        ('Random Article', 'random.html'),    
        )

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True

FILENAME_METADATA = '(?P<slug>.*)'

ARTICLE_URL = 'article/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'article/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = 'page/{date:%Y}/{date:%m}/{slug}/'
PAGE_SAVE_AS = 'page/{date:%Y}/{date:%m}/{slug}/index.html'
CATEGORY_URL = 'category/{date:%Y}/{date:%m}/{slug}/'
CATEGORY_SAVE_AS = 'category/{date:%Y}/{date:%m}/{slug}/index.html'
TAG_URL = 'tag/{date:%Y}/{date:%m}/{slug}/'
TAG_SAVE_AS = 'tag/{date:%Y}/{date:%m}/{slug}/index.html'
#TAGS_SAVE_AS = 'tag/index.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/Aleda'),
          (u'微博', 'http://weibo.com/u/2189437740'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# THEME
THEME = "pelican-elegant"
