from core.mscript import MScript
from core.transform import Transform



class RotationScript(MScript):
    def __init__(self, name,):
        super().__init__(name)
        
    
    def start(self):
        self.transform = self.gameObject.getComponent(Transform)
    
    def update(self, deltaTime):
        
        if self.transform:
            rotationSpeed = 90.0
            self.transform.rotateQ(0, deltaTime * rotationSpeed, 0)