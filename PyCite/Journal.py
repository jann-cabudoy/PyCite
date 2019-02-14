from Citation import Citation

class JournalCitation(Citation):
    """description of class"""
   
    #Args passed into class are StringVar, so must use .get() to get an actual string
    def __init__(self, authlast, authfirst, title, pubyear, issue, jname, pgbeg, pgend):
        Citation.__init__(self, authlast, authfirst, title, pubyear)
        self.issue = issue.get()
        self.jname = jname.get()
        self.pgbeg = pgbeg.get()
        self.pgend = pgend.get()

    def getissue(self):
        return self.issue

    def getjname(self):
        return self.jname

    def getpgbeg(self):
        return self.pgbeg

    def getpgend(self):
        return self.pgend
