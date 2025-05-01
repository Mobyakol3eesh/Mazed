


from MazedEngine.component import Component
from MazedEngine.transform import Transform
from pyrr import Quaternion, Matrix44
import glm


class Camera(Component):
    def __init__(self, name, near , far, fov, aspect):
      
        super().__init__(name)
        self.near = near
        self.far = far
        self.fov = fov
        self.aspect = aspect
        self.projection = glm.perspective(glm.radians(self.fov), self.aspect, self.near, self.far)
        self.cameraForward = glm.vec3(0, 0, -1)
        self.gameObject = None
        self.cameraPosition = glm.vec3(0, 0, 0)
        self.up = glm.vec3(0, 1, 0)
        self.view = None
        self.orietation = Quaternion()
        self.rotationMat = glm.mat4(1.0)
        
    def start(self):
        self.cameraPosition = self.gameObject.getComponent(Transform).position
        self.gameObject.getComponent(Transform).forward = self.cameraForward
        self.gameObject.getComponent(Transform).baseForward = self.cameraForward
        self.gameObject.getComponent(Transform).up = self.up
        self.updateViewMatrix()
    
    def update(self,deltaTime):
        if self.cameraPosition != self.gameObject.getComponent(Transform).position:
            self.cameraPosition = self.gameObject.getComponent(Transform).position
        if self.cameraForward != self.gameObject.getComponent(Transform).forward:
            self.cameraForward = self.gameObject.getComponent(Transform).forward
        if self.up != self.gameObject.getComponent(Transform).up:
            self.up = self.gameObject.getComponent(Transform).up
        # if self.orietation != self.gameObject.getComponent(Transform).orientation:
        #     self.orietation = self.gameObject.getComponent(Transform).orientation
        # self.rotationMat = self.gameObject.getComponent(Transform).matFromQ()
        
        
        self.updateViewMatrix()
        
        
    def updateViewMatrix(self):
        self.view = glm.lookAt(
            self.cameraPosition,  
            self.cameraPosition + self.cameraForward,  
            glm.vec3(0, 1, 0)   
        )
            
        
        