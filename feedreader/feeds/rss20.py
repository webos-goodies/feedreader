"""
RSS 2.0 Support
"""

from feedreader.feeds.base import (Feed, Item, get_element_text, get_attribute, search_child,
                                   get_descendant, get_descendant_text, get_descendant_datetime,
                                   safe_strip, normalize_spaces)


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
    return safe_strip(get_descendant_text(self.channel, 'link'))

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
    return [RSS20Item(item) for item in self.channel.iterchildren(tag='item')]


class RSS20Item(Item):

  @property
  def id(self):
    return safe_strip(get_descendant_text(self._element, 'guid'))

  @property
  def title(self):
    return normalize_spaces(get_descendant_text(self._element, 'title'))

  @property
  def link(self):
    return safe_strip(get_descendant_text(self._element, 'link'))

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
    return (get_descendant_text(self._element,
                                '{http://purl.org/rss/1.0/modules/content/}encoded') or
            get_descendant_text(self._element, 'description'))

  @property
  def published(self):
    return (get_descendant_datetime(self._element, 'pubDate') or
            get_descendant_datetime(self._element, '{http://purl.org/dc/elements/1.1/}date'))

  @property
  def updated(self):
    return None
