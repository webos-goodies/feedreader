import lxml.objectify
import lxml.html
import re

__all__ = ('ParseError', 'InvalidFeed', 'from_string')

# TODO: change the feeds to a registration model
from feeds.atom10 import Atom10Feed
from feeds.atom03 import Atom03Feed
from feeds.rss20 import RSS20Feed
from feeds.rss10 import RSS10Feed
from feeds.rss091 import RSS091Feed

from fallback.atom import AtomFallback
from fallback.rss20 import RSS20Fallback
from fallback.rss10 import RSS10Fallback
from fallback.rss091 import RSS091Fallback

feeds = (Atom10Feed, RSS20Feed, RSS10Feed, Atom03Feed, RSS091Feed)
fallbacks = (AtomFallback, RSS20Fallback, RSS10Fallback, RSS091Fallback)

class InvalidFeed(Exception): pass
class ParseError(Exception): pass

XML_RE    = re.compile(r'''^(\s*<\?xml[^>]+)encoding=['"]([^'">]+)['"]''')
CDATA_RE  = re.compile(r'<!\[CDATA\[(.*?)\]\]>', re.DOTALL)
LINK_RE   = re.compile(r'(</?)link', re.IGNORECASE)
XML_ILLEGAL_RE = re.compile(u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])')
# XML_ILLEGAL_RE = re.compile(
#   u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' +
#   u'|' +
#   u'([%s-%s][^%s-%s])|([^%s-%s][%s-%s])|([%s-%s]$)|(^[%s-%s])' % (
#     unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),
#     unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),
#     unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff)))


def _replace_encoding(s):
  encoding = ['utf-8']
  def to_utf8(m):
    c = m.group(2).lower()
    if c == 'shift_jis' or c == 'shift-jis' or c == 'shiftjis' or c == 'sjis':
      encoding[0] = 'cp932'
    else:
      encoding[0] = m.group(2)
    return m.group(1)
  s = XML_RE.sub(to_utf8, s, 1)
  if not isinstance(s, unicode):
    s = unicode(s, encoding[0], 'ignore')
  return s

def _remove_illegals(s):
  s = s[0:s.rfind(u'>') + 1]
  s = XML_ILLEGAL_RE.sub('', s)
  return s

def _remove_cdata(s):
  def escape_cdata(m):
    escaped = m.group(1).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    escaped = escaped.replace('"', '&quot;').replace("'", '&#39;')
    return escaped
  return CDATA_RE.sub(escape_cdata, s)

def _replace_linktag(s):
  return LINK_RE.sub(lambda m:m.group(1) + 'feedlink', s)


def _from_parsed(parsed, classes):
  for feed in classes:
    result = feed(parsed)
    if result.is_valid:
      return result
  raise InvalidFeed(parsed.tag)

def from_string(data, *args, **kwargs):
  data = _replace_encoding(data)
  data = _remove_illegals(data)
  try:
    parsed = lxml.objectify.fromstring(data, *args, **kwargs)
    return _from_parsed(parsed, feeds)
  except:
    pass
  data = _remove_cdata(data)
  data = _replace_linktag(data)
  parsed = lxml.html.fromstring(data)
  return _from_parsed(parsed, fallbacks)
