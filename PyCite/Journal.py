from Citation import *

class JournalCitation(Citation):
    """description of class"""

    def __init__(self, authlast, authfirst, title, pubyear, issue, jname, pgbeg, pgend):
        Citation.__init__(self, authlast, authfirst, title, pubyear)
        self.issue = issue
        self.jname = jname
        self.pgbeg = pgbeg
        self.pgend = pgend

    def getissue(self):
        return self.issue

    def getjname(self):
        return self.jname

    def getpgbeg(self):
        return self.pgbeg

    def getpgend(self):
        return self.pgend
