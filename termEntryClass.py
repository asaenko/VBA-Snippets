'''
Term entry class for use in termbase class
'''

import codecs
import os


class termEntry(object):
    def __init__(self, src_term, trg_term, comment=''):
        self.src_term = src_term
        self.trg_term = list(trg_term.split(';'))
        self.comment = comment

    def __str__(self):
        if self.comment:
            return '{src}\t{trg}\t{comm}\r\n'.format\
            (src=self.src_term, trg=';'.join(self.trg_term), comm=self.comment)
        else:
            return '{src}\t{trg}\r\n'.format\
            (src=self.src_term, trg=';'.join(self.trg_term))

    def changeSource(self, new_term):
        self.src_term = new_term

    def changeTarget(self, new_term):
        self.trg_term = list(new_term.split(';'))

    def replaceTargetTerm(self, old_term, new_term):
        if old_term in self.trg_term:
            pos = self.trg_term.index(old_term)
            del(self.trg_term[pos])
            self.trg_term.insert(pos, new_term)
        else:
            print('Term not found')

    def removeTargetTerm(self, trg_term):
        if trg_term in self.trg_term:
            self.trg_term.remove(trg_term)
        else:
            print('Term not found')

    def addTargetTerm(self, new_term):
        self.trg_term.extend(new_term.split(';'))

    def addComment(self, comment):
        self.comment = comment

    def removeComment(self):
        self.comment = ''

    def getSource(self):
        return self.src_term

    def getTarget(self):
        return self.trg_term

    def getComment(self):
        return self.comment

        
if __name__ == '__main__':
    pass
