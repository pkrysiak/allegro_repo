# -*- coding:UTF-8 -*-
import unittest,mechanize
from allegro import lib
from mock import patch,MagicMock
from html import *

class AllegroTests(unittest.TestCase):

    def setUp(self):
        self.search_phrase = 'laptop'

    def tearDown(self):
        self.search_phrase = None

    @patch('allegro.lib.mechanize.Browser')
    def test_succesfull_link(self, Browser):
        mechanize.Browser().response().read.return_value = html
        link , _ = lib.allegro_api(self.search_phrase)
        print link

