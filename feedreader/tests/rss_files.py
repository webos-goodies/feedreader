# -*- encoding: utf-8; -*-

from dateutil.parser import parse

RSS_FILES = (
    ('rss/reddit.xml', {
        'title': 'reddit.com: what\'s new online!',
        'link': 'http://www.reddit.com/',
        'description': '',
        'entries': (
            {
                'id': 'http://www.reddit.com/r/science/comments/86yb2/the_answer_to_the_energy_crisis_is_donuts_solar/',
                'title': 'the answer to the energy crisis is donuts [solar cells from donuts]',
                'link': 'http://www.reddit.com/r/science/comments/86yb2/the_answer_to_the_energy_crisis_is_donuts_solar/',
                'published': parse('Mon, 23 Mar 2009 18:47:28 -0700')
            },
            {
                'id': 'http://www.reddit.com/r/reddit.com/comments/86297/do_no_evil_my_ass_google_is_now_supporting_domain/',
                'title': 'Do no evil my ass, google is now supporting domain squatters',
                'link': 'http://www.reddit.com/r/reddit.com/comments/86297/do_no_evil_my_ass_google_is_now_supporting_domain/',
                'published': parse('Thu, 19 Mar 2009 19:15:53 -0700')
            },
            {
                'id': 'http://www.reddit.com/r/pics/comments/7m2sa/the_best_10_the_best_of_2008_of_2008/',
                'title': u'The Best 10 \u201cThe Best \u2026 of 2008\u2033 of 2008',
                'link': 'http://www.reddit.com/r/pics/comments/7m2sa/the_best_10_the_best_of_2008_of_2008/',
                'published': parse('Sun, 28 Dec 2008 10:38:19 -0700')
            }
        )
    }),
    ('rss/digg.xml', {
        'title': 'digg / kevinrose / history',
        'link': 'http://digg.com/users/kevinrose/history',
        'description': 'A history of kevinrose\'s activity at digg.com',
        'entries': (
            {
                'id': 'http://digg.com/food_drink/Tea_Measurements_What_is_the_best_way_to_measure_loose_tea',
                'title': 'Tea Measurements: What is the best way to measure loose tea?',
                'link': 'http://digg.com/food_drink/Tea_Measurements_What_is_the_best_way_to_measure_loose_tea',
                'author_name': 'kevinrose',
                'published': parse('Sat, 25 Jul 2009 04:34:22 UTC')
            },
            # Digg has some screwy feeds with empty items
            {
                'id': 'http://digg.com/users/kevinrose/friends/view',
                'title': '',
                'link': 'http://digg.com/users/kevinrose/friends/view',
                'published': parse('Fri, 24 Jul 2009 16:53:30 UTC')
            },
            {
                'id': 'http://digg.com/users/kevinrose/friends/view',
                'title': '',
                'link': 'http://digg.com/users/kevinrose/friends/view',
                'published': parse('Fri, 24 Jul 2009 09:15:28 UTC')
            },
            {
                'id': 'http://digg.com/users/kevinrose/friends/view',
                'title': '',
                'link': 'http://digg.com/users/kevinrose/friends/view',
                'published': parse('Fri, 24 Jul 2009 07:50:24 UTC')
            },
            {
                'id': 'http://digg.com/gadgets/Palm_webOS_1_1_now_available_fixes_iTunes_8_2_1_syncing',
                'title': 'Palm webOS 1.1 now available, fixes iTunes 8.2.1 syncing',
                'link': 'http://digg.com/gadgets/Palm_webOS_1_1_now_available_fixes_iTunes_8_2_1_syncing',
                'description': 'Time to update your Pre, as Palm has released webOS 1.1.0. Quite a bit of changes here, and most importantly, the patch notes say that it "Resolves an issue preventing media sync from working with latest version of iTunes (8.2.1)."',
                'author': 'kevinrose',
                'published': parse('Fri, 24 Jul 2009 02:45:36 UTC')
            },
        )
    }),
    ('rss/deviantart.xml', {
        'title': 'Sooper-Deviant\'s Gallery',
        'link': 'http://browse.deviantart.com/?order=5&q=gallery%3ASooper-Deviant',
        'description': 'deviantART RSS for  sort:time gallery:Sooper-Deviant',
        'entries': (
            {
                'id': 'http://Sooper-Deviant.deviantart.com/art/Small-Universe-9848-130937420',
                'title': 'Small Universe 9848',
                'link': 'http://Sooper-Deviant.deviantart.com/art/Small-Universe-9848-130937420',
                'published': parse('Sun, 26 Jul 2009 06:13:31 PDT'),
                'enclosures': (
                    {
                        'href': 'http://th04.deviantart.net/fs48/300W/f/2009/207/d/7/d7400f45d945d29fa1edba98531bc887.jpg',
                        'media': 'thumbnail',
                    },
                ),
            },
        )
    }),
    ('rss/engadget_jp.xml', {
        'title': 'Engadget Japanese',
        'link': 'http://japanese.engadget.com',
        'description': 'Engadget Japanese',
        'entries': (
            {
                'title': u'デル S2240T発売、10点タッチ対応の21.5型フルHD液晶モニタ',
                'link': 'http://japanese.engadget.com/2013/05/01/st2240t-10-21-5-hd/',
                'id': 'http://japanese.engadget.com/2013/05/01/st2240t-10-21-5-hd/',
                'description': u'デルがマルチタッチ対応液晶モニタの新製品 S2240T を国内向けに発売しました。',
                'author_name': 'Ittousai',
                'published': None
            },
            {
                'title': u'Androidのバージョン別シェア更新、Jelly Bean(4.1+) が ICS (4.0)を追い越す。計55.9%',
                'link': 'http://japanese.engadget.com/2013/05/01/android-jelly-bean-4-1-ics-4-0-55-9/',
                'id': 'http://japanese.engadget.com/2013/05/01/android-jelly-bean-4-1-ics-4-0-55-9/',
                'description': u'月に一度のお楽しみ、でもありませんが、Google が Android開発者ダッシュボードの',
                'author_name': 'Ittousai',
                'published': None
            },
            {
                'title': u'PR: 【三井の賃貸】最新値下げ物件が集結！賃料改定物件特集',
                'link': 'http://rss.rssad.jp/rss/ad/Du1eQMczaHjX/jPjwBLIVhnwY?type=2&ent=9995d519158078b05d269016b3e82d53',
                'id': None,
                'description': u'<table cellspacing="0" cellpadding="0"><tbody>',
                'author_name': None,
                'published': None
            },
            {
                'title': u'iOS / Androidの公式Twitter アプリ更新、トレンドの地域選択や仕様変更',
                'link': 'http://japanese.engadget.com/2013/05/01/ios-android-twitter/',
                'id': 'http://japanese.engadget.com/2013/05/01/ios-android-twitter/',
                'description': u'Twitter が iOS と Android版の公式 Twitter アプリを更新しました。',
                'author_name': 'Ittousai',
                'published': None
            },
        )
    }),
    ('rss/googlegroups.xml', {
        'title': 'Google Groups',
        'link': 'http://groups.google.com/group/foobar',
        'description': u'いわゆる掲示板',
        'entries': (
            {
                'title': u'おひさしぶりです。',
                'link': 'http://groups.google.com/group/foobar/browse_thread/thread/xxx?hl=ja&show_docid=xxxx',
                'id': 'http://groups.google.com/group/foobar/browse_thread/thread/xxx?hl=ja&show_docid=xxxx',
                'description': u'先生、皆様、お元気でしょうか？ <br> <p>談話室が、',
                'author_name': u"jun.cello1...@gmail.com (かみや)",
                'published': None
            },
            {
                'title': u'おひさしぶりです。',
                'link': 'http://groups.google.com/group/foobar/browse_thread/thread/aaa?hl=ja&show_docid=aaa',
                'id': 'http://groups.google.com/group/foobar/browse_thread/thread/aaa?hl=ja&show_docid=aaa',
                'description': u"先生、皆様、お元気でしょうか？\n&lt;br&gt; &lt;p&gt;談話室が、",
                'author_name': u"jun.cello1...@gmail.com (かみや)",
                'published': None
            },
        )
    }),
    ('rss/parttimepoker.xml', {
        'title': 'Part Time Poker',
        'link': 'http://www.parttimepoker.com',
        'description': u'Poker strategy, news, jokes, interviews and reviews',
        'entries': (
            {
                'title': u'HNR 6/17: WSOP Updates, Golden Sit and Go’s at PokerStars',
                'link': 'http://www.parttimepoker.com/hnr-617-wsop-updates-golden-sit-and-gos-at-pokerstars',
                'id': 'http://www.parttimepoker.com/?p=10767',
                'description': u'<p><img src="http://www.parttimepoker.com/wp-',
                'author_name': u"Michael Jones",
                'published': parse('Mon, 17 Jun 2013 19:16:51 +0000')
            },
            {
                'title': u'PokerStars Giving Away $1M in Golden Sit and Go’s',
                'link': 'http://www.parttimepoker.com/pokerstars-giving-away-1m-in-golden-sit-and-gos',
                'id': 'http://www.parttimepoker.com/?p=10768',
                'description': u'<p><img src="http://www.parttimepoker.com/wp-content/',
                'author_name': u"Michael Jones",
                'published': parse('Mon, 17 Jun 2013 19:12:21 +0000')
            },
            {
                'title': u'WSOP Update 6/17: Senior Champ Crowned; Cloutier in Running for No. 7',
                'link': 'http://www.parttimepoker.com/wsop-update-617-senior-champ-crowned-cloutier-in-running-for-no-7',
                'id': 'http://www.parttimepoker.com/?p=10764',
                'description': u'<p><img src="http://www.parttimepoker.com/wp-content/',
                'author_name': u"Michael Jones",
                'published': parse('Mon, 17 Jun 2013 11:25:46 +0000')
            },
        )
    }),
    ('rss/podcast1242.xml', {
        'title': u'ザ・ボイス　そこまで言うか！',
        'link': 'http://podcast.1242.com',
        'description': u'毎日、日替わりでコメンテーターの方々と共に、',
        'entries': (
            {
                'title': u'2014/07/30 長谷川幸洋 ニッポン放送 ザ・ボイス ニュースピックアップセブン',
                'link': 'http://podcast.1242.com/sound/5926.mp3',
                'id': 'http://podcast.1242.com/sound/5926.mp3',
                'description': u'<feedeen>\n<enclosure url="http://podcast.1242.com/sound/5926.mp3" type="audio/mpeg"></enclosure>\n</feedeen>\n2014/07/30 長谷川幸洋 ニッポン放送 ザ・ボイス ニュースピックアップセブン',
                'author_name': None,
                'published': parse('Wed, 30 Jul 2014 18:00:00 +0900')
            },
            {
                'title': u'2014/07/29 宮崎哲弥 ニッポン放送 ザ・ボイス ニュースピックアップセブン',
                'link': 'http://podcast.1242.com/sound/5919.mp3',
                'id': 'http://podcast.1242.com/sound/5919.mp3',
                'description': u'<feedeen>\n<enclosure url="http://podcast.1242.com/sound/5919.mp3" type="audio/mpeg"></enclosure>\n</feedeen>\n2014/07/29 宮崎哲弥 ニッポン放送 ザ・ボイス ニュースピックアップセブン',
                'author_name': None,
                'published': parse('Tue, 29 Jul 2014 17:00:00 +0900')
            },
            {
                'title': u'2014/07/28 勝谷誠彦 ニッポン放送 ザ・ボイス ニュースピックアップセブン',
                'link': 'http://podcast.1242.com/sound/5914.mp3',
                'id': 'http://podcast.1242.com/sound/5914.mp3',
                'description': u'<feedeen>\n<enclosure url="http://podcast.1242.com/sound/5914.mp3" type="audio/mpeg"></enclosure>\n</feedeen>\n2014/07/28 勝谷誠彦 ニッポン放送 ザ・ボイス ニュースピックアップセブン',
                'author_name': None,
                'published': parse('Mon, 28 Jul 2014 18:00:00 +0900')
            },
        )
    }),
    ('rss/nhk_podcast.xml', {
        'title': u'ラジオあさいちばん「ビジネス展望」',
        'link': 'http://www.nhk.or.jp/r-asa/',
        'description': u'専門家が経済問題を深く切り込みます。',
        'entries': (
            {
                'title': u'14年07月28日「完全雇用を考える」同志社大学大学院教授 浜 矩子さん',
                'link': 'http://www.nhk.or.jp/r-asa/podcast/bmp308/140728.mp3',
                'description': u'<feedeen>\n<enclosure url="http://www.nhk.or.jp/r-asa/podcast/bmp308/140728.mp3" type="audio/mpeg"></enclosure>\n</feedeen>\n「完全雇用を考える」同志社大学大学院教授 浜 矩子さん',
                'author_name': None,
                'published': parse('Sat, 2 august 2014 00:00:00 +0900')
            },
            {
                'title': u'14年07月29日「人口減少と地方中枢拠点都市構想」京都大学大学院経済学研究科教授 諸富 徹さん',
                'link': 'http://www.nhk.or.jp/r-asa/podcast/bmp308/140729.mp3',
                'description': u'<feedeen>\n<enclosure url="http://www.nhk.or.jp/r-asa/podcast/bmp308/140729.mp3" type="audio/mpeg"></enclosure>\n</feedeen>\n「人口減少と地方中枢拠点都市構想」京都大学大学院経済学研究科教授 諸富 徹さん',
                'author_name': None,
                'published': parse('Sat, 2 august 2014 00:00:00 +0900')
            },
            {
                'title': u'14年07月30日「地方創生はできるのか」慶応義塾大学教授 金子 勝さん',
                'link': 'http://www.nhk.or.jp/r-asa/podcast/bmp308/140730.mp3',
                'description': u'<feedeen>\n<enclosure url="http://www.nhk.or.jp/r-asa/podcast/bmp308/140730.mp3" type="audio/mpeg"></enclosure>\n</feedeen>\n「地方創生はできるのか」慶応義塾大学教授 金子 勝さん',
                'author_name': None,
                'published': parse('Sat, 2 august 2014 00:00:00 +0900')
            },
        )
    }),
    ('rss/radionikkei.xml', {
        'title': u'伊藤洋一のRound Up World Now!',
        'link': 'http://www.radionikkei.jp/roundup/',
        'description': u'伊藤洋一氏が日本だけでなく世界中で起きた1週間の経済・社会・政治関連の出来事',
        'entries': (
            {
                'title': u'Round Up World Now!（2014.8.1放送分）',
                'link': 'http://podcasting.radionikkei.jp/podcasting/roundup/roundup-140801.mp3',
                'description': u'<feedeen>\n<enclosure url="http://podcasting.radionikkei.jp/podcasting/roundup/roundup-140801.mp3" type="audio/mpeg"></enclosure>\n</feedeen>\n安倍内閣支持率、初の50%割れ　日経・テ東世論調査／Amazon、PBブランド商品専用ストア開設　成城石井など15社参加／中国共産党「周永康・前党政治局常務委員を重大な規律違反の疑いで調査」',
                'author_name': None,
                'published': parse('Fri, 01 Aug 2014 22:59:00 +0900')
            },
            {
                'title': u'Round Up World Now!（2014.7.25放送分）',
                'link': 'http://podcasting.radionikkei.jp/podcasting/roundup/roundup-140725.mp3',
                'description': u'<feedeen>\n<enclosure url="http://podcasting.radionikkei.jp/podcasting/roundup/roundup-140725.mp3" type="audio/mpeg"></enclosure>\n</feedeen>\n上半期の不動産取引、2兆5000億円　金融危機後の最高／マレーシア機撃墜でEU内に対ロ強硬論',
                'author_name': None,
                'published': parse('Fri, 25 Jul 2014 22:59:00 +0900')
            },
            {
                'title': u'Round Up World Now!（2014.7.18放送分）',
                'link': 'http://podcasting.radionikkei.jp/podcasting/roundup/roundup-140718.mp3',
                'description': u'<feedeen>\n<enclosure url="http://podcasting.radionikkei.jp/podcasting/roundup/roundup-140718.mp3" type="audio/mpeg"></enclosure>\n</feedeen>\n携帯電話会社にSIMロック解除義務づけ　総務省の商習慣見直し案／JR東日本、2020年代半ばに都心・羽田結ぶ新線',
                'author_name': None,
                'published': parse('Fri, 18 Jul 2014 22:59:00 +0900')
            },
        )
    }),
)
