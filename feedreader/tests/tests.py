import itertools
import os.path
import unittest2

from feedreader.parser import from_file

DIR = os.path.abspath(os.path.dirname(__file__))

from rss_files import RSS_FILES
from atom_files import ATOM_FILES
from rssone_files import RSS10_FILES
from rssnine_files import RSS091_FILES

ATTRIBUTES = ('author_name', 'author_link', 'author_email',
              'title', 'link', 'description', 'id', 'published', 'pudated')


class RSSTestCase(unittest2.TestCase):
  def testParsing(self):
    for fname, test_data in RSS_FILES:
      fp = open(os.path.join(DIR, fname), 'r')
      parsed = from_file(fp)

      self.assertEquals(parsed.feed, 'RSS 2.0')
      self.assertEquals(parsed.title, test_data['title'])
      self.assertEquals(parsed.link, test_data['link'])
      self.assertEquals(parsed.description, test_data['description'])
      # Test the first one:
      for entry, test_req in itertools.izip(parsed.entries[:len(test_data['entries'])], test_data['entries']):
        for field in ATTRIBUTES:
          if field in test_req:
            self.assertEquals(getattr(entry, field), test_req[field])


class AtomTestCase(unittest2.TestCase):
  def testParsing(self):
    for fname, test_data in ATOM_FILES:
      fp = open(os.path.join(DIR, fname), 'r')
      parsed = from_file(fp)
      if fname != 'atom/atom03.xml':
        self.assertEquals(parsed.feed, 'Atom 1.0')
      else:
        self.assertEquals(parsed.feed, 'Atom 0.3')
      self.assertEquals(parsed.title, test_data['title'])
      self.assertEquals(parsed.link, test_data['link'])
      self.assertEquals(parsed.description, test_data['description'])
      # Test the first one:
      for entry, test_req in itertools.izip(parsed.entries[:len(test_data['entries'])], test_data['entries']):
        for field in ATTRIBUTES:
          if field in test_req:
            self.assertEquals(getattr(entry, field), test_req[field])


class RSS10TestCase(unittest2.TestCase):
  def testParsing(self):
    for fname, test_data in RSS10_FILES:
      fp = open(os.path.join(DIR, fname), 'r')
      parsed = from_file(fp)
      self.assertEquals(parsed.feed, 'RSS 1.0')
      self.assertEquals(parsed.title, test_data['title'])
      self.assertEquals(parsed.link, test_data['link'])
      self.assertEquals(parsed.description, test_data['description'])
      # Test the first one:
      for entry, test_req in itertools.izip(parsed.entries[:len(test_data['entries'])], test_data['entries']):
        for field in ATTRIBUTES:
          if field in test_req:
            self.assertEquals(getattr(entry, field), test_req[field])

class RSS091TestCase(unittest2.TestCase):
  def testParsing(self):
    for fname, test_data in RSS091_FILES:
      fp = open(os.path.join(DIR, fname), 'r')
      parsed = from_file(fp)
      self.assertEquals(parsed.feed, 'RSS 0.91')
      self.assertEquals(parsed.title, test_data['title'])
      self.assertEquals(parsed.link, test_data['link'])
      self.assertEquals(parsed.description, test_data['description'])
      # Test the first one:
      for entry, test_req in itertools.izip(parsed.entries[:len(test_data['entries'])], test_data['entries']):
        for field in ATTRIBUTES:
          if field in test_req:
            self.assertEquals(getattr(entry, field), test_req[field])

if __name__ == '__main__':
    unittest2.main()
