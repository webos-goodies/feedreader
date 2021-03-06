"""
Atom 1.0 Support
"""

from feedreader.base import remove_tags, escape_html
from feedreader.feeds.base import (PREFERRED_LINK_TYPES, PREFERRED_CONTENT_TYPES,
                                   Feed, Item, get_element_text, get_attribute, search_child,
                                   get_descendant, get_descendant_text, get_descendant_datetime,
                                   safe_strip, normalize_spaces, unescape_html,
                                   collect_descendant_text, collect_descendant_xml)


class Atom10Feed(Feed):
  __feed__ = 'Atom 1.0'

  @property
  def is_valid(self):
    # <feed xmlns="http://www.w3.org/2005/Atom">
    return self._element.tag == '{http://www.w3.org/2005/Atom}feed'

  @property
  def id(self):
    return safe_strip(get_descendant_text(self._element, 'id'))

  @property
  def title(self):
    return normalize_spaces(get_descendant_text(self._element, 'title'))

  @property
  def link(self):
    link = search_child(self._element, '{http://www.w3.org/2005/Atom}link',
                        ('rel', 'alternate', 'type', PREFERRED_LINK_TYPES))
    return safe_strip(get_attribute(link, 'href', is_url=True))

  @property
  def description(self):
    subtitle = search_child(self._element, '{http://www.w3.org/2005/Atom}subtitle',
                            ('type', PREFERRED_CONTENT_TYPES))
    return get_element_text(subtitle)

  @property
  def published(self):
    return get_descendant_datetime(self._element, 'published')

  @property
  def updated(self):
    return get_descendant_datetime(self._element, 'updated')

  @property
  def entries(self):
    node_name = '{http://www.w3.org/2005/Atom}entry'
    return [Atom10Item(item) for item in self._element.iterchildren(tag=node_name)]


class Atom10Item(Item):

  @property
  def id(self):
    return safe_strip(get_descendant_text(self._element, 'id'))

  @property
  def title(self):
    value   = None
    element = get_descendant(self._element, 'title')
    if element is not None:
      type = element.get('type', 'text').lower().strip()
      if type == 'xhtml' or element.countchildren() > 0:
        value = collect_descendant_text(element)
      elif type == 'html':
        value = unescape_html(remove_tags(get_element_text(element)))
      else:
        value = get_element_text(element)
    return normalize_spaces(value)

  @property
  def link(self):
    link = search_child(self._element, '{http://www.w3.org/2005/Atom}link',
                        ('rel', 'alternate', 'type', PREFERRED_LINK_TYPES))
    return safe_strip(get_attribute(link, 'href', is_url=True))

  @property
  def author_name(self):
    return normalize_spaces(get_descendant_text(self._element, 'author', 'name'))

  @property
  def author_email(self):
    return safe_strip(get_descendant_text(self._element, 'author', 'email'))

  @property
  def author_link(self):
    return safe_strip(get_descendant_text(self._element, 'author', 'uri', is_url=True))

  @property
  def description(self):
    value   = None
    content = search_child(self._element, '{http://www.w3.org/2005/Atom}content',
                           ('type', PREFERRED_CONTENT_TYPES))
    if content is None:
      content = search_child(self._element, '{http://www.w3.org/2005/Atom}summary',
                             ('type', PREFERRED_CONTENT_TYPES))
    if content is not None:
      type = content.get('type', 'text').lower().strip()
      if type == 'xhtml' or content.countchildren() > 0:
        value = collect_descendant_xml(content)
      elif type == 'html':
        value = get_element_text(content)
      else:
        value = escape_html(get_element_text(content))
    return safe_strip(value)

  @property
  def published(self):
    return get_descendant_datetime(self._element, 'published')

  @property
  def updated(self):
    return get_descendant_datetime(self._element, 'updated')
