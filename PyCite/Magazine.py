from Citation import Citation

class MagazineCitation(Citation):
    """description of class"""

    #Args passed into class are StringVar, so must use .get() to get an actual string
    def __init__(self, authlast, authfirst, title, pubyear, mtitle, issue, pgbeg, pgend):
        Citation.__init__(self, authlast, authfirst, title, pubyear)
        self.mtitle = mtitle.get()
        self.issue = issue.get()
        self.pgbeg = pgbeg.get()
        self.pgend = pgend.get()

    def getmtitle(self):
        return self.mtitle

    def getissue(self):
        return self.issue

    def getpgbeg(self):
        return self.pgbeg

    def getpgend(self):
        return self.pgend



