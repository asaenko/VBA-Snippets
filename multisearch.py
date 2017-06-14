import sys
import webbrowser

class multiSearch(object):
    def __init__(self, flag, query):
        self.flag = flag
        self.query = query
        self.commands = {'-g': 'self.google()'}

    def google(self):
        webbrowser.open('https://www.google.ru/search?q=%22' + self.query + '%22')

    def search(self):
        eval(self.commands[self.flag])

if __name__ == '__main__':
    flag = sys.argv[1]
    query = ' '.join(sys.argv[2:])
    searchInst = multiSearch(flag, query)
    searchInst.search()
