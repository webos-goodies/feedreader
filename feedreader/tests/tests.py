# -*- encoding: utf-8; -*-

import itertools
import sys
import os
import os.path
import unittest
import traceback

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from feedreader.parser import from_string

DIR = os.path.abspath(os.path.dirname(__file__))

from rss_files import RSS_FILES
from atom_files import ATOM_FILES
from rssone_files import RSS10_FILES
from rssnine_files import RSS091_FILES

ATTRIBUTES = ('author_name', 'author_link', 'author_email',
              'title', 'link', 'description', 'id', 'published', 'pudated')

def from_file(fp):
  str = fp.read()
  return from_string(str)

class RSSTestCase(unittest.TestCase):
  def testParsing(self):
    for fname, test_data in RSS_FILES:
      fp = open(os.path.join(DIR, fname), 'r')
      parsed = from_file(fp)
      if fname == 'rss/googlegroups.xml':
        self.assertEquals(parsed.feed, 'RSS 2.0 Fallback')
      else:
        self.assertEquals(parsed.feed, 'RSS 2.0')
      self.assertEquals(parsed.title, test_data['title'])
      self.assertEquals(parsed.link, test_data['link'])
      self.assertEquals(parsed.description, test_data['description'])
      # Test the first one:
      for entry, test_req in itertools.izip(parsed.entries[:len(test_data['entries'])], test_data['entries']):
        for field in ATTRIBUTES:
          if field in test_req:
            self.assertEquals(getattr(entry, field), test_req[field])


class AtomTestCase(unittest.TestCase):
  def testParsing(self):
    for fname, test_data in ATOM_FILES:
      fp = open(os.path.join(DIR, fname), 'r')
      parsed = from_file(fp)
      if fname == 'atom/fallback.xml':
        self.assertEquals(parsed.feed, 'Atom Fallback')
      elif fname == 'atom/atom03.xml':
        self.assertEquals(parsed.feed, 'Atom 0.3')
      else:
        self.assertEquals(parsed.feed, 'Atom 1.0')
      self.assertEquals(parsed.title, test_data['title'])
      self.assertEquals(parsed.link, test_data['link'])
      self.assertEquals(parsed.description, test_data['description'])
      # Test the first one:
      for entry, test_req in itertools.izip(parsed.entries[:len(test_data['entries'])], test_data['entries']):
        for field in ATTRIBUTES:
          if field in test_req:
            self.assertEquals(getattr(entry, field), test_req[field])


class RSS10TestCase(unittest.TestCase):
  def testParsing(self):
    for fname, test_data in RSS10_FILES:
      fp = open(os.path.join(DIR, fname), 'r')
      parsed = from_file(fp)
      if fname == 'rssone/fallback.xml':
        self.assertEquals(parsed.feed, 'RSS 1.0 Fallback')
      else:
        self.assertEquals(parsed.feed, 'RSS 1.0')
      self.assertEquals(parsed.title, test_data['title'])
      self.assertEquals(parsed.link, test_data['link'])
      self.assertEquals(parsed.description, test_data['description'])
      # Test the first one:
      for entry, test_req in itertools.izip(parsed.entries[:len(test_data['entries'])], test_data['entries']):
        for field in ATTRIBUTES:
          if field in test_req:
            self.assertEquals(getattr(entry, field), test_req[field])

class RSS091TestCase(unittest.TestCase):
  def testParsing(self):
    for fname, test_data in RSS091_FILES:
      fp = open(os.path.join(DIR, fname), 'r')
      parsed = from_file(fp)
      if fname == 'rssnine/fallback.xml':
        self.assertEquals(parsed.feed, 'RSS 0.91 Fallback')
      else:
        self.assertEquals(parsed.feed, 'RSS 0.91')
      self.assertEquals(parsed.title, test_data['title'])
      self.assertEquals(parsed.link, test_data['link'])
      self.assertEquals(parsed.description, test_data['description'])
      # Test the first one:
      for entry, test_req in itertools.izip(parsed.entries[:len(test_data['entries'])], test_data['entries']):
        for field in ATTRIBUTES:
          if field in test_req:
            self.assertEquals(getattr(entry, field), test_req[field])

class InvalidFeedsTestCase(unittest.TestCase):
  def testParsing(self):
    dirname = os.path.join(DIR, 'invalid_feeds')
    for fname in os.listdir(dirname):
      try:
        fp = open(os.path.join(dirname, fname), 'r')
        parsed = from_file(fp)
        self.assertTrue(parsed.title)
        entries = parsed.entries
        self.assertTrue(len(entries) > 0)
        for entry in entries:
          if fname not in ('madrigale.xml', 'mew5.xml'):
            self.assertTrue(entry.title)
          self.assertTrue(entry.link)
          if fname != 'fc2.xml':
            self.assertTrue(entry.description, fname)
      except Exception as e:
        print "\nFile: %s\nException: %s\n%s\n" % (fname, type(e), e.message)
        traceback.print_exc()

if __name__ == '__main__':
    unittest.main()
