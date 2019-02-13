from Citation import Citation

class MagazineCitation(Citation):
    """description of class"""

    def __init__(self, authlast, authfirst, title, pubyear, mtitle, issue, pgbeg, pgend):
        Citation.__init__(self, authlast, authfirst, title, pubyear)
        self.mtitle = mtitle
        self.issue = issue
        self.pgbeg = pgbeg
        self.pgend = pgend

    def getmtitle(self):
        return self.mtitle

    def getissue(self):
        return self.issue

    def getpgbeg(self):
        return self.pgbeg

    def getpgend(self):
        return self.pgend



