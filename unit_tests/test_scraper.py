#!/usr/bin/env python
# coding: utf-8

"""
Unit Tests

"""

import unittest

import pycurl

from scraper import WebScrape


class TestScraper(unittest.TestCase):
    """ Basic Unit Test Scraper"""

    def test_scraper(self):
        ws = WebScrape()
        session = ws.get_url("https://www.google.com")
        self.assertIs(pycurl.Curl, type(session))


if __name__ == "__main__":
    unittest.main()
