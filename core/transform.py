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
    
    def translate(self,x , y, z):
        
       self.transformMat = glm.translate(self.transformMat, glm.vec3(x, y , z))
       self.applyTransform()
        
        
    def scale(self, x, y, z):
        
        self.transformMat = glm.scale(self.transformMat, glm.vec3(x, y, z))
        self.applyTransform()
        
    def quaternionRotate(self, axis, angle):
        
        
        
        
        if axis == 'x':
            axis = [1, 0, 0]
        elif axis == 'y':
            axis = [0, 1, 0]
        elif axis == 'z':
            axis = [0, 0, 1]
        else:
            raise ValueError(f"Unknown rotation axis: {axis}")
        axis = np.array(axis, dtype=np.float32)
       
        q = Quaternion.from_axis_rotation(axis, angle)
        
        rotation_matrix = Matrix44.from_quaternion(q)
        
       
        rotation_matrix_glm = glm.mat4(*rotation_matrix)  
        
       
        self.transformMat = self.transformMat * rotation_matrix_glm 
        self.applyTransform()
        
    def applyTransform(self):
        self.shader.use_uniform("transform",self.transformMat, 'mat4')
        