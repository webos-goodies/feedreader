"""
RSS 0.91 Support
"""

from feedreader.feeds.base import (Feed, Item, get_element_text, get_attribute, search_child,
                                   get_descendant, get_descendant_text, get_descendant_datetime)


class RSS091Feed(Feed):
  __feed__ = 'RSS 0.91'

  @property
  def channel(self):
    return getattr(self._element, 'channel', None)

  @property
  def is_valid(self):
    return (self._element.tag == 'rss' and
            (self._element.attrib['version'] == '0.91' or
             self._element.attrib['version'] == '0.92') and
            self.channel is not None)

  @property
  def id(self):
    return None

  @property
  def title(self):
    return get_descendant_text(self.channel, 'title')

  @property
  def link(self):
    return get_descendant_text(self.channel, 'link')

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
    return get_descendant_text(self._element, 'guid')

  @property
  def title(self):
    return get_descendant_text(self._element, 'title')

  @property
  def link(self):
    return get_descendant_text(self._element, 'link')

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
