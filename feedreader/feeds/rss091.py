"""
RSS 0.91 Support
"""

from feedreader.feeds.base import (Feed, Item, get_element_text, get_attribute, search_child,
                                   get_descendant, get_descendant_text, get_descendant_datetime,
                                   safe_strip, normalize_spaces, unescape_html)


class RSS091Feed(Feed):
  __feed__ = 'RSS 0.91'

  @property
  def channel(self):
    return getattr(self._element, 'channel', None)

  @property
  def is_valid(self):
    return (self._element.tag == 'rss' and
            '0.9' in self._element.attrib['version'] and
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
    return get_descendant_datetime(self._channel, 'lastBuildDate')

  @property
  def updated(self):
    return None

  @property
  def entries(self):
    return [RSS091Item(item) for item in self.channel.iterchildren(tag='item')]


class RSS091Item(Item):

  @property
  def id(self):
    return safe_strip(get_descendant_text(self._element, 'guid'))

  @property
  def title(self):
    return normalize_spaces(unescape_html(get_descendant_text(self._element, 'title')))

  @property
  def link(self):
    return safe_strip(get_descendant_text(self._element, 'link', is_url=True))

  @property
  def author_name(self):
    return None

  @property
  def author_email(self):
    return None

  @property
  def author_link(self):
    return None

  @property
  def description(self):
    return get_descendant_text(self._element, 'description')

  @property
  def published(self):
    return get_descendant_datetime(self._element, 'pubDate')

  @property
  def updated(self):
    return None
