#!/usr/bin/env python
# coding: utf-8

"""
Web Scraper Module
Pull data from kaggle
Use pycurl???  or not

"""

import argparse
import itertools
import json
import logging
import time
import urllib.request
import urllib.parse

import pycurl

class WebScrape():
    def readurl(self, host_url):
        c = pycurl.Curl()
        c.setopt(c.URL, host_url)
        c.setopt(pycurl.TIMEOUT, 10)

        c.setopt(pycurl.FOLLOWLOCATION, 1)
        #c.setopt(pycurl.POSTFIELDS, 'username={user}&password={password}'.format(**host_login))
        # X-XSRF-TOKEN
        #c.setopt(pycurl.COOKIEJAR, 'data/kaggle.cookie')

        # c.setopt(c.VERBOSE, True)

        c.setopt(pycurl.SSL_VERIFYPEER, 0);
        session = c
        return session

def main():
    print ("Web Scraper Module")
    ws = WebScrape()
    session = ws.readurl("https://www.kaggle.com/account/login?phase=emailSignIn&returnUrl=%2Fwendykan%2Flending-club-loan-data%2Fversion%2F1")
    print (session)
    session.perform()

if __name__ == "__main__":
    main()