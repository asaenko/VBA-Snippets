#!/usr/bin/env python3
#TODO: add linguee, reverso, lingvo, stackoverflow, duckduckgo

import sys
import webbrowser

class multiSearch(object):
    def __init__(self, flag, query):
        self.flag = flag
        self.query = query
        self.commands = {'-g': 'https://www.google.ru/search?q=%22{}%22', '-p': 'http://www.proz.com/search/?term={}&from=rus&to=eng&es=1'}

    #TODO: replace functions with links in the commands dictionary
    def google(self):
        webbrowser.open('https://www.google.ru/search?q=%22' + self.query + '%22')

    def proz(self):
        webbrowser.open('http://www.proz.com/search/?term=' + self.query + '&from=rus&to=eng&es=1')


    def search(self):
#        eval(self.commands[self.flag])
        webbrowser.open(self.flag.format(self.query))

if __name__ == '__main__':
    flag = sys.argv[1]
    query = ' '.join(sys.argv[2:])
    searchInst = multiSearch(flag, query)
    searchInst.search()
