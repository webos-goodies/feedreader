"""
RSS 1.0 Support
"""

from feedreader.feeds.base import (Feed, Item, get_element_text, get_attribute, search_child,
                                   get_descendant, get_descendant_text, get_descendant_datetime,
                                   safe_strip, normalize_spaces, unescape_html)


class RSS10Feed(Feed):
  __feed__ = 'RSS 1.0'

  @property
  def channel(self):
    return getattr(self._element, '{http://purl.org/rss/1.0/}channel', None)

  @property
  def is_valid(self):
    return (self._element.tag == '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF' and
            self.channel is not None)

  @property
  def id(self):
    return safe_strip(get_attribute(self._element,
                                    '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about'))

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
    return None

  @property
  def updated(self):
    return None

  @property
  def entries(self):
    node_name = '{http://purl.org/rss/1.0/}item'
    return [RSS10Item(item) for item in self._element.iterchildren(tag=node_name)]


class RSS10Item(Item):

  @property
  def id(self):
    return safe_strip(get_attribute(self._element,
                                    '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about'))

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
    text = get_descendant_text(self._element,
                               '{http://purl.org/rss/1.0/modules/content/}encoded')
    if text is None:
      text = get_descendant_text(self._element,
                                 '{http://purl.org/rss/1.0/}description')
    return text

  @property
  def published(self):
    return get_descendant_datetime(self._element, '{http://purl.org/dc/elements/1.1/}date')

  @property
  def updated(self):
    return None
