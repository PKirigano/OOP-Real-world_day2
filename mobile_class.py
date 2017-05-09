class mobile(object):
    
    #constructor
    def __init__(self, OS, isSmart=True, browser):
        self.os = os
        self.isSmart = isSmart
        self.browser = browser

    #accesser methods (getters)
    def getOS(self):
        return self.os

    def getisSmart(self):
        return self.isSmart

    def getbrowser(self):
        return self.browser
    
    #Mutator methods (setters)
    def setOS(self, OperatingSy):
        self.os = OperatingSy

    def setisSmart(self, isSmart):
        self.isSmart = isSmart
    
    def setbrowser(self, browser):
        self.browser = browser

class sumsang(mobile):
    
    def __init__(self, OS, isSmart=True, browser, isTracked=True):
        super().__init__(OS, isSmart=True, browser)
        self.isTracked = isTracked

    def track(self):
        return "tracking"