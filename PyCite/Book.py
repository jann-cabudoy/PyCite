from Citation import *

class BookCitation(Citation):
    """description of class"""

    def __init__(self, authlast, authfirst, title, pubyear, pub, city, state):
        Citation.__init__(self, authlast, authfirst, title, pubyear)
        self.pub = pub
        self.city = city
        self.state = state

    def getpub(self):
        return self.pub

    def getcity(self):
        return self.city

    def getstate(self):
        return self.state

