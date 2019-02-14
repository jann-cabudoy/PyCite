class Citation(object):
    """description of class"""
    #Args passed into class are StringVar, so must use .get() to get an actual string
    def __init__(self, authlast, authfirst, title, pubyear):
        self.authlast = authlast.get()
        self.authfirst = authfirst.get()
        self.title = title.get()
        self.pubyear = pubyear.get()

    def getauthlast(self):
        return self.authlast

    def getauthfirst(self):
        return self.authfirst

    def gettitle(self):
        return self.title
    
    def getpubyear(self):
        return self.pubyear

    def generatecitation(self):
        return


