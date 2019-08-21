#!/usr/bin/env python
# coding: utf-8

"""
Web Scraper Module
Pull data from kaggle
Use pycurl???  or not

"""
import zlib

import zipfile

class data_handler:
    def stream_gzip_decompress(self, stream):
        dec = zlib.decompressobj(32 + zlib.MAX_WBITS)  # offset 32 to skip the header
        #for chunk in stream:
        #    rv = dec.decompress(chunk)
        #    if rv:
        #        yield rv

def main():
    dh = data_handler()

    with zipfile.ZipFile("data/loan.csv.zip") as myzipfh:
        with myzipfh.open('loan.csv') as fh:
            print(fh.readline())

if __name__ == "__main__":
    main()