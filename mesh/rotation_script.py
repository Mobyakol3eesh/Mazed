from MazedEngine.mscript import MScript
from MazedEngine.transform import Transform



class RotationScript(MScript):
    def __init__(self, name,):
        super().__init__(name)
        
    
    def start(self):
        self.transform = self.gameObject.getComponent(Transform)
     
    def update(self, deltaTime):
        
        if self.transform:
            rotationSpeed = 90
            
            self.transform.rotateQ(0, rotationSpeed * deltaTime, 0)
            