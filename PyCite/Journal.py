from Citation import Citation

class JournalCitation(Citation):
    """description of class"""
   
    #Args passed into class are StringVar, so must use .get() to get an actual string
    def __init__(self, authlast, authfirst, title, pubyear, issue, jname, volume):
        Citation.__init__(self, authlast, authfirst, title, pubyear)
        self.issue = issue.get()
        self.jname = jname.get()
        self.volume = volume.get()

    def getissue(self):
        return self.issue

    def getjname(self):
        return self.jname

    def getpgbeg(self):
        return self.pgbeg

    def getpgend(self):
        return self.pgend

    def generatecitation(self):
        citation_string = authlast + ", "+ authfirst[0:1] + ". " + "(" + pubyear + ")." + title + "." + jname + ", " + volume + "(" + issue + ")." + "\n"
        return
