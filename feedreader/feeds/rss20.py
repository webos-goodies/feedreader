"""
RSS 2.0 Support
"""

import cgi
from feedreader.feeds.base import (Feed, Item, get_element_text, get_attribute, search_child,
                                   get_descendant, get_descendant_text, get_descendant_datetime,
                                   safe_strip, normalize_spaces, unescape_html)


class RSS20Feed(Feed):
  __feed__ = 'RSS 2.0'

  @property
  def channel(self):
    return getattr(self._element, 'channel', None)

  @property
  def is_valid(self):
    return (self._element.tag == 'rss' and
            '2.0' in self._element.attrib['version'] and
            self.channel is not None)

  @property
  def id(self):
    return None

  @property
  def title(self):
    return normalize_spaces(get_descendant_text(self.channel, 'title'))

  @property
  def link(self):
    return safe_strip(get_descendant_text(self.channel, 'link', is_url=True))

  @property
  def description(self):
    return get_descendant_text(self.channel, 'description')

  @property
  def published(self):
    return (get_descendant_datetime(self._channel, 'pubDate') or
            get_descendant_datetime(self._channel, '{http://purl.org/dc/elements/1.1/}date'))

  @property
  def updated(self):
    return None

  @property
  def entries(self):
    entries   = [RSS20Item(item) for item in self.channel.iterchildren(tag='item')]
    ok        = True
    prev_link = None
    for entry in entries:
      link = entry.link
      if link is None or link == prev_link:
        ok = False
        break
      prev_link = link
    if not ok:
      for entry in entries:
        entry.use_enclosure_as_link()
    return entries


class RSS20Item(Item):

  def __init__(self, element):
    super(RSS20Item, self).__init__(element)
    self.__link_cache = None
    self.__enclosures_cache = None

  @property
  def id(self):
    return safe_strip(get_descendant_text(self._element, 'guid'))

  @property
  def title(self):
    return normalize_spaces(unescape_html(get_descendant_text(self._element, 'title')))

  @property
  def link(self):
    if self.__link_cache is None:
      self.__link_cache = safe_strip(get_descendant_text(self._element, 'link', is_url=True))
    return self.__link_cache

  @property
  def author_name(self):
    value = (get_descendant_text(self._element, 'author') or
             get_descendant_text(self._element, '{http://purl.org/dc/elements/1.1/}creator'))
    return normalize_spaces(value)

  @property
  def author_email(self):
    return None

  @property
  def author_link(self):
    return None

  @property
  def description(self):
    text = (get_descendant_text(self._element,
                                '{http://purl.org/rss/1.0/modules/content/}encoded') or
            get_descendant_text(self._element, 'description'))
    enclosures = [
      '<enclosure url="%s" type="%s"></enclosure>' % (
        cgi.escape(e['url'], quote=True), cgi.escape(e['type'], quote=True))
      for e in self.enclosures]
    if enclosures:
      text = "<feedeen>\n%s\n</feedeen>\n%s" % ("\n".join(enclosures), text)
    return text

  @property
  def published(self):
    return (get_descendant_datetime(self._element, 'pubDate') or
            get_descendant_datetime(self._element, '{http://purl.org/dc/elements/1.1/}date'))

  @property
  def updated(self):
    return None

  @property
  def enclosures(self):
    if self.__enclosures_cache is None:
      self.__enclosures_cache = []
      for e in getattr(self._element, 'enclosure', ()):
        url  = get_attribute(e, 'url', is_url=True)
        type = get_attribute(e, 'type')
        if url and type:
          self.__enclosures_cache.append({ 'url':url, 'type':type })
    return self.__enclosures_cache

  def use_enclosure_as_link(self):
    entries = self.enclosures
    if entries:
      self.__link_cache = entries[0]['url']
