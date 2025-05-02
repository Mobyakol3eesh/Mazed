
from MazedEngine.mscript import MScript
from MazedEngine.transform import Transform
from MazedEngine.camera import Camera
import glm


class cameraMovement(MScript):
    def __init__(self, name, inputRef):
        super().__init__(name)
        self.input = inputRef

    def start(self):
        self.camera = self.gameObject.getComponent(Camera)

       
    def update(self, deltaTime):
        x = self.input.getAxis("Horizontal") if self.input.getAxis("Horizontal") else 0.0
        z = self.input.getAxis("Vertical") if self.input.getAxis("Vertical") else 0.0
         
        xdir = self.input.getAxis("MouseX") if self.input.getAxis("MouseX") else 0.0
        ydir = self.input.getAxis("MouseY") if self.input.getAxis("MouseY") else 0.0
        
        transform = self.gameObject.getComponent(Transform)
        moveVector = glm.vec3(x, 0, z)
        if (moveVector.x != 0 and moveVector.z != 0): 
            moveVector = glm.normalize(moveVector)
        
        
        speed = 5.0
        transform.translate(moveVector.x * deltaTime * speed, 0, moveVector.z * speed * deltaTime) 
        transform.rotateQ(ydir * 0.3, xdir * 0.3, 0, local=True)
        print(xdir,ydir)