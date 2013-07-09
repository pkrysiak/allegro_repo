# -*- coding: UTF-8 -*-
import mechanize,webbrowser
from urllib2 import urlopen,URLError
from bs4 import BeautifulSoup

class NoItemException(Exception):
    pass

class PriceConversionException(Exception):
    pass

class NoConnectionError(Exception):
    pass


def open_in_browser(link):
    '''
    input: link - str
    output: None'''
    webbrowser.open_new_tab(link)

def fill_forms(item_name):
    '''
    input: item name - str
    output: html site - str'''

    br = mechanize.Browser()
    try:
        br.open('http://allegro.pl/')
    except URLError:
        raise NoConnectionError

    br.select_form(nr = 0)
    br['string'] = 'laptop'
    br.submit()

    br.select_form(nr = 1)
    br['offerTypeBuyNow'] = ['1']
    br['standard_allegro'] = ['1']
    br['startingTime'] = ['']
    br['endingTime'] = ['']
    br['shippingTime'] = ['']
    br.submit()
    return br.response().read()

def get_linklist(html):
    '''
    input: html - str
    output: list of subject links'''
    link_list = []
    soup = BeautifulSoup(html)
    a = soup.findAll('h2')
    for i in a:
        h = BeautifulSoup(str(i))
        a = h.find('a')
        if a != None:
            link_list.append('http://allegro.pl'+ a['href'])
    return link_list[1:]


def get_item_price(site):
    '''
    input: site - string
    output: price - string'''

    b = BeautifulSoup(site)
    c =  b.find('span',attrs={'class':'buy-now dist'})
    return c.contents[2].strip()

def convert_price_to_float(str_price):
    '''
    input: price - unicode
    output: price - float'''
    try:
        str(str_price)
        price = str_price.replace(' ','')
        price = price.replace(',','.')
        return float(price)
    except (AttributeError, ValueError):
        raise PriceConversionException("Can't convert price..")



def allegro_api(item_name = 'laptop', browser_mode = False):
    '''function that does the job '''

    site = fill_forms(item_name)

    links = get_linklist(site)
    price = convert_price_to_float( get_item_price(site) )

    if browser_mode:
        open_in_browser(links[0])

    return links[0],price
