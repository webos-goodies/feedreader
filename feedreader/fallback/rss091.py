"""
RSS 0.91 Support
"""

from feedreader.fallback.base import (Feed, Item, get_element_text, get_attribute, search_child,
                                      get_xpath_node, get_xpath_text, get_xpath_datetime)


class RSS091Fallback(Feed):
  __feed__ = 'RSS 0.91 Fallback'

  def __init__(self, element):
    self.__channel = None
    super(RSS091Fallback, self).__init__(element)

  @property
  def channel(self):
    if self.__channel is None:
      self.__channel = get_xpath_node(self._element, 'descendant::channel')
    return self.__channel

  @property
  def is_valid(self):
    return (self._element.tag.lower() == 'rss' and
            (self._element.attrib['version'] == '0.91' or
             self._element.attrib['version'] == '0.92') and
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
    return get_xpath_datetime(self._channel, 'lastbuilddate')

  @property
  def updated(self):
    return None

  @property
  def entries(self):
    return [RSS091Item(item) for item in self.channel.xpath('descendant::item')]


class RSS091Item(Item):

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
    return None

  @property
  def author_email(self):
    return None

  @property
  def author_link(self):
    return None

  @property
  def description(self):
    return get_xpath_text(self._element, 'descendant::description')

  @property
  def published(self):
    return get_xpath_datetime(self._element, 'descendant::pubdate')

  @property
  def updated(self):
    return None
