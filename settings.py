# -*- coding: utf-8 -*-
AUTHOR = u'Salt-fr'
SITENAME = u"Salt-fr"
TAGLINE = u"Rencontres des utilisateurs francophones de Salt"
SITEURL = 'http://salt-fr.afpy.org'

PATH = 'sources/'
OUTPUT_PATH = 'www/'

ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

TIMEZONE = 'Europe/Paris'

PLUGIN_PATHS = ["pelican-plugins/"]
PLUGINS = ['gravatar', "optimize_images"]

COVER_IMG_URL = '/images/sidebar.jpg'

THEME = 'pure'

LINKS = (
    ('AFPY', 'http://www.afpy.org/'),
#    ('Python', 'https://www.python.org/'),
#    ('La Cantine', 'http://cantine.atlantic2.org/'),
)

SOCIAL = (
    ('envelope', 'http://lists.afpy.org/listinfo/salt-fr'),
    ('user', 'http://www.meetup.com/Paris-Salt-Meetup/'),
    ('rss', '/feeds/all.atom.xml'),
#    ('twitter', 'https://twitter.com/SaltParis'),
    ('github', 'https://github.com/afpy/salt-fr'),
)

MENUITEMS = (
    (u'À propos', '/pages/a-propos-de-salt-fr.html'),
    (u'Archives', '/archives.html')
)

STATIC_PATHS = ['images', 'documents', 'extra/CNAME', 'presentations']

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

DEFAULT_PAGINATION = 5

#GOOGLE_ANALYTICS = 'XXX'

#DISQUS_SITENAME = 'xxx'
