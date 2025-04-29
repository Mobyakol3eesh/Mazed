

from pyrr import Quaternion, Matrix44
from core.component import Component
import glm

class Transform(Component):
    def __init__(self,x=0,y=0,z=0):
        super().__init__(name="Transform")
        
        self.modelMat = glm.mat4(1.0)
        self.orientation = Quaternion()
        
        self.position = glm.vec3(x, y, z)
        
        
        self.translationMat = glm.mat4(1.0)
        self.scaleMat = glm.mat4(1.0)
        
        self.setPosition(x,y,z)
    
    def setPosition(self, position):
        self.position = glm.vec3(*position)
        self.translationMat = glm.translate(glm.mat4(1.0), self.position)
        self.applyTransform()
        
    def setPosition(self, x,y,z):
        self.position = glm.vec3(x, y, z)
        self.translationMat = glm.translate(glm.mat4(1.0), self.position)
        self.applyTransform()
    
    def translate(self,x , y, z):
        
       self.position += glm.vec3(x,y,z)
       self.translationMat = glm.translate(self.translationMat,glm.vec3(x,y,z))
       self.applyTransform()
        
        
    def scale(self, x, y, z):
        
        self.scaleMat = glm.scale(glm.mat4(1.0),glm.vec3(x,y,z))
        self.applyTransform()
        
    def rotateQ(self, angleX,angleY, angleZ,local=True):
        q = Quaternion.from_eulers(glm.vec3(glm.radians(angleX), glm.radians(angleY), glm.radians(angleZ)))
        if local:
            self.orientation = self.orientation * q
        else:
            self.orientation = q * self.orientation
        
       
        self.applyTransform()
        
    def applyTransform(self):
        rotationMat = Matrix44.from_quaternion(self.orientation)
        rotationMat = glm.mat4(rotationMat)
        
        self.modelMat = self.translationMat * (rotationMat * self.scaleMat)
        
        
    def getModelMatrix(self):
        return self.modelMat
        