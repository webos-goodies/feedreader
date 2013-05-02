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
)
