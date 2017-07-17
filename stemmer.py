'''
Command-line script to use the termBaseClass terms stemming functionality
The input file has to be bilingual
'''

import os
import sys
import optparse
from termBaseClass import *

def main():
    parser = optparse.OptionParser("usage: %prog "+ "-l <language> -m <mode> \
-e <encoding> filename")
    parser.add_option('-l', '--language', dest='lang', default='en',\
                      type='string', help="Enter language: en, ru, de")
    parser.add_option('-m', '--mode', dest="mode", default='stem',\
                      type='string', help='stem OR unstem')
    parser.add_option('-e', '--encoding', dest='encoding', default='utf16',\
                      type='string', help="Enter encoding, e.g. utf8, utf16, utf16be...")
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("No file name was specified")
        raise SystemExit(0)

    lang = options.lang
    mode = options.mode
    encoding = options.encoding
    filename = args[0]

    if not os.path.exists(filename):
        sys.stderr.write("File not found")
        raise SystemExit(1)

    tb = termBase(filename, encoding)
    if mode == 'stem':
        tb.stemTerms(lang)
    elif mode == 'unstem':
        tb.unstemTerms()

if __name__ == '__main__':
    main()
