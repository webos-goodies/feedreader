# -*- encoding: utf-8; -*-

from dateutil.parser import parse

RSS091_FILES = (
    ('rssnine/pocketgamer.xml', {
        'title': 'Pocket Gamer | www.pocketgamer.co.uk | Latest additions (iPhone)',
        'link': 'http://www.pocketgamer.co.uk/',
        'description': 'The latest stories from Pocket Gamer, updated every five minutes.',
        'entries': (
            {
                'title': u'Review: The House of the Dead: Overkill - The Lost Reels',
                'link': 'http://feedproxy.google.com/~r/PocketGamerLatestAdditionsiphone/~3/-yWMzZdVG6o/review.asp',
                'published': parse('Tue, 30 Apr 2013 18:00:00 GMT'),
                'description': u'img src="http://www.pocketgamer.co.uk/artwork/thumbs/'
            },
            {
                'title': u'Top 10 best one-button games on iPhone',
                'link': 'http://feedproxy.google.com/~r/PocketGamerLatestAdditionsiphone/~3/f7UyIkbDX18/feature.asp',
                'published': parse('Tue, 30 Apr 2013 16:00:00 GMT'),
                'description': u'iPhone gaming appeals to a far broader crowd than the traditional consoles do.'
            },
            {
                'title': u'Space Hulk dev answers questions on multiplayer options, game rules',
                'link': 'http://feedproxy.google.com/~r/PocketGamerLatestAdditionsiphone/~3/_gYd3eB_RPE/video.asp',
                'published': parse('Tue, 30 Apr 2013 15:34:14 GMT'),
                'description': u'img src="http://www.pocketgamer.co.uk/artwork/stock_shots/gen_video_69x69.jpg"'
            },
            {
                'title': u'Review: Idol Words',
                'link': 'http://feedproxy.google.com/~r/PocketGamerLatestAdditionsiphone/~3/3GVmE58m-kU/review.asp',
                'published': parse('Tue, 30 Apr 2013 15:00:00 GMT'),
                'description': u'img src="http://www.pocketgamer.co.uk/artwork/thumbs/'
            }
        )
    }),
    ('rssnine/getnews.xml', {
        'title': u'ガジェット通信',
        'link': 'http://getnews.jp/',
        'description': u'デジタル世代のレビュー＆ニュース＆カルチャーマガジン',
        'entries': (
            {
                'id': 'http://getnews.jp/archives/336896',
                'title': u'長嶋茂雄　"脳梗塞で倒れてから9年でリハビリ休んだのは2回"',
                'link': 'http://getnews.jp/archives/336896',
                'published': parse('Fri, 10 May 2013 01:15:16 +0900'),
                'description': u'今から9年前の2004年3月4日、自宅で倒れた長嶋茂雄さん（77才）。'
            },
            {
                'id': 'http://getnews.jp/archives/336843',
                'title': u'はるかぜちゃんが嘆く「学校名さらし」 子役タレントのプライバシーはどうなる？',
                'link': 'http://getnews.jp/archives/336843',
                'published': parse('Fri, 10 May 2013 00:45:00 +0900'),
                'description': u'「はるかぜちゃん」の愛称で知られるタレントの春名風花さん。'
            }
        )
    }),
    ('rssnine/getnews_relative.xml', {
        'title': u'ガジェット通信',
        'link': 'http://getnews.jp/',
        'description': u'デジタル世代のレビュー＆ニュース＆カルチャーマガジン',
        'entries': (
            {
                'id': 'http://getnews.jp/archives/336896',
                'title': u'長嶋茂雄　脳梗塞で倒れてから9年でリハビリ休んだのは2回',
                'link': 'http://getnews.jp/archives/336896',
                'published': parse('Fri, 10 May 2013 01:15:16 +0900'),
                'description': u'今から9年前の2004年3月4日、自宅で倒れた長嶋茂雄さん（77才）。'
            },
        )
    }),
    ('rssnine/fallback.xml', {
        'title': u'ガジェット通信',
        'link': 'http://getnews.jp/',
        'description': u'デジタル世代のレビュー＆ニュース＆カルチャーマガジン',
        'entries': (
            {
                'id': 'http://getnews.jp/archives/336896',
                'title': u'長嶋茂雄　"脳梗塞で倒れてから9年でリハビリ休んだのは2回"',
                'link': 'http://getnews.jp/archives/336896',
                'published': parse('Fri, 10 May 2013 01:15:16 +0900'),
                'description': u'今から9年前の2004年3月4日、自宅で倒れた長嶋茂雄さん（77才）。'
            },
            {
                'id': 'http://getnews.jp/archives/336843',
                'title': u'はるかぜちゃんが嘆く「学校名さらし」 子役タレントのプライバシーはどうなる？',
                'link': 'http://getnews.jp/archives/336843',
                'published': parse('Fri, 10 May 2013 00:45:00 +0900'),
                'description': u'「はるかぜちゃん」の愛称で知られるタレントの春名風花さん。'
            }
        )
    }),
)
