# -*- encoding: utf-8; -*-

from dateutil.parser import parse

ATOM_FILES = (
    ('atom/blogger.xml', {
        'title': 'The Official Google Blog',
        'link': 'http://googleblog.blogspot.com/',
        'description': 'Insights from Googlers into our products, technology, and the Google culture.',
        'entries': (
            {
                'id': 'tag:blogger.com,1999:blog-10861780.post-6894556562483778659',
                'title': 'Imagery on Google Maps of Fukushima Exclusion Zone Town Namie-machi',
                'link': 'http://feedproxy.google.com/~r/blogspot/MKuf/~3/k84LwkiTyXg/imagery-on-google-maps-of-fukushima.html',
                'description': '<i>From time to time we invite guests',
                'published': parse('2013-03-27T13:36:00.000-07:00'),
                'updated': parse('2013-03-27T13:36:11.380-07:00'),
                'author_name': 'Emily Wood',
                'author_link': 'https://plus.google.com/112374322230920073195',
                'author_email': 'noreply@blogger.com'
            },
            {
                'id': 'tag:blogger.com,1999:blog-10861780.post-558015491657123778',
                'title': 'Enabling the next generation of computer scientists with CS4HS',
                'link': 'http://feedproxy.google.com/~r/blogspot/MKuf/~3/bxAcy49FEAw/enabling-next-generation-of-computer.html',
                'description': 'For the past four years, Google has sponsored an initiative called',
                'published': parse('2013-03-27T09:43:00.000-07:00'),
                'updated': parse('2013-03-27T09:43:31.988-07:00'),
                'author_name': 'Emily Wood',
                'author_link': 'https://plus.google.com/112374322230920073195',
                'author_email': 'noreply@blogger.com',
            },
            {
                'id': 'tag:blogger.com,1999:blog-10861780.post-6076208562672557756',
                'title': u'Global Impact Awards’ hunt for U.K.’s most innovative social entrepreneurs starts today',
                'link': 'http://feedproxy.google.com/~r/blogspot/MKuf/~3/BwXM-OPPgQI/global-impact-awards-hunt-for-uks-most_24.html',
                'description': 'From <a href="http://www.sanger.ac.uk/about/history/hgp/',
                'published': parse('2013-03-24T17:00:00.000-07:00'),
                'updated': parse('2013-03-24T17:11:46.423-07:00'),
                'author_name': 'Emily Wood',
                'author_link': 'https://plus.google.com/112374322230920073195',
                'author_email': 'noreply@blogger.com',
            },
            {
                'id': 'tag:blogger.com,1999:blog-10861780.post-7509484451492057383',
                'title': 'Urban art, zoomorphic whistles and Hungarian poetry',
                'link': 'http://feedproxy.google.com/~r/blogspot/MKuf/~3/TIn_bnRX9lk/urban-art-zoomorphic-whistles-and.html',
                'description': 'There are few places (if any) in the world where you could',
                'published': parse('2013-03-21T01:01:00.000-07:00'),
                'updated': parse('2013-03-21T01:01:19.776-07:00'),
                'author_name': 'Emily Wood',
                'author_link': 'https://plus.google.com/112374322230920073195',
                'author_email': 'noreply@blogger.com',
            }
        )
    }),

    ('atom/pyxis.xml', {
        'id': 'tag:blog.lan2.jp,2011:/entre//4',
        'title': u'起業家応援ブログ by 株式会社ピクシス',
        'link': 'http://blog.lan2.jp/entre/',
        'description': u'企業経営者の皆様方へ、経理、会社法、税法、総務業務などの経営に必要な情報をタイムリーに提供することにより、事業成長を支援するサイバーコンサルタントとして活動していきます。',
        'updated': parse('2011-01-27T11:47:31Z'),
        'entries': (
            {
                'id': 'tag:blog.lan2.jp,2011:/entre//4.158',
                'title': u'平成23年度(2011年度)税制改正-所得税編-',
                'link': 'http://blog.lan2.jp/entre/2011/01/232011_1.html',
                'description': u'2010年12月16日、「平成23年度（2011年度）税制改正大綱」が閣議決定されました。',
                'published': parse('2011-01-27T11:47:31Z'),
                'updated': parse('2011-01-27T11:47:31Z'),
                'author_name': u'株式会社 ピクシス',
                'author_uri': 'http://www.lan2.jp/'
            },
            {
                'id': 'tag:blog.lan2.jp,2011:/entre//4.157',
                'title': u'平成23年度(2011年度)税制改正-法人税編-',
                'link': 'http://blog.lan2.jp/entre/2011/01/232011.html',
                'published': parse('2011-01-20T10:36:58Z'),
                'updated': parse('2011-01-27T11:08:49Z'),
                'author_name': u'株式会社 ピクシス',
                'author_link': 'http://www.lan2.jp/',
                'description': u'2010年12月16日、「平成23年度（2011年度）税制改正大綱」が閣議決定されました。'
            },
            {
                'title': u'タックスへイブン対策税制の概要',
                'link': 'http://blog.lan2.jp/entre/2010/08/post_68.html',
                'id': 'tag:blog.lan2.jp,2010:/entre//4.156',
                'published': parse('2010-08-17T11:11:20Z'),
                'updated': parse('2010-08-17T11:11:20Z'),
                'author_name': u'株式会社 ピクシス',
                'author_link': 'http://www.lan2.jp/',
                'description': u'タックスへイブン（軽課税国）である源泉地国で得た所得は、',
            },
            {
                'title': u'租税特別措置透明化法の概要',
                'link': 'http://blog.lan2.jp/entre/2010/06/post_67.html',
                'id': 'tag:blog.lan2.jp,2010:/entre//4.155',
                'published': parse('2010-06-29T11:00:35Z'),
                'updated': parse('2010-06-29T11:00:35Z'),
                'author_name': u'株式会社 ピクシス',
                'author_link': 'http://www.lan2.jp/',
                'description': u'去る3月24日、「所得税法等の一部を改正する法律」と共に、'
            }
        )
    })
)
