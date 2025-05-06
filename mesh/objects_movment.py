

from MazedEngine.mscript import MScript
from MazedEngine.transform import Transform

import glm

class objectMovement(MScript):
    def __init__(self, name, inputRef):
        super().__init__(name)
        self.input = inputRef

    def start(self):
        self.transform = self.gameObject.getComponent(Transform)
        
    def update(self, deltaTime): 
        x = self.input.getAxis("Horizontal") if self.input.getAxis("Horizontal") else 0.0
        z = self.input.getAxis("Vertical") if self.input.getAxis("Vertical") else 0.0
        if x == 0 and z == 0:
            print(self.transform.position)

        moveVector = glm.vec3(x, 0, z)
        if (moveVector.x != 0 and moveVector.z != 0): 
            moveVector = glm.normalize(moveVector)
        
        speed = 100.0
        self.transform.translate(moveVector.x * deltaTime * speed, 0, moveVector.z * speed * deltaTime,local= False)
     