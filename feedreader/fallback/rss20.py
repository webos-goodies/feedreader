"""
RSS 2.0 Support
"""

from feedreader.fallback.base import (Feed, Item, get_element_text, get_attribute, search_child,
                                      get_xpath_node, get_xpath_text, get_xpath_datetime)


class RSS20Fallback(Feed):
  __feed__ = 'RSS 2.0 Fallback'

  def __init__(self, element):
    self.__channel = None
    if element.tag.lower() != 'rss':
      el = get_xpath_node(element, 'descendant::rss')
      if el is not None:
        element = el
    super(RSS20Fallback, self).__init__(element)

  @property
  def channel(self):
    if self.__channel is None:
      self.__channel = get_xpath_node(self._element, 'descendant::channel')
    return self.__channel

  @property
  def is_valid(self):
    return (self._element.tag.lower() == 'rss' and
            '2.0' in self._element.attrib['version'] and
            self.channel is not None)

  @property
  def id(self):
    return None

  @property
  def title(self):
    return get_xpath_text(self.channel, 'title')

  @property
  def link(self):
    return get_xpath_text(self.channel, 'feedlink')

  @property
  def description(self):
    return get_xpath_text(self.channel, 'description')

  @property
  def published(self):
    return (get_xpath_datetime(self._channel, 'pubdate') or
            get_xpath_datetime(self._channel, 'date'))

  @property
  def updated(self):
    return None

  @property
  def entries(self):
    return [RSS20Item(item) for item in self.channel.xpath('descendant::item')]


class RSS20Item(Item):

  @property
  def id(self):
    return get_xpath_text(self._element, 'descendant::guid')

  @property
  def title(self):
    return get_xpath_text(self._element, 'descendant::title')

  @property
  def link(self):
    return get_xpath_text(self._element, 'descendant::feedlink')

  @property
  def author_name(self):
    return (get_xpath_text(self._element, 'descendant::author') or
            get_xpath_text(self._element, 'descendant::creator'))

  @property
  def author_email(self):
    return None

  @property
  def author_link(self):
    return None

  @property
  def description(self):
    return (get_xpath_text(self._element, 'descendant::encoded') or
            get_xpath_text(self._element, 'descendant::description'))

  @property
  def published(self):
    return (get_xpath_datetime(self._element, 'descendant::pubdate') or
            get_xpath_datetime(self._element, 'descendant::date'))

  @property
  def updated(self):
    return None
