from core.mscript import MScript
from core.transform import Transform



class RotationScript(MScript):
    def __init__(self, name, rotationSpeed=90.0):
        super().__init__(name)
        self.rotationSpeed = rotationSpeed
        self.transform = None
    
    def start(self):
        self.transform = self.gameObject.getComponent(Transform)
    
    def update(self, deltaTime):
        print(f"RotationScript: {self.name} updating with deltaTime: {deltaTime}")
        if self.transform:
            self.transform.rotateQ(0, deltaTime * self.rotationSpeed, 0)