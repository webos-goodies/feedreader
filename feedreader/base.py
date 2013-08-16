import re
import dateutil.parser

PREFERRED_TITLE_TYPES   = ('text', 'html')
PREFERRED_LINK_TYPES    = ('text/html', 'application/xhtml+xml', 'text/plain')
PREFERRED_CONTENT_TYPES = ('html', 'text')

SPACES_RE = re.compile(r'\s+')


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
  if isinstance(s, basestring):
    return SPACES_RE.sub(' ', s.strip())
  else:
    return s


class Base(object):
  def __init__(self, element):
    self._element = element


class Item(Base):
  pass


class Feed(Base):
  __feed__ = ''

  @property
  def feed(self):
    return self.__feed__
