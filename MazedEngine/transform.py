

from pyrr import Quaternion, Matrix44
from MazedEngine.component import Component
import pyrr
import glm

class Transform(Component):
    def __init__(self,x=0,y=0,z=0):
        super().__init__(name="Transform")
        
        self.modelMat = glm.mat4(1.0)
        self.orientation = Quaternion()
        
        self.position = glm.vec3(x, y, z)
        self.forward =  glm.vec3(0, 0, 1)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        
        self.baseUp = glm.vec3(0, 1, 0)
        self.baseRight = glm.vec3(1, 0, 0)
        self.baseForward = glm.vec3(0, 0, 1)
        
        self.translationMat = glm.mat4(1.0)
        self.scaleMat = glm.mat4(1.0)
        self.up = glm.vec3(0, 1, 0)
        self.setPosition(x,y,z)
    
    # def setPosition(self, position):
    #     self.position = glm.vec3(*position)
    #     self.translationMat = glm.translate(glm.mat4(1.0), self.position)
    #     self.applyTransform()

    def setPosition(self, x,y,z):
        self.position = glm.vec3(x, y, z)
        self.translationMat = glm.translate(glm.mat4(1.0), self.position)
        self.applyTransform()
    
    def translate(self,x , y, z):
        
        right = glm.normalize(glm.cross(self.forward, self.up))
        up = glm.normalize(glm.cross(right, self.forward))
        move = right * x + up * y + self.forward * z
        self.position += move
        self.translationMat = glm.translate(glm.mat4(1.0), self.position)
       
        self.applyTransform()
        
        
    def scale(self, x, y, z):
        
        self.scaleMat = glm.scale(glm.mat4(1.0),glm.vec3(x,y,z))
        self.applyTransform()
        
    def rotateQ(self, angleX,angleY, angleZ,local=True):
        
        
        
        qX = Quaternion.from_axis_rotation(self.baseRight, glm.radians(angleX))  
        qY = Quaternion.from_axis_rotation(self.baseUp, glm.radians(angleY))     
        qZ = Quaternion.from_axis_rotation(self.baseForward, glm.radians(angleZ))
        
        if local:
            self.orientation = self.orientation * qY * qX * qZ
            
        else:
            self.orientation = qY * qX * qZ * self.orientation
        
        
        
        self.right = pyrr.quaternion.apply_to_vector(self.orientation, self.baseRight)
        self.up = pyrr.quaternion.apply_to_vector(self.orientation, self.baseUp)
        self.forward = pyrr.quaternion.apply_to_vector(self.orientation, self.baseForward)
        
        
        
        
        
        
        self.right = glm.normalize(self.right)
        self.right = glm.vec3(self.right.x, self.right.y, self.right.z)
        self.up = glm.normalize(self.up)
        self.up = glm.vec3(self.up.x, self.up.y, self.up.z)
        self.forward = glm.normalize(self.forward)
        self.forward = glm.vec3(self.forward.x, self.forward.y, self.forward.z)
        
        self.applyTransform()
      

    def matFromQ(self):
        rotationMat = Matrix44.from_quaternion(self.orientation)
        rotationMat = glm.mat4(rotationMat)
        return rotationMat
    def applyTransform(self):
        rotationMat = self.matFromQ()
        
        self.modelMat =  (self.translationMat  * (rotationMat * self.scaleMat))
        
        
    def getModelMatrix(self):
        return self.modelMat
        