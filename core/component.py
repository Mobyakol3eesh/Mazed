


class Component:
    def __init__(self, name) :
        self.name = name
        self.gameObject = None
        self.Enabled = True

    
    
    def setGameObject(self, gameObject):
        self.gameObject = gameObject
    
    
    def enable(self):
        self.Enabled = True
    
    def disable(self):
        self.Enabled = False
        
    def isEnabled(self):
        return self.Enabled
    
    