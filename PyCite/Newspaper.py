from Citation import Citation

class NewspaperCitation(Citation):
    """description of class"""

    #Args passed into class are StringVar, so must use .get() to get an actual string
    def __init__(self, authlast, authfirst, title, pubyear, ntitle, pgbeg, pgend):
        Citation.__init__(self, authlast, authfirst, title, pubyear)
        self.ntitle = ntitle.get()
        self.pgbeg = pgbeg.get()
        self.pgend = pgend.get()

    def getntitle(self):
        return self.ntitle
    
    def getpgbeg(self):
        return self.pgbeg

    def getpgend(self):
        return self.end

