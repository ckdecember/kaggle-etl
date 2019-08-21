#!/usr/bin/env python
# coding: utf-8

"""
Web Scraper Module
Pull data from kaggle
Use pycurl???  or not

"""

import argparse
from io import BytesIO
import logging
import os

from bs4 import BeautifulSoup, SoupStrainer
from dotenv import load_dotenv
import pycurl

load_dotenv()

class WebScrape():
    def __init__(self):
        self.encoding = 'UTF-8'

    def get_url(self, host_url):
        """ reads the url given """
        c = pycurl.Curl()
        c.setopt(c.URL, host_url)
        c.setopt(pycurl.TIMEOUT, 10)
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        c.setopt(pycurl.SSL_VERIFYPEER, 0);
        #c.perform()
        session = c
        return session

    def readpage(self, page_request):
        # read the webpage dom for this token
        # input name=X-XSRF-TOKEN
        # use bs4 to read a little bit.  get the token tag.  refeed tag.
        soup = BeautifulSoup(page_request, features="html.parser", from_encoding=self.encoding)
        return soup

    def readstuff(self):
        pass
        user = os.environ['USERNAME']
        password = os.environ['PASSWORD']
        c.setopt(pycurl.POSTFIELDS, 'username={}&password={}'.format(user, password))
        #c.setopt(pycurl.COOKIEJAR, 'data/kaggle.cookie')
        # c.setopt(c.VERBOSE, True)
        c.setopt(pycurl.SSL_VERIFYPEER, 0);
        session = c
        return session

def main():
    print ("Web Scraper Module")
    ws = WebScrape()
    session = ws.get_url("https://www.kaggle.com/account/login?phase=emailSignIn&returnUrl=%2Fwendykan%2Flending-club-loan-data%2Fversion%2F1")
    print (session)
    buffer = session.perform_rb()
    print (buffer)
    soup = ws.readpage(buffer)
    logging.debug(soup)



if __name__ == "__main__":
    main()