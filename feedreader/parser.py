import lxml.objectify
import re

__all__ = ('ParseError', 'InvalidFeed', 'from_string')

# TODO: change the feeds to a registration model
from feeds.atom10 import Atom10Feed
from feeds.atom03 import Atom03Feed
from feeds.rss20 import RSS20Feed
from feeds.rss10 import RSS10Feed
from feeds.rss091 import RSS091Feed

feeds = (Atom10Feed, RSS20Feed, RSS10Feed, Atom03Feed, RSS091Feed)

ACCEPT_HEADER = "application/atom+xml,application/rdf+xml,application/rss+xml,application/x-netcdf,application/xml;q=0.9,text/xml;q=0.2,*/*;q=0.1"

USER_AGENT = 'py-feedreader'

class InvalidFeed(Exception): pass
class ParseError(Exception): pass

CDATA_RE  = re.compile(r'<!\[CDATA\[(.*?)\]\]>', re.DOTALL)
ENTITY_RE = re.compile(r'&(?!(?:lt|gt|quot|amp|apos|#\d+|#x[0-9a-fA-F]+);)')

def _preprocess(str):
    cdata = []
    def mask_cdata(m):
        cdata.append(m.group(1))
        return '<![CDATA[%d]]>' % (len(cdata) - 1)
    def restore_cdata(m):
        return '<![CDATA[%s]]>' % cdata.pop()
    str = CDATA_RE.sub(mask_cdata, str)
    str = ENTITY_RE.sub('&amp;', str)
    cdata.reverse()
    str = CDATA_RE.sub(restore_cdata, str)
    return str


def _from_parsed(parsed):
    for feed in feeds:
        result = feed(parsed)
        if result.is_valid:
            return result
    raise InvalidFeed(parsed.tag)

def from_string(data, *args, **kwargs):
    parsed = lxml.objectify.fromstring(_preprocess(data), *args, **kwargs)
    return _from_parsed(parsed)
