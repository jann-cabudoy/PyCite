from Citation import Citation

class JournalCitation(Citation):
    """description of class"""
   
    #Args passed into class are StringVar, so must use .get() to get an actual string
    def __init__(self, authlast, authfirst, title, pubyear, issue, jname, volume):
        Citation.__init__(self, authlast, authfirst, title, pubyear)
        self.issue = issue.get()
        self.jname = jname.get()
        self.volume = volume.get()

    def generatecitation(self):
        citation_string = self.authlast + ", "+ self.authfirst[0:1] + ". " + "(" + self.pubyear + ")." + self.title + "." + self.jname + ", " + self.volume + "(" + self.issue + ")." + "\n" + "\n"
        return citation_string
