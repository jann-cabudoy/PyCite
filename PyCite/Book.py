from Citation import Citation 


class BookCitation(Citation):
    """description of class"""

    def __init__(self, authlast, authfirst, title, pubyear, pub, city, state):
        Citation.__init__(self, authlast, authfirst, title, pubyear)
        self.pub = str(pub)
        self.city = str(city)
        self.state = str(state)

    def getpub(self):
        return self.pub

    def getcity(self):
        return self.city

    def getstate(self):
        return self.state

