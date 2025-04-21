

from pyrr import Quaternion, Matrix44
from core.component import Component
import glm

class Transform(Component):
    def __init__(self,shader):
        super().__init__(name="Transform")
        self.transformMat = glm.mat4(1.0)
        self.shader = shader
        self.orientation = Quaternion()
    
    def translate(self,x , y, z):
        
       self.transformMat = glm.translate(self.transformMat, glm.vec3(x, y , z))
       self.applyTransform()
        
        
    def scale(self, x, y, z):
        
        self.transformMat = glm.scale(self.transformMat, glm.vec3(x, y, z))
        self.applyTransform()
        
    def rotateQLocal(self, angleX,angleY, angleZ):
        q = Quaternion.from_eulers(glm.vec3(glm.radians(angleX), glm.radians(angleY), glm.radians(angleZ)))
        self.orientation = self.orientation * q
        matrix44 = Matrix44.from_quaternion(self.orientation)
        self.transformMat = glm.mat4(matrix44) 
        self.applyTransform()
        
    def rotateQGlobal(self, angleX,angleY, angleZ):
        q = Quaternion.from_eulers(glm.vec3(glm.radians(angleX), glm.radians(angleY), glm.radians(angleZ)))
        self.orientation = q * self.orientation
        matrix44 = Matrix44.from_quaternion(self.orientation)
        self.transformMat = glm.mat4(matrix44) 
        self.applyTransform()
    
    def applyTransform(self):
        self.shader.use_uniform("transform",self.transformMat, 'mat4')
        