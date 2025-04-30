



from abc import abstractmethod
from MazedEngine.component import Component

class MScript(Component):
    
    def __init__(self,name):
        self.name = name
        self.gameObject = None
    
    @abstractmethod
    def update(self, deltaTime):
        pass    
    @abstractmethod
    def start(self):
        pass
    
    def getGameObject(self):
        return self.gameObject
    