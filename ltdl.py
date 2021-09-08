#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import time

'''
Extract the title from a web page using
the standard lib.
'''

from html.parser import HTMLParser
from urllib.request import urlopen
import urllib

def error_callback(*_, **__):
    pass

def is_string(data):
    return isinstance(data, str)

def is_bytes(data):
    return isinstance(data, bytes)

def to_utf8(data):
    if is_string(data):
        data = data.encode('utf-8', errors='ignore')
    elif is_bytes(data):
        data = data.decode('utf-8', errors='ignore')
    else:
        data = str(data).encode('utf-8', errors='ignore')
    return data


class Parser(HTMLParser):
    def __init__(self, url):
        self.title = None
        self.rec = False
        HTMLParser.__init__(self)
        try:
            self.feed(to_utf8(urlopen(url).read()))
        except urllib.error.HTTPError:
            return
        except urllib.error.URLError:
            return
        except ValueError:
            return

        self.rec = False
        self.error = error_callback

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.rec = True

    def handle_data(self, data):
        if self.rec:
            self.title = data

    def handle_endtag(self, tag):
        if tag == 'title':
            self.rec = False


def get_title(url):
    return Parser(url).title

# Method 2
from urllib.request import urlopen
from lxml.html import parse

#url = "https://www.google.com"
#page = urlopen(line)
#p = parse(page)
#p.find(".//title").text


# Method 3
import requests
hearders = {'headers':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'}
#n = requests.get(line , headers=hearders)
#al = n.text
#title = al[al.find('<title>') + 7 : al.find('</title>')]

# Method 4
from bs4 import BeautifulSoup
#soup = BeautifulSoup(urllib.request.urlopen("https://www.google.com"))
#print (soup.title.string)

import html

def get_title_method1(url):
    # Method 1
    title = get_title(url)
    if title is None:
        raise ValueError("Must be str, not NoneType")
    return title

def get_title_method2(url):
    # Method 2 DEPRECATED (Unable to encode japanese or chinese characters properly)
    page = urlopen(url)
    p = parse(page)
    title = p.find(".//title").text
    if title is None:
        raise ValueError("Must be str, not NoneType")
    #return title

def get_title_method3(url):
    n = requests.get(url , headers=hearders)
    al = n.text
    title = al[al.find('<title>') + 7 : al.find('</title>')]
    if title is None:
        raise ValueError("Must be str, not NoneType")
    return html.unescape(title)

def get_title_method4(url):
    # Method 4
    # Takes Longer but works better for reddit.com
    soup = BeautifulSoup(urllib.request.urlopen(url), features="lxml")
    title = soup.title.string
    if title is None:
        raise ValueError("Must be str, not NoneType")
    return title

def get_title_reddit_link(url):
    # Tries methods 4,3,1 in that order, to get title of url webpage.
    # Returns title or url itself if HTTP Error
    try:
        return get_title_method4(url)
    except:
        pass
    try:
        return get_title_method3(url)
    except:
        pass
    try:
        return get_title_method1(url)
    except:
        return url

def get_title_default(url):
    # Tries methods 3,4,1 in that order, to get title of url webpage.
    # Returns title or url itself if HTTP Error
    try:
        return get_title_method3(url)
    except:
        pass
    try:
        return get_title_method4(url)
    except:
        pass
    try:
        return get_title_method1(url)
    except:
        return url

def get_title_all_methods(url):
    if ("reddit.com" in url):
        return get_title_reddit_link(url)
    else:
        return get_title_default(url)
