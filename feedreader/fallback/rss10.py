"""
RSS 1.0 Support
"""

from feedreader.fallback.base import (Feed, Item, get_element_text, get_attribute, search_child,
                                      get_xpath_node, get_xpath_text, get_xpath_datetime,
                                      safe_strip, normalize_spaces, unescape_html)


class RSS10Fallback(Feed):
  __feed__ = 'RSS 1.0 Fallback'

  def __init__(self, element):
    self.__channel = None
    super(RSS10Fallback, self).__init__(element)

  @property
  def channel(self):
    if self.__channel is None:
      self.__channel = get_xpath_node(self._element, 'descendant::channel')
    return self.__channel

  @property
  def is_valid(self):
    return (self._element.tag.upper() == 'RDF' and self.channel is not None)

  @property
  def id(self):
    return safe_strip(get_attribute(self._element, 'about'))

  @property
  def title(self):
    return normalize_spaces(get_xpath_text(self.channel, 'title'))

  @property
  def link(self):
    return safe_strip(get_xpath_text(self.channel, 'feedlink'))

  @property
  def description(self):
    return get_xpath_text(self.channel, 'description')

  @property
  def published(self):
    return None

  @property
  def updated(self):
    return None

  @property
  def entries(self):
    return [RSS10Item(item) for item in self._element.xpath('descendant::item')]


class RSS10Item(Item):

  @property
  def id(self):
    return safe_strip(get_attribute(self._element, 'rdf:about'))

  @property
  def title(self):
    return normalize_spaces(unescape_html(get_xpath_text(self._element, 'descendant::title')))

  @property
  def link(self):
    return safe_strip(get_xpath_text(self._element, 'descendant::feedlink'))

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
    text = get_xpath_text(self._element, 'descendant::encoded')
    if text is None:
      text = get_xpath_text(self._element, 'descendant::description')
    return text

  @property
  def published(self):
    return get_xpath_datetime(self._element, 'descendant::date')

  @property
  def updated(self):
    return None
