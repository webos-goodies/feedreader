# -*- encoding: utf-8; -*-

import sys
import os
import urllib2
import traceback

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from feedreader.parser import from_string

def main():
  if len(sys.argv) < 2:
    sys.stderr.write("Usage : parse_http.py <url>\n")
    sys.exit(1)

  response = urllib2.urlopen(sys.argv[1])
  body = response.read()

  print repr(from_string(body))


if __name__ == '__main__':
  main()
