"""
Atom 0.3 Support
"""

from feedreader.feeds.base import (PREFERRED_LINK_TYPES, PREFERRED_CONTENT_TYPES,
                                   Feed, Item, get_element_text, get_attribute, search_child,
                                   get_descendant, get_descendant_text, get_descendant_datetime,
                                   safe_strip, normalize_spaces)


class Atom03Feed(Feed):
  __feed__ = 'Atom 0.3'

  @property
  def is_valid(self):
    # <feed version="0.3" xmlns="http://purl.org/atom/ns#">
    return self._element.tag == '{http://purl.org/atom/ns#}feed'

  @property
  def id(self):
    return safe_strip(get_descendant_text(self._element, 'id'))

  @property
  def title(self):
    return normalize_spaces(get_descendant_text(self._element, 'title'))

  @property
  def link(self):
    link = search_child(self._element, '{http://purl.org/atom/ns#}link',
                        ('rel', 'alternate', 'type', PREFERRED_LINK_TYPES))
    return safe_strip(get_attribute(link, 'href'))

  @property
  def description(self):
    return get_descendant_text(self._element, 'tagline')

  @property
  def published(self):
    return get_descendant_datetime(self._element, 'issued')

  @property
  def updated(self):
    return get_descendant_datetime(self._element, 'modified')

  @property
  def entries(self):
    node_name = '{http://purl.org/atom/ns#}entry'
    return [Atom03Item(item) for item in self._element.iterchildren(tag=node_name)]


class Atom03Item(Item):

  @property
  def id(self):
    return safe_strip(get_descendant_text(self._element, 'id'))

  @property
  def title(self):
    return normalize_spaces(get_descendant_text(self._element, 'title'))

  @property
  def link(self):
    link = search_child(self._element, '{http://purl.org/atom/ns#}link',
                        ('rel', 'alternate', 'type', PREFERRED_LINK_TYPES))
    return safe_strip(get_attribute(link, 'href'))

  @property
  def author_name(self):
    return normalize_spaces(get_descendant_text(self._element, 'author', 'name'))

  @property
  def author_email(self):
    return safe_strip(get_descendant_text(self._element, 'author', 'email'))

  @property
  def author_link(self):
    return safe_strip(get_descendant_text(self._element, 'author', 'uri'))

  @property
  def description(self):
    content = search_child(self._element, '{http://purl.org/atom/ns#}content',
                           ('type', PREFERRED_CONTENT_TYPES))
    if content is None:
      content = search_child(self._element, '{http://purl.org/atom/ns#}summary',
                             ('type', PREFERRED_CONTENT_TYPES))
    return get_element_text(content)

  @property
  def published(self):
    return get_descendant_datetime(self._element, 'issued')

  @property
  def updated(self):
    return get_descendant_datetime(self._element, 'modified')
