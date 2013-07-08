# -*- coding:UTF-8 -*-
import unittest
from mock import patch,MagicMock
from allegro import lib
from html import *
from urllib2 import URLError
class AllegroTests(unittest.TestCase):

    def setUp(self):
        self.search_phrase = 'laptop'

    def tearDown(self):
        self.search_phrase = None

    @patch('allegro.lib.mechanize.Browser')
    def test_succesfull_link(self, Browser):
        Browser().response().read.return_value = html
        link , _ =lib.allegro_api(self.search_phrase)
        self.assertEqual(link, html_link)

    @patch('allegro.lib.mechanize.Browser')
    def test_successfull_price(self, Browser):
        Browser().response().read.return_value = html
        _ , price = lib.allegro_api(self.search_phrase)
        self.assertEqual(price, lib.convert_price_to_float(html_price))

    def test_convert_price_to_float(self):
        l = [1,' ',',','','acsd,)']
        for elem in l:
            self.assertRaises(lib.PriceConversionException, lib.convert_price_to_float, elem)
