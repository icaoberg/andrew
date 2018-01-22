#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'icaoberg'
SITENAME = u'icaoberg AT scs cmu edu'
SITEURL = 'http://www.scs.cmu.edu/~icaoberg'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('github', 'http://github.com/icaoberg'),
	  ('twitter', 'http://twitter.com/icaoberg'),
          ('linkedin', 'https://www.linkedin.com/in/icaoberg'),
          ('facebook', 'https://www.facebook.com/icaoberg'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = './pelican-bold'

DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = ['extra', 'images', 'pdfs']

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['gallery', 'pelican_gist', 'pelican_youtube', 'sitemap', 'tag_cloud']

GALLERY_PATH = 'images/gallery'
PHOTO_EXIF_COPYRIGHT_AUTHOR = 'icaoberg AT andrew DOT cmu DOT edu'
PHOTO_EXIF_COPYRIGHT = 'COPYRIGHT'

RESPONSIVE_IMAGES = True
FIGURE_NUMBERS = True

TWITTER_USERNAME = 'icaoberg'

COPYRIGHT = 'Copyright (c) 2006-2018 icaoberg AT cmu DOT edu'

#FEED_ALL_RSS = 'feeds/all.rss.xml'
#CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

SITESUBTITLES = ('school of computer science', 'computational biology')

# Configuration for the "sitemap" plugin 
SITEMAP = { 'format': 'xml', 'priorities': { 'articles': 1, 'indexes': 0.5, 'pages': 0.5, }, 'changefreqs': { 'articles': 'always', 'indexes': 'hourly', 'pages': 'monthly' } }