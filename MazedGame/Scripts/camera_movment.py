
from MazedEngine.mscript import MScript
from MazedEngine.transform import Transform
from MazedEngine.camera import Camera
import glm
import pyrr

class cameraMovement(MScript):
    def __init__(self, name, inputRef):
        super().__init__(name)
        self.input = inputRef
        self.pitch = 0.0
        self.yaw = 0.0

    def start(self):
        self.camera = self.gameObject.getComponent(Camera)

       
    def update(self, deltaTime):
        x = self.input.getAxis("Horizontal") if self.input.getAxis("Horizontal") else 0.0
        z = self.input.getAxis("Vertical") if self.input.getAxis("Vertical") else 0.0
        
        xdir = self.input.getAxis("MouseX") if self.input.getAxis("MouseX") else 0.0
        ydir = self.input.getAxis("MouseY") if self.input.getAxis("MouseY") else 0.0
        self.pitch += ydir * 0.5
        self.yaw += xdir * 0.5
        self.yaw = glm.clamp(self.yaw, -40.0, 40.0)
        self.pitch = glm.clamp(self.pitch, -30.0, 40.0)
      
      
        transform = self.gameObject.getComponent(Transform)
        moveVector = glm.vec3(x, 0, z)
        if (moveVector.x != 0 and moveVector.z != 0): 
            moveVector = glm.normalize(moveVector)
       
        speed = 200.0
        forward = transform.forward
        transform.forward = glm.vec3(forward.x, 0, forward.z)
        transform.translate(moveVector.x * deltaTime * speed, 0, moveVector.z * speed * deltaTime) 
        if self.pitch <= -30.0 or self.pitch >= 40.0:
      
            transform.rotateQ(0, xdir * 0.5, 0,fps=True)
         
        
        else:
            transform.rotateQ(ydir * 0.5, xdir * 0.5, 0,fps=False)
        if self.yaw <= -40.0 or self.yaw >= 40.0:
            transform.rotateQ(ydir * 0.5, 0, 0,fps=True)
        else:
            transform.rotateQ(0, xdir * 0.5, 0,fps=True)
        print(transform.position)
        
        
        