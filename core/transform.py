import numpy as np
from numpy import *
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
        matrix44 = Matrix44.from_quaternion(self.orientation)
        self.transformMat = glm.mat4(matrix44) * self.transformMat
        self.applyTransform()
        
    def rotateQX(self, angle):
        q = Quaternion.from_eulers(glm.vec3(glm.radians(angle), 0, 0))
        self.orientation *= q
        matrix44 = Matrix44.from_quaternion(self.orientation)
        self.transformMat = glm.mat4(matrix44) * self.transformMat
        self.applyTransform()

    def rotateQY(self, angle):
        q = Quaternion.from_eulers(glm.vec3(0, glm.radians(angle), 0))
        self.orientation *= q
        matrix44 = Matrix44.from_quaternion(self.orientation)
        self.transformMat = glm.mat4(matrix44) * self.transformMat
        self.applyTransform()

    def rotateQZ(self, angle):
        q = Quaternion.from_eulers(glm.vec3(0, 0, glm.radians(angle)))
        self.orientation *= q
        matrix44 = Matrix44.from_quaternion(self.orientation)
        self.transformMat = glm.mat4(matrix44) * self.transformMat
        self.applyTransform()
  
    def applyTransform(self):
        self.shader.use_uniform("transform",self.transformMat, 'mat4')
        