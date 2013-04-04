# -*- encoding: utf-8; -*-

from dateutil.parser import parse

RSS10_FILES = (
    ('rssone/hatebu.xml', {
        'id': 'http://b.hatena.ne.jp/hotentry',
        'title': u'はてなブックマーク - 人気エントリー',
        'link': 'http://b.hatena.ne.jp/hotentry',
        'description': u'最近の人気エントリー',
        'entries': (
            {
                'id': 'http://bazubu.com/seo-13666.html',
                'title': u'SEO対策｜検索順位の上位を独占するために私が行っている36の手順',
                'link': 'http://bazubu.com/seo-13666.html',
                'published': parse('2013-04-03T17:01:42+09:00'),
                'description': u'<blockquote cite="http://bazubu.com/seo-13666.html" title='
            },
            {
                'id': 'http://togech.jp/2013/04/03/741',
                'title': u'人気Twitter女子に聞く！　モテツイートの鉄則 - トゥギャッチ',
                'link': 'http://togech.jp/2013/04/03/741',
                'published': parse('2013-04-03T17:04:48+09:00'),
                'description': u'<blockquote cite="http://togech.jp/2013/04/03/741" title="'
            },
            {
                'id': 'http://headlines.yahoo.co.jp/hl?a=20130403-00000133-jij-pol',
                'title': u'国内クリエーター結集を＝クールジャパン推進で―政府 （時事通信） - Yahoo!ニュース',
                'link': 'http://headlines.yahoo.co.jp/hl?a=20130403-00000133-jij-pol',
                'published': parse('2013-04-03T20:39:31+09:00'),
                'description': u'<blockquote cite="http://headlines.yahoo.co.jp/hl?a=201304'
            },
            {
                'id': 'http://www.atmarkit.co.jp/ait/articles/1304/03/news011.html',
                'title': u'グリーはいかにしてJenkinsを導入したのか（2）：JenkinsでCIすればiOSアプリのビルドは、もう面倒くさくない (1/2) - ＠IT',
                'link': 'http://www.atmarkit.co.jp/ait/articles/1304/03/news011.html',
                'published': parse('2013-04-03T18:41:12+09:00'),
                'description': u'<blockquote cite="http://www.atmarkit.co.jp/ait/articles/1'
            },
        )
    }),
)
