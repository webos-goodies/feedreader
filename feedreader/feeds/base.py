import re
import urlparse
import dateutil.parser
import lxml.etree
from feedreader import base

PREFERRED_LINK_TYPES    = base.PREFERRED_LINK_TYPES
PREFERRED_CONTENT_TYPES = base.PREFERRED_CONTENT_TYPES

unicodify  = base.unicodify
parse_date = base.parse_date
safe_strip = base.safe_strip
normalize_spaces = base.normalize_spaces
unescape_html = base.unescape_html

ROOT_TAG_RE  = re.compile(r'^\s*<[^>]+>|</[^>]+>\s*$')


def get_element_text(element, is_url=False):
  if element is None:
    return None
  text = unicodify(element.text).strip()
  base = is_url and element.base
  if base:
    text = urlparse.urljoin(base, text)
  return text

def get_descendant(element, *args):
  for node_name in args:
    if element is None:
      return None
    element = getattr(element, node_name, None)
  return element

def get_descendant_text(element, *args, **kwargs):
  element = get_descendant(element, *args)
  return get_element_text(element, **kwargs)

def get_descendant_datetime(element, *args):
  text = get_descendant_text(element, *args)
  return parse_date(safe_strip(text))

def get_attribute(element, attr_name, is_url=False):
  if element is None:
    return None
  attr = element.get(attr_name, None)
  if attr is None:
    return None
  attr = unicodify(attr).strip()
  base = is_url and element.base
  if base:
    attr = urlparse.urljoin(base, attr)
  return attr

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

def collect_descendant_text(element):
  return lxml.etree.tostring(element, encoding=unicode, with_tail=False, method='text')

def collect_descendant_xml(element):
  if element is None:
    return None
  xml = lxml.etree.tostring(element, encoding=unicode, with_tail=False)
  return ROOT_TAG_RE.sub('', xml)


class Item(base.Item):
  pass


class Feed(base.Feed):
  __feed__ = ''

  @property
  def feed(self):
    return self.__feed__
