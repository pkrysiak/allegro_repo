# -*- coding:UTF-8 -*-
import unittest
from mock import patch,MagicMock
from allegro import lib
from html import *

class AllegroTests(unittest.TestCase):

    def setUp(self):
        self.search_phrase = 'laptop'

    def tearDown(self):
        self.search_phrase = None

    @patch('allegro.lib.mechanize.Browser')
    def test_succesfull_link(self, Browser):
        Browser.response().read.return_value = html
        # import ipdb; ipdb.set_trace()
        link , _ =lib.allegro_api(self.search_phrase)
        print link

