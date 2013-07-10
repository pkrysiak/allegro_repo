# -*- coding:UTF-8 -*-
import unittest
from mock import patch,Mock
from allegro import lib
from html import html,html_link,html_price
from urllib2 import URLError

class AllegroTests(unittest.TestCase):

    def setUp(self):
        self.search_phrase = 'laptop'
        self.search_price = 3229.0

    def tearDown(self):
        self.search_phrase = None
        self.search_price = None

    @patch('allegro.lib.mechanize.Browser')
    def test_succesfull_link(self, Browser):
        Browser().response().read.return_value = html
        link , _ = lib.allegro_api(self.search_phrase)
        self.assertEqual(link, html_link)

    @patch('allegro.lib.mechanize.Browser')
    def test_successfull_price(self, Browser):
        Browser().response().read.return_value = html
        _ , price = lib.allegro_api(self.search_phrase)
        self.assertEqual(price, self.search_price)

    @patch('allegro.lib.mechanize.Browser')
    def test_no_connection_error(self, Browser):
        Browser().open.side_effect = URLError('NoConnection..')
        self.assertRaises(lib.NoConnectionError, lib.allegro_api, self.search_phrase)

    def test_no_item_error(self):
        self.assertRaises(lib.NoItemException, lib.allegro_api, 'konstantynopolitańczykowianeczka')

    def test_convert_price_to_float_fail(self):
        for not_price in [1, ' ', ',', '', 'acsd,)']:
            self.assertRaises(lib.PriceConversionException, lib._convert_price_to_float, not_price)

    def test_convert_price_to_float_success(self):
        for input_price, result_price in [('0', 0), ('29,99', 29.99), ('2 129,84', 2129.84)]:
            self.assertEqual(result_price, lib._convert_price_to_float(input_price))