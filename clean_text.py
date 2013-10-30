#!/usr/bin/env python 
""" clean_text.py
Used for cleaning text so that it will be able to upload to transifex.
"""

import unicodedata
import sys

def normalize_text(text):
    return unicodedata.normalize('NFKD', text.decode('latin-1')).encode('ascii', 'ignore')

def usage():
    print 'Usage'
    print 'python clean_text.py [filename]'

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print 'Cleaning text for ' + sys.argv[1]
        f = open(sys.argv[1], 'r+')
        data = f.read()
        new_data = normalize_text(data)
        f.write(new_data)
        f.close()
        print 'Done.'
    else:
        usage()
