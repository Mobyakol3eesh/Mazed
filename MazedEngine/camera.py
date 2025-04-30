


from MazedEngine.component import Component
from MazedEngine.transform import Transform
from pyrr import Quaternion, Matrix44
import glm


class Camera(Component):
    def __init__(self, name, near , far, fov, aspect,cameraForward=glm.vec3(0, 0, -1)):
      
        super().__init__(name)
        self.near = near
        self.far = far
        self.fov = fov
        self.aspect = aspect
        self.projection = glm.perspective(glm.radians(self.fov), self.aspect, self.near, self.far)
        self.cameraForward = cameraForward
        self.gameObject = None
        self.cameraPosition = glm.vec3(0, 0, 0)
        self.view = None
        self.orietation = Quaternion()
        
        
    def start(self):
        self.cameraPosition = self.gameObject.getComponent(Transform).position 
        self.updateViewMatrix()
    
    def update(self,deltaTime):
        if self.cameraPosition != self.gameObject.getComponent(Transform).position:
            self.cameraPosition = self.gameObject.getComponent(Transform).position
        
        #will apply rotation to the camera
        
        self.updateViewMatrix()
        
        
    def updateViewMatrix(self):
        self.view = glm.lookAt(
            self.cameraPosition,  
            self.cameraPosition + self.cameraForward,  
            glm.vec3(0, 1, 0)   
        )
    
        
        