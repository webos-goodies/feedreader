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
                'title': u'"タイトル"',
                'link': 'http://example.com/articles/01.html',
                'description': u'コンテンツ',
                'published': parse('2006-12-16T15:18:25+09:00'),
                'updated': parse('2006-12-16T06:22:55Z'),
                'author_name': u'hogehoge'
            },
        )
    }),
    ('atom/gentoo.xml', {
        'id': 'http://packages.gentoo.org/feed/',
        'title': 'Gentoo Packages',
        'link': 'http://packages.gentoo.org/',
        'description': None,
        'updated': parse('2014-10-04T12:34:01Z'),
        'entries': (
            {
                'id': 'http://packages.gentoo.org/package/sys-apps/roccat-tools?ts=2014-10-04T12:34:01Z',
                'title': u'sys-apps/roccat-tools-2.2.0: Utility for advanced configuration of Roccat devices & machines',
                'link': 'http://packages.gentoo.org/package/sys-apps/roccat-tools',
                'description': u'<div>*roccat-tools-2.2.0 (04 Oct 2014)<br/>04 Oct 2014; Markos Chandras (<a href="http://cia.vc/stats/author/hwoarang">hwoarang</a>) +<a href="http://sources.gentoo.org/viewcvs.py/gentoo-x86/sys-apps/roccat-tools/roccat-tools-2.2.0.ebuild?view=markup">roccat-tools-2.2.0.ebuild</a>:<br/>Version bump. Bug #<a href="https://bugs.gentoo.org/show_bug.cgi?id=523974">523974</a></div>',
                'published': None,
                'updated': parse('2014-10-04T12:34:01Z'),
                'author_name': u'Markos Chandras (hwoarang)'
            },
            {
                'id': 'http://packages.gentoo.org/package/dev-libs/libgaminggear?ts=2014-10-04T12:32:52Z',
                'title': u'dev-libs/libgaminggear-0.5.0: Provides functionality for gaming input devices',
                'link': 'http://packages.gentoo.org/package/dev-libs/libgaminggear',
                'description': u'<div>*libgaminggear-0.5.0 (04 Oct 2014)<br/>04 Oct 2014; Markos Chandras (<a href="http://cia.vc/stats/author/hwoarang">hwoarang</a>) <br/>+<a href="http://sources.gentoo.org/viewcvs.py/gentoo-x86/dev-libs/libgaminggear/libgaminggear-0.5.0.ebuild?view=markup">libgaminggear-0.5.0.ebuild</a>:<br/>Version bump. Bug #<a href="https://bugs.gentoo.org/show_bug.cgi?id=523976">523976</a></div>',
                'published': None,
                'updated': parse('2014-10-04T12:32:52Z'),
                'author_name': u'Markos Chandras (hwoarang)'
            },
            {
                'id': 'http://packages.gentoo.org/package/x11-misc/imake?ts=2014-10-04T12:31:19Z',
                'title': u'x11-misc/imake-1.0.7: C preprocessor interface to the make utility',
                'link': 'http://packages.gentoo.org/package/x11-misc/imake',
                'description': u'<div>04 Oct 2014; Markus Meier (<a href="http://cia.vc/stats/author/maekke">maekke</a>) <a href="http://sources.gentoo.org/viewcvs.py/gentoo-x86/x11-misc/imake/imake-1.0.7.ebuild?view=markup">imake-1.0.7.ebuild</a>:<br/>arm stable, bug #<a href="https://bugs.gentoo.org/show_bug.cgi?id=499166">499166</a></div>',
                'published': None,
                'updated': parse('2014-10-04T12:31:19Z'),
                'author_name': u'Markus Meier (maekke)'
            },
            {
                'id': 'http://packages.gentoo.org/package/net-wireless/wpa_supplicant?ts=2014-10-04T12:31:15Z',
                'title': u'net-wireless/wpa_supplicant-2.2-r1: IEEE 802.1X/WPA supplicant for secure wireless transfers',
                'link': 'http://packages.gentoo.org/package/net-wireless/wpa_supplicant',
                'description': u'<div>04 Oct 2014; Markus Meier (<a href="http://cia.vc/stats/author/maekke">maekke</a>) <a href="http://sources.gentoo.org/viewcvs.py/gentoo-x86/net-wireless/wpa_supplicant/wpa_supplicant-2.2-r1.ebuild?view=markup">wpa_supplicant-2.2-r1.ebuild</a>:<br/>arm stable, bug #<a href="https://bugs.gentoo.org/show_bug.cgi?id=522852">522852</a></div>',
                'published': None,
                'updated': parse('2014-10-04T12:31:15Z'),
                'author_name': u'Markus Meier (maekke)'
            },
        )
    }),
    ('atom/aws_j.xml', {
        'id': 'tag:typepad.com,2003:weblog-86842883779368716',
        'title': u'Amazon Web Services ブログ',
        'link': 'http://aws.typepad.com/aws_japan/',
        'description': u'開発者、ITプロフェッショナル向けにAmazon Web Services(AWS)が提供するアマゾンクラウド(Amazon EC2, S3, RDS, EMR他)の公式ブログです。最新情報をエバンジェリストが伝えます [AWSブログ]',
        'updated': parse('2014-10-02T00:19:48Z'),
        'entries': (
            {
                'id': 'tag:typepad.com,2003:post-6a00d8341c534853ef01b7c6eb6d3b970b',
                'title': u'EC2<メンテナンスについての続報>',
                'link': 'http://aws.typepad.com/aws_japan/2014/10/ec2ment-update.html',
                'description': u'<div xmlns="http://www.w3.org/1999/xhtml"><p>本日は先週末(2014/9/27から)に実施した、再起動を伴う</p></div>',
                'published': parse('2014-10-01T17:15:23-07:00'),
                'updated': parse('2014-10-02T00:19:48Z'),
                'author_name': u'AWS Evangelist'
            },
            {
                'id': 'tag:typepad.com,2003:post-6a00d8341c534853ef01b8d074aed3970c',
                'title': u'Amazon AppStreamが東京リージョンで利用可能に',
                'link': 'http://aws.typepad.com/aws_japan/2014/09/appstream-tokyo.html',
                'description': u'<div xmlns="http://www.w3.org/1999/xhtml"><p>Amazon AppStreamは、クラウドベースのグラフィックレンダリング（2Dも3Dも）を利用しており、ローカルの計算能力やストレージを削減することができることで、複雑なアプリケーションをシンプルなデバイスで実行することができます。</p></div>',
                'published': parse('2014-09-30T22:25:17-07:00'),
                'updated': parse('2014-10-01T01:32:16Z'),
                'author_name': u'AWS Evangelist'
            },
            {
                'id': 'tag:typepad.com,2003:post-6a00d8341c534853ef01bb078cece7970d',
                'title': u'EC2メンテナンスアップデートに関して',
                'link': 'http://aws.typepad.com/aws_japan/2014/09/ec2mente.html',
                'description': u'<div xmlns="http://www.w3.org/1999/xhtml"><p>今週末から来週頭において実施されるEC2メンテナンスに関して、複数のお客様からご質問を頂きましたので、こちらのブログでもお知らせさせて頂きたいと思います。</p></div>',
                'published': parse('2014-09-25T18:16:55-07:00'),
                'updated': parse('2014-09-26T01:17:39Z'),
                'author_name': u'AWS Evangelist'
            },
            {
                'id': 'tag:typepad.com,2003:post-6a00d8341c534853ef01a73e147e7e970d',
                'title': u'【AWS発表】ElastiCacheでもT2インスタンスタイプを利用可能に',
                'link': 'http://aws.typepad.com/aws_japan/2014/09/elasticache-t2-support.html',
                'description': u'<div xmlns="http://www.w3.org/1999/xhtml"><p>すでにご存知化と思いますが、<a href="https://aws.amazon.com/ec2/">Amazon Elastic Compute Cloud</a> (EC2)の新しい<strong>T2</strong>インスタンスタイプは、しっかりしたベースライン性能と、必要に応じて、ベースラインを超えてバーストする能力を提供します。 <a href="http://aws.typepad.com/aws_japan/2014/07/low-cost-burstable-ec2-instances.html">以前にブログ記事に書いた</a>ように、このインスタンスタイプは開発、テスト、中規模トラフィックのWebサイトに最適です。</p></div>',
                'published': parse('2014-09-12T01:26:50-07:00'),
                'updated': parse('2014-09-12T08:26:50Z'),
                'author_name': u'AWS Evangelist'
            },
        )
    }),
    ('atom/devopera.xml', {
        'id': 'https://dev.opera.com/',
        'title': 'Dev.Opera',
        'link': 'https://dev.opera.com/',
        'description': None,
        'updated': parse('2014-09-29T15:26:19+02:00'),
        'entries': (
            {
                'id': 'https://dev.opera.com/articles/better-font-face/',
                'title': u'Better @font-face with Font Load Events',
                'link': 'https://dev.opera.com/articles/better-font-face/',
                'description': u'<p><code>@font-face</code> is an established staple in the diet of almost half of the web. According to the HTTP Archive, 47% of web sites make a request for at least one custom web font.',
                'published': parse('2014-09-26T00:00:00+02:00'),
                'updated': parse('2014-09-26T00:00:00+02:00'),
                'author_name': u'Zach Leatherman'
            },
        )
    }),
    ('atom/derorinkuma.xml', {
        'id': 'http://derorinkuma.com/feed/atom',
        'title': u'サッカーコラム速報でろブロ',
        'link': 'http://derorinkuma.com',
        'description': u'でろりんクマとかサッカー好きがネットのニュースや試合を見てグダグダサッカーについて語っています。',
        'updated': parse('2015-02-08T05:43:33Z'),
        'entries': (
            {
                'id': 'http://derorinkuma.com/?p=65438',
                'title': u'鈴木隆行選手がジェフユナイテッド市原・千葉に移籍…気が付いたらもう38歳',
                'link': 'http://derorinkuma.com/65438',
                'description': u'元日本代表FWで水戸ホーリーホックに所属していた鈴木隆行選手がジェフユナイテッド市原・千葉に加入する事が正式に決まったようです。公式サイトが伝えています。 Source:http://jefunited.co.jp/ne…',
                'published': parse('2015-02-08T05:43:33Z'),
                'updated': parse('2015-02-08T05:43:33Z'),
                'author_name': u'でろりん'
            },
            {
                'id': 'http://derorinkuma.com/?p=65434',
                'title': u'セリエA第22節 ユヴェントス 3-1 ミラン 本田圭佑はトップ下でフル出場もインパクト残せず完敗',
                'link': 'http://derorinkuma.com/65434',
                'description': u'セリエA第22節 1位ユヴェントスvs8位ACミラン 試合の感想です。 出場選手 Away： ACミラン GK 23 ディエゴ・ロペス DF 29 ガブリエル・パレッタ DF 31 ルカ・アントネッリ DF 33 アレッ…',
                'published': parse('2015-02-07T21:57:31Z'),
                'updated': parse('2015-02-07T21:57:31Z'),
                'author_name': u'でろりん'
            },
            {
                'id': 'http://derorinkuma.com/?p=65430',
                'title': u'ブンデス第20節 フライブルク 0-3 ドルトムント　香川真司はフル出場1アシスト',
                'link': 'http://derorinkuma.com/65430',
                'description': u'ブンデスリーガ第20節 15位SCフライブルクvs18位（最下位）ボルシア・ドルトムント 試合の感想です。 出場選手 Away： ボルシア・ドルトムント GK 1 ロマン・ヴァイデンフェラー DF 4 ネヴェン・スボティ…',
                'published': parse('2015-02-07T16:24:23Z'),
                'updated': parse('2015-02-07T16:24:23Z'),
                'author_name': u'でろりん'
            },
            {
                'id': 'http://derorinkuma.com/?p=65428',
                'title': u'サッカー協会が日本代表の新監督候補に5人程度の外国人をリストアップ',
                'link': 'http://derorinkuma.com/65428',
                'description': u'日本サッカー協会が日本代表の新監督の候補について、5人程度の外国人をリストアップしている事を明らかにしているようです。なんとNHKが報じています。 Source:http://www3.nhk.or.jp/news/ht…',
                'published': parse('2015-02-06T09:01:12Z'),
                'updated': parse('2015-02-06T09:01:12Z'),
                'author_name': u'でろりん'
            },
        )
    }),
    ('atom/fallback.xml', {
        'id': 'tag:example.com,2006:hogehoge',
        'title': u'Broken atom sample',
        'link': 'http://atom03.example.com/',
        'description': u'A sample of Atom 0.3 feed.',
        'updated': parse('2013-04-06T05:45:46Z'),
        'entries': (
            {
                'id': 'tag:example.com,2006:hogehoge.50450919',
                'title': u'"タイトル"',
                'link': 'http://example.com/articles/01.html',
                'description': u'コンテンツ',
                'published': parse('2006-12-16T15:18:25+09:00'),
                'updated': parse('2006-12-16T06:22:55Z'),
                'author_name': u'hogehoge'
            },
        )
    }),
)
