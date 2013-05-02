import dateutil.parser

PREFERRED_TITLE_TYPES   = ('text', 'html')
PREFERRED_LINK_TYPES    = ('text/html', 'application/xhtml+xml', 'text/plain')
PREFERRED_CONTENT_TYPES = ('html', 'text')

def unicodify(s):
  if s is None:
    return u''
  elif isinstance(s, unicode):
    return s
  return unicode(s, errors='replace')

def parse_date(s):
  result = None
  try:
    result = dateutil.parser.parse(s)
  except:
    pass
  return result

def get_element_text(element):
  if element is None:
    return None
  return unicodify(element.text).strip()

def get_descendant(element, *args):
  for node_name in args:
    if element is None:
      return None
    element = getattr(element, node_name, None)
  return element

def get_descendant_text(element, *args):
  element = get_descendant(element, *args)
  return get_element_text(element)

def get_descendant_datetime(element, *args):
  text = get_descendant_text(element, *args)
  if text is None:
    return None
  return parse_date(text)

def get_attribute(element, attr_name):
  if element is None:
    return None
  attr = element.get(attr_name, None)
  if attr is None:
    return None
  return unicodify(attr).strip()

def search_child(element, node_name, attrs):
  if element is None:
    return None
  candidate, level = None, -1
  for el in element.iterchildren(tag=node_name):
    l, length = 0, len(attrs)
    for i in xrange(0, length, 2):
      value     = get_attribute(el, attrs[i])
      condition = attrs[i + 1]
      if isinstance(condition, (list, tuple)):
        try:
          l = l + (16 << (length - i) / 2) + len(condition) - indexOf(condition, value)
        except:
          pass
      elif value == condition:
        l = l + (16 << (length - i) / 2)
    if l > level:
      candidate, level = el, l
  return candidate


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
