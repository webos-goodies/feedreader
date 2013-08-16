"""
Malformed Atom fallback
"""

from feedreader.fallback.base import (PREFERRED_TITLE_TYPES, PREFERRED_LINK_TYPES,
                                      PREFERRED_CONTENT_TYPES,
                                      Feed, Item, get_element_text, get_attribute, search_child,
                                      get_xpath_node, get_xpath_text, get_xpath_datetime,
                                      safe_strip, normalize_spaces)


class AtomFallback(Feed):
  __feed__ = 'Atom Fallback'

  @property
  def is_valid(self):
    # <feed xmlns="http://www.w3.org/2005/Atom">
    return self._element.tag.lower() == 'feed'

  @property
  def id(self):
    return safe_strip(get_xpath_text(self._element, 'id'))

  @property
  def title(self):
    return normalize_spaces(get_xpath_text(self._element, 'title'))

  @property
  def link(self):
    link = search_child(self._element, 'feedlink',
                        ('rel', 'alternate', 'type', PREFERRED_LINK_TYPES))
    return safe_strip(get_attribute(link, 'href'))

  @property
  def description(self):
    subtitle = search_child(self._element, 'subtitle',
                            ('type', PREFERRED_CONTENT_TYPES))
    if subtitle is not None:
      return get_element_text(subtitle)
    else:
      return get_xpath_text(self._element, 'tagline')

  @property
  def published(self):
    return (get_xpath_datetime(self._element, 'published') or
            get_xpath_datetime(self._element, 'issued'))

  @property
  def updated(self):
    return (get_xpath_datetime(self._element, 'updated') or
            get_xpath_datetime(self._element, 'modified'))

  @property
  def entries(self):
    return [Atom10Item(item) for item in self._element.xpath('descendant::entry')]


class Atom10Item(Item):

  @property
  def id(self):
    return safe_strip(get_xpath_text(self._element, 'descendant::id'))

  @property
  def title(self):
    return normalize_spaces(get_xpath_text(self._element, 'descendant::title'))

  @property
  def link(self):
    link = search_child(self._element, 'descendant::feedlink',
                        ('rel', 'alternate', 'type', PREFERRED_LINK_TYPES))
    return safe_strip(get_attribute(link, 'href'))

  @property
  def author_name(self):
    return normalize_spaces(get_xpath_text(self._element, 'descendant::author/descendant::name'))

  @property
  def author_email(self):
    return safe_strip(get_xpath_text(self._element, 'descendant::author/descendant::email'))

  @property
  def author_link(self):
    return safe_strip(get_xpath_text(self._element, 'descendant::author/descendant::uri'))

  @property
  def description(self):
    content = search_child(self._element, 'descendant::content',
                           ('type', PREFERRED_CONTENT_TYPES))
    if content is None:
      content = search_child(self._element, 'descendant::summary',
                             ('type', PREFERRED_CONTENT_TYPES))
    return get_element_text(content)

  @property
  def published(self):
    return (get_xpath_datetime(self._element, 'descendant::published') or
            get_xpath_datetime(self._element, 'descendant::issued'))

  @property
  def updated(self):
    return (get_xpath_datetime(self._element, 'descendant::updated') or
            get_xpath_datetime(self._element, 'descendant::modified'))
