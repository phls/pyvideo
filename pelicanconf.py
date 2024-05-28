#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import json
import os

AUTHOR = "Software Livre Brasil"
SITENAME = "Vídeos de Software Livre no Brasil"
SITEURL = 'https://videos.gnulinux.com.br'
TEMPLATE_PAGES = {
    'languages.html': 'languages.html',
}

PATH = 'content'
DATA_DIR = 'conferences'
NO_PUBLISH_FILE = 'NO_PUBLISH.json'
IGNORE_FILES = [
    '.#*',
    'category.json',
    'CONTRIBUTING.rst',
    'CONTRIBUTORS_WITHOUT_COMMITS.rst',
    NO_PUBLISH_FILE,
    'README.rst',
    '*.schemas/video.json',
    '*posters/apsimregions-a-gridded-modeling-framework-for-th.json',
]

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt_BR'

DEFAULT_PAGINATION = 10

DEFAULT_CATEGORY = "Undefined"

AUTHOR_URL = AUTHOR_SAVE_AS = 'palestrante/{slug}.html'
ARTICLE_URL = ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_LANG_URL = ARTICLE_LANG_SAVE_AS = '{category}/{slug}-{lang}.html'
DRAFT_URL = DRAFT_SAVE_AS = 'drafts/{category}/{slug}.html'
DRAFT_LANG_URL = DRAFT_LANG_SAVE_AS = 'drafts/{category}/{slug}-{lang}.html'
PAGE_URL = PAGE_SAVE_AS = 'paginas/{slug}.html'
PAGE_LANG_URL = PAGE_LANG_SAVE_AS = 'paginas/{slug}-{lang}.html'
CATEGORY_URL = CATEGORY_SAVE_AS = 'eventos/{slug}.html'
TAGS_URL = TAGS_SAVE_AS = 'tags.html'
# Hack to avoid this issue: https://github.com/getpelican/pelican/issues/1137
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
# End hack to avoid issue #1137
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%b}/index.html'
CATEGORIES_SAVE_AS = 'eventos.html'
AUTHORS_SAVE_AS = 'palestrantes.html'

USE_FOLDER_AS_CATEGORY = False

# Feeds
FEED_MAX_ITEMS = 100
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/event_{slug}.atom.xml'
CATEGORY_FEED_RSS = 'feeds/event_{slug}.rss.xml'
AUTHOR_FEED_ATOM = 'feeds/speaker_{slug}.atom.xml'
AUTHOR_FEED_RSS = 'feeds/speaker_{slug}.rss.xml'
TAG_FEED_ATOM = 'feeds/tag_{slug}.atom.xml'
TAG_FEED_RSS = 'feeds/tag_{slug}.rss.xml'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True

THEME = 'themes/slvideo/'

GITHUB_URL = 'https://github.com/phls/pyvideo'
#CONTRIBUTE_URL = 'https://github.com/pyvideo/pyvideo/wiki/How-to-Contribute-Media'
#API_URL = 'https://api.pyvideo.org'
API_URL = 'http://videos.softwarelivre.org'

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/CNAME',
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'pelican_alias',
    'drop_no_publish',
    'json_reader',
    'replace_underscore',
    'extended_sitemap',
    'event_series',
    'event_info',
    'aggregations',
    'writer',
]

# https://en.wikipedia.org/wiki/ISO_639-3
# https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes
VIDEO_LANGUAGE_NAMES = {
    'ita': 'Italian',
    'zho': 'Chinese',
    'por': 'Portuguese',
    'ukr': 'Ukrainian',
    'deu': 'German',
    'eng': 'English',
    'rus': 'Russian',
    'fra': 'French',
    'spa': 'Spanish',
    'eus': 'Basque',
    'cat': 'Catalan',
    'glg': 'Galician',
    'kor': 'Korean',
    'lit': 'Lithuanian',
    'jpn': 'Japanese',
    'slk': 'Slovak',
    'pol': 'Polish',
    'heb': 'Hebrew',
    'tha': 'Thai',
    'ces': 'Czech',
}


def jinja_language_name(code):
    return VIDEO_LANGUAGE_NAMES.get(code, code)

JINJA_FILTERS = {
    'language_name': jinja_language_name,
    'commafy': lambda v: "{:,}".format(v)
}

try:
    PR_NUMBER = int(os.environ.get('TRAVIS_PULL_REQUEST'))
except (TypeError, ValueError):
    PR_NUMBER = None
