import dateutil.parser
from feedreader import base

PREFERRED_TITLE_TYPES   = base.PREFERRED_TITLE_TYPES
PREFERRED_LINK_TYPES    = base.PREFERRED_LINK_TYPES
PREFERRED_CONTENT_TYPES = base.PREFERRED_CONTENT_TYPES

unicodify  = base.unicodify
parse_date = base.parse_date

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
