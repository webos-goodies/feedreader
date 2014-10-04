import dateutil.parser
from feedreader import base

PREFERRED_LINK_TYPES    = base.PREFERRED_LINK_TYPES
PREFERRED_CONTENT_TYPES = base.PREFERRED_CONTENT_TYPES

unicodify  = base.unicodify
parse_date = base.parse_date
safe_strip = base.safe_strip
normalize_spaces = base.normalize_spaces


def get_element_text(element):
  if element is None:
    return None
  text = element.text
  if text is None:
    return u''
  return unicodify(text).strip()

def get_xpath_node(element, xpath):
  if element is None:
    return None
  c = element.xpath(xpath)
  if(len(c) < 1):
    return None
  return c[0]

def get_xpath_text(element, xpath):
  element = get_xpath_node(element, xpath)
  return get_element_text(element)

def get_xpath_datetime(element, xpath):
  text = get_xpath_text(element, xpath)
  return parse_date(safe_strip(text))

def get_attribute(element, attr_name):
  if element is None:
    return None
  attr = element.get(attr_name, None)
  if attr is None:
    return None
  return unicodify(attr).strip()

def search_child(element, xpath, attrs):
  if element is None:
    return None
  candidate, level = None, -1
  for el in element.xpath(xpath):
    l, length = 0, len(attrs)
    for i in xrange(0, length, 2):
      value     = get_attribute(el, attrs[i])
      condition = attrs[i + 1]
      if isinstance(condition, (list, tuple)):
        try:
          l = l + (16 << (length - i) / 2) + len(condition) - condition.index(value)
        except:
          pass
      elif value == condition:
        l = l + (16 << (length - i) / 2)
    if l > level:
      candidate, level = el, l
  return candidate


class Item(base.Item):
  pass


class Feed(base.Feed):
  __feed__ = ''

  @property
  def feed(self):
    return self.__feed__
