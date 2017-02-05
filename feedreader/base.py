import re
import dateutil.parser
from oxy import strutil

PREFERRED_LINK_TYPES    = ('text/html', 'application/xhtml+xml', 'text/plain')
PREFERRED_CONTENT_TYPES = ('html', 'xhtml', 'text')

SPACES_RE    = re.compile(ur'[\u0009-\u000d\u0020\u0085\u2028\u2029]+')
STRIP_RE     = re.compile(ur'\A[\s\u200b-\u200d\ufeff]+|[\s\u200b-\u200d\ufeff]+\Z', re.U)
TAG_RE       = re.compile(r'</?[a-zA-Z<!\?][^>]*>')
ENTITY_RE    = re.compile(r'[<>&"]')
ENTITY_MAP   = { '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;' }


def unicodify(s):
  if s is None:
    return u''
  elif isinstance(s, unicode):
    return s
  return unicode(s, errors='replace')

def parse_date(s):
  result = None
  try:
    if s is not None:
      result = dateutil.parser.parse(s)
  except:
    pass
  return result

def safe_strip(s):
  if isinstance(s, basestring):
    return s.strip()
  else:
    return s

def normalize_spaces(s):
  if isinstance(s, bytes):
    s = unicode(s, errors='replace')
  elif not isinstance(s, unicode):
    return s
  return SPACES_RE.sub(u' ', STRIP_RE.sub(u'', s))

def remove_tags(s):
  if isinstance(s, basestring):
    return TAG_RE.sub('', s)
  else:
    return s

def escape_html(s):
  if isinstance(s, basestring):
    return ENTITY_RE.sub(lambda m:ENTITY_MAP[m.group(0)], s)
  else:
    return s

def unescape_html(s):
  if isinstance(s, basestring):
    return strutil.unescape_html(s)
  else:
    return s

class Base(object):
  def __init__(self, element):
    self._element = element


class Item(Base):
  @property
  def podcast(self):
    return None


class Feed(Base):
  __feed__ = ''

  @property
  def feed(self):
    return self.__feed__
