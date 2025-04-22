

from pyrr import Quaternion, Matrix44
from core.component import Component
import glm

class Transform(Component):
    def __init__(self,shader):
        super().__init__(name="Transform")
        self.transformMat = glm.mat4(1.0)
        self.shader = shader
        self.orientation = Quaternion()
        self.position = glm.vec3(0, 0, 0)
        self.scaleVec = glm.vec3(1, 1, 1)
        
    
    def translate(self,x , y, z):
        
       self.position += glm.vec3(x, y, z)
       self.applyTransform()
        
        
    def scale(self, x, y, z):
        
        self.scaleVec = glm.vec3(x, y, z)
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
        self.transformMat = glm.translate(glm.mat4(1.0),self.position) * (rotationMat * glm.scale(glm.mat4(1.0),self.scaleVec))
        
        
        self.shader.use_uniform("transform",self.transformMat, 'mat4')
        