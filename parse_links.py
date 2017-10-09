#!/usr/bin/env python

from html.parser import HTMLParser
from io import StringIO
from urllib.request import urlopen
from urllib.parse import urljoin

from bs4 import BeautifulSoup, SoupStrainer

URLs = (
    'http://python.org',
    'http://baidu.com',
)


def output(x):
    print('\n'.join(sorted(set(x))))


def simpleBS(url, f):
    output(urljoin(url, x['href']) for x in BeautifulSoup(
        f).find_all('a'))


def fasterBS(url, f):
    output(urljoin(url, x['href']) for x in BeautifulSoup(
        f, parse_only=SoupStrainer('a')))


def htmlparser(url, f):
    class AnchorParser(HTMLParser):

        def handle_startendtag(self, tag, attrs):
            if tag != 'a':
                return
            if not hasattr(self, 'data'):
                self.data = []
            for attr in attrs:
                if attr[0] == 'href':
                    self.data.append(attr[1])
    parser = AnchorParser()
    parser.feed(f.read())
    parser.close()
    output(urljoin(url, x) for x in parser.data)


def process(url, data):
    print('\n*** simple BS')
    simpleBS(url, data)
    data.seek(0)
    print('\n*** faster BS')
    fasterBS(url, data)
    data.seek(0)
    print('\n*** HTMLParser')
    htmlparser(url, data)
    data.seek(0)


def main():
    for url in URLs:
        f = urlopen(url)
        data = StringIO(f.read().decode())
        f.close()
        process(url, data)


if __name__ == '__main__':
    main()
