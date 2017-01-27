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
                'title': u'<SEO対策> 検索順位の上位を独占するために私が行っている36の手順',
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
    ('rssone/mycom.xml', {
        'id': 'http://news.mynavi.jp/enterprise/',
        'title': u'マイナビニュース エンタープライズ',
        'link': 'http://news.mynavi.jp/enterprise/',
        'description': u'「マイナビニュース」は、ニュースと読み物を中心とした総合専門サイトです。',
        'entries': (
            {
                'id': 'http://news.mynavi.jp/news/2013/04/05/220/index.html',
                'title': u'PostgreSQLセキュリティアップデート版登場',
                'link': 'http://rss.rssad.jp/rss/artclk/MCpt8OV0jzw0/47958d2ee87693baee2ea6b22518d995?ul=AJu1bqB67gY2itpnemUJLNRFzzYrD_29LgmLK5dFVfqOTQZo1seyVTKAqvkwzbQle_9wHqIxiusSfSr9J9v.pfMWPVmS',
                'published': parse('2013-04-05T17:45:46+09:00'),
                'description': u'<p>PostgreSQL Global Development Groupは4月4日(米国時間)'
            },
            {
                'id': 'http://news.mynavi.jp/news/2013/04/05/143/index.html',
                'title': u'ライフボート、Windows Server 2012対応のサーバー用バックアップソフト',
                'link': 'http://rss.rssad.jp/rss/artclk/MCpt8OV0jzw0/fbd8278f34289b1714fd85800d57a378?ul=TIHMO3S3e4qiquV.SakKYkUrucq._PEER8ede6_rBO4ECOf1ebppaClBzEOogTnepEPWz8VsHgIbMmeEVQfyusKQ0QBb',
                'published': parse('2013-04-05T13:44:04+09:00'),
                'description': u'<p>ライフボートは4月5日、独パラゴンソフトウェアグループが開発'
            },
            {
                'id': 'http://news.mynavi.jp/news/2013/04/05/142/index.html',
                'title': u'DNP、新規事業に向け研究や実証実験を行う「サービスデザイン・ラボ」設立',
                'link': 'http://rss.rssad.jp/rss/artclk/MCpt8OV0jzw0/8b3d6d2859cf06a18cdbb126184298f9?ul=uBOdgPVrYVIA02EjCAXF9IQXysIsNUeFOfvZwQtXSbjmkJtP5.W6XgWCXNVNmUkaICgBPQPt7UtD4xmFSd2_WWlebWkD',
                'published': parse('2013-04-05T13:40:00+09:00'),
                'description': u'<p>大日本印刷(DNP)は4月5日、生活者中心の価値分析からサービスを'
            },
            {
                'id': 'http://news.mynavi.jp/news/2013/04/05/107/index.html',
                'title': u'タブレットの低価格・高機能化でPC減少、前年比7.6%減 - Androidシェア拡大',
                'link': 'http://rss.rssad.jp/rss/artclk/MCpt8OV0jzw0/e6da81eac81c4a0de99653a67100247a?ul=MComG95.FADWE9aSxGTIyQJ5LnDf_v_jWqNQHlc5Gwjq2F3AyhUx4twQ0F9F1oBlam6hkT9rvd3PnZCjGUL0NoDzZ6ZP',
                'published': parse('2013-04-05T11:54:03+09:00'),
                'description': u'<p>米Gartnerは4月4日(英国時間)、PC、タブレット、スマートフォン'
            }
        )
    }),
    ('rssone/mycom_relative.xml', {
        'id': 'http://news.mynavi.jp/enterprise/',
        'title': u'マイナビニュース エンタープライズ',
        'link': 'http://news.mynavi.jp/enterprise/',
        'description': u'「マイナビニュース」は、ニュースと読み物を中心とした総合専門サイトです。',
        'entries': (
            {
                'id': 'http://news.mynavi.jp/news/2013/04/05/220/index.html',
                'title': u'PostgreSQLセキュリティアップデート版登場',
                'link': 'http://news.mynavi.jp/news/2013/04/05/220/index.html',
                'published': parse('2013-04-05T17:45:46+09:00'),
                'description': u'<p>PostgreSQL Global Development Groupは4月4日(米国時間)'
            },
        )
    }),
    ('rssone/fallback.xml', {
        'id': 'http://b.hatena.ne.jp/hotentry',
        'title': u'はてなブックマーク - 人気エントリー',
        'link': 'http://b.hatena.ne.jp/hotentry',
        'description': u'最近の人気エントリー',
        'entries': (
            {
                'id': 'http://bazubu.com/seo-13666.html',
                'title': u'<SEO対策> 検索順位の上位を独占するために私が行っている36の手順',
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
