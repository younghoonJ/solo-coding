from urllib.request import urlopen
import os
import six
import tempfile


class UrlExtractor:
    """Extract Url from html page"""

    def __init__(self, html_file=None, web_url=None):
        self.html_file = html_file
        self.web_url = web_url
        self.data = None
        self.urls = []

    def get_from_file(self):
        fp = open(self.html_file, 'r')
        self.data = fp.read()
        fp.close()

    def get_from_web(self):
        fp = urlopen(self.web_url)
        self.data = six.text_type(fp.read())  # bytes
        fp.close()

    def extract_string(self, line, s, e):
        try:
            return line[line.index(s):line.index(e) + len(e)]
        except Exception:
            return None

    def extract(self, _start, _end):
        """ Extract Url starts with _starts and end with _end."""
        if not self.urls:
            for line in self.data.split('<a href="'):
                s = self.extract_string(line, _start, _end)
                if s is not None:
                    self.urls.append(s)
        return self.urls
