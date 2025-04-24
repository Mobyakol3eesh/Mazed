


class Component():
    def __init__(self, name) :
        self.name = name
        self.Enabled = True

    
    def enable(self):
        self.Enabled = True
    
    def disable(self):
        self.Enabled = False
        
    def isEnabled(self):
        return self.Enabled
    
    def __str__(self):
        return f"Component Name :  {self.name}"