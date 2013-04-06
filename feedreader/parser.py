import lxml.objectify
import httplib
import urlparse

__all__ = ('ParseError', 'InvalidFeed', 'from_string', 'from_url', 'from_file')

# TODO: change the feeds to a registration model
from feeds.atom10 import Atom10Feed
from feeds.atom03 import Atom03Feed
from feeds.rss20 import RSS20Feed
from feeds.rss10 import RSS10Feed

feeds = (Atom10Feed, RSS20Feed, RSS10Feed, Atom03Feed)

ACCEPT_HEADER = "application/atom+xml,application/rdf+xml,application/rss+xml,application/x-netcdf,application/xml;q=0.9,text/xml;q=0.2,*/*;q=0.1"

USER_AGENT = 'py-feedreader'

class InvalidFeed(Exception): pass
class ParseError(Exception): pass

def _from_parsed(parsed):
    for feed in feeds:
        result = feed(parsed)
        if result.is_valid:
            return result
    raise InvalidFeed(parsed.tag)

def from_string(data, *args, **kwargs):
    parsed = lxml.objectify.fromstring(data, *args, **kwargs)
    return _from_parsed(parsed)

def from_file(fp, *args, **kwargs):
    parsed = lxml.objectify.parse(fp, **kwargs).getroot()
    return _from_parsed(parsed)

def from_url(url, **kwargs):
    url = urlparse.urlparse(url)
    if url.scheme == 'https':
        conn = httplib.HTTPSConnection
    elif url.scheme == 'http':
        conn = httplib.HTTPConnection
    else:
        raise NotImplementedError
    
    base_url = '%s://%s' % (url.scheme, url.hostname)
    
    headers = {
        'User-Agent': USER_AGENT,
        'Accept': ACCEPT_HEADER,
    }
    connection = conn(url.hostname)
    method = kwargs.pop('method', 'GET').upper()
    if method == 'GET':
        path, query = url.path, ''
        if url.query:
            path += '?' + url.query
    else:
        path, query = url.path, url.query
    connection.request(method, path, query, headers)
    try:
        response = connection.getresponse()
    except httplib.BadStatusLine, exc:
        raise ParseError('Bad status line: %s' % (exc,))
    
    if response.status != 200:
        if response.status in (301, 302):
            return from_url(response.getheader('location'), **kwargs)
        raise ParseError('%s %s' % (response.status, response.reason))

    return from_file(response, base_url=base_url)
