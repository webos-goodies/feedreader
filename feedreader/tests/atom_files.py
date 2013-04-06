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
    }),
    ('atom/gihyo.xml', {
        'id': 'http://gihyo.jp/dev',
        'title': u'gihyo.jp：DEVELOPER STAGE',
        'link': 'http://gihyo.jp/dev',
        'description': u'gihyo.jp（DEVELOPER STAGE）の更新情報をお届けします',
        'updated': parse('2013-04-06T10:52:00+09:00'),
        'entries': (
            {
                'id': 'http://gihyo.jp/dev/serial/01/meteor/0012',
                'title': u'第12回　［最終回］Meteorが指し示すWebアプリ開発の未来 ── 体感！JavaScriptで超速アプリケーション開発 －Meteor完全解説',
                'link': 'http://rss.rssad.jp/rss/artclk/6kFPmDSBc8CI/5117feb031ce10175e22718e9125ba10?ul=qFLnlCCiJCv.k11G1fG.YKSSaQnenmAUw7YiCwq7IRtXwUWObJzF59R8m5.HCUrt9arCw5T',
                'description': u'<p>さて，これまで10回以上に渡って続けさせていただいたこの',
                'published': parse('2013-04-05T18:02:00+09:00'),
                'updated': parse('2013-04-05T18:02:00+09:00'),
                'author_name': u'白石俊平'
            },
            {
                'id': 'http://gihyo.jp/dev/serial/01/realtimeweb/0006',
                'title': u'第6回　node.js，SignalRとクラウド，まとめ ── リアルタイムWebを極める',
                'link': 'http://rss.rssad.jp/rss/artclk/6kFPmDSBc8CI/c0df4e6311e69382b68c992ca7b09c6f?ul=lTVXR6hb6XP1vijiBl9iZMuSXiVGnMeroLM1v5lydTGG5OBxgOT1tUcaE9AzYJ5PUX_BSB9',
                'description': u'最終回となる今回は，node.jsとSignalRのそれぞれを実際に',
                'published': parse('2013-04-05T11:00:00+09:00'),
                'updated': parse('2013-04-05T11:00:00+09:00'),
                'author_name': u'芝村達郎'
            },
            {
                'id': 'http://gihyo.jp/dev/serial/01/mahout/0003',
                'title': u'第3回　Mahoutの環境構築とFP-Growthによるマーケットバスケット分析 ── Mahoutで体感する機械学習の実践',
                'link': 'http://rss.rssad.jp/rss/artclk/6kFPmDSBc8CI/2d032d5244a41f534cf7a4b65bb9e869?ul=IQ_0lyTW5R7OJbdLTanC44B79QNnSaRtLiNJuEOIdCSs3mxXy0fEeBOAh0mHB_U_N40jk8Q',
                'description': u'今回は，実践編として，Mahoutが実装しているアプリオリアルゴリズム',
                'published': parse('2013-04-04T10:54:00+09:00'),
                'updated': parse('2013-04-04T10:54:00+09:00'),
                'author_name': u'やまかつ'
            },
            {
                'id': 'http://gihyo.jp/dev/clip/01/groonga/0001',
                'title': u'第1回　全文検索エンジンgroongaを紹介します！ ── 隔週連載groonga',
                'link': 'http://rss.rssad.jp/rss/artclk/6kFPmDSBc8CI/d4a4314f2a518694bf8214ad2d20a142?ul=wNwWJqZuGH9ZSoOlD8KRty7Gn5nQqbfNY1Hp.Ny2nGHaBwxLY._5OvYwjp925JRk0vH6zBO',
                'description': u'<p>今回から始まった隔週連載groongaでは，groongaを使いたくなるような',
                'published': parse('2013-04-02T10:54:00+09:00'),
                'updated': parse('2013-04-02T10:54:00+09:00'),
                'author_name': u'Haruka Yoshihara'
            }
        )
    }),
    ('atom/atom03.xml', {
        'id': 'tag:example.com,2006:hogehoge',
        'title': u'Atom 0.3 sample',
        'link': 'http://atom03.example.com/',
        'description': u'A sample of Atom 0.3 feed.',
        'updated': parse('2013-04-06T05:45:46Z'),
        'entries': (
            {
                'id': 'tag:example.com,2006:hogehoge.50450919',
                'title': u'タイトル',
                'link': 'http://example.com/articles/01.html',
                'description': u'コンテンツ',
                'published': parse('2006-12-16T15:18:25+09:00'),
                'updated': parse('2006-12-16T06:22:55Z'),
                'author_name': u'hogehoge'
            },
        )
    }),
)
