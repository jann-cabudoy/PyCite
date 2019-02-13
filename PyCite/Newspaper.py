from Citation import *

class NewspaperCitation(Citation):
    """description of class"""

    def __init__(self, authlast, authfirst, title, pubyear, ntitle, pgbeg, pgend):
        Citation.__init__(self, authlast, authfirst, title, pubyear)
        self.ntitle = ntitle
        self.pgbeg = pgbeg
        self.pgend = pgend

    def getntitle(self):
        return self.ntitle
    
    def getpgbeg(self):
        return self.pgbeg

    def getpgend(self):
        return self.end

