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

def _fill_forms(item_name):
    '''
    input: item name - str
    output: html site - str'''

    br = mechanize.Browser()
    try:
        br.open('http://allegro.pl/')
    except URLError:
        raise NoConnectionError

    br.select_form(nr = 0)
    br['string'] = item_name
    br.submit()
    try:
        br.select_form(nr = 1)
    except mechanize._mechanize.FormNotFoundError:
        raise NoItemException('No items found for this search phrase..')
    br['offerTypeBuyNow'] = ['1']
    br['standard_allegro'] = ['1']
    br['startingTime'] = ['']
    br['endingTime'] = ['']
    br['shippingTime'] = ['']
    br.submit()
    return br.response().read()

def _convert_price_to_float(str_price):
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


def allegro_api(item_name):
    '''function that does the job '''

    site = _fill_forms(item_name)
    soup = BeautifulSoup(site)
    item = soup.find('article', attrs={'class': 'offer'})
    if item is None:
        raise NoItemException('No items found for this search phrase..')
    link = 'http://allegro.pl' + item.find('a')['href']
    price = item.find('span', attrs={'class': 'buy-now dist'}).contents[2]

    return link, _convert_price_to_float(price)