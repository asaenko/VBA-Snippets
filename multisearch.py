#!/usr/bin/env python3

import sys
import webbrowser

class multiSearch(object):
    def __init__(self, flag, query):
        self.flag = flag
        self.query = query
        self.commands = dict(Google=r'https://www.google.ru/search?q=%22{query}%22',
                             Proz=r'http://www.proz.com/search/?term={query}&from=rus&to=eng&es=1',
                             Linguee=r'http://www.linguee.com/english-russian/search?query={query}',
                             LingueeDeEn=r'http://www.linguee.de/deutsch-englisch/search?source=auto&query={query}',
                             LingueeRuEn=r'http://www.linguee.ru/русский-английский/search?source=auto&query={query}',
                             LingueeEsEn=r'http://www.linguee.com/english-spanish/search?source=spanish&query={query}',
                             LingueeFrEn=r'http://www.linguee.fr/francais-anglais/search?source=auto&query={query}',
                             Lingvo=r'http://forum.lingvo.ru/actualsearch.aspx?search={query}&st=t&a=&ma=0&bid=0&dt=-1&s=1&so=1',
                             Translatorscafe=r'http://www.translatorscafe.com/tcterms/en-US/?q={query}&lnsr=42&lntr=129&spec=0&diff=255',
                             StackOverflow=r'https://stackoverflow.com/search?q={query}',
                             Duckduckgo=r'https://duckduckgo.com/?q={query}&ia=meanings',
                             GoogleTr=r'https://translate.google.ru/?hl=en&tab=wT#auto/en/{query}')

    def search(self):
        webbrowser.open(self.commands[self.flag].format(query=self.query))


if __name__ == '__main__':
    flag = sys.argv[1]
    query = ' '.join(sys.argv[2:])
    searchInst = multiSearch(flag, query)
    searchInst.search()

