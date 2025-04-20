from OpenGL.GL import *
from core.opengl_buffers import openGLBuffer
from core.opengl_utilities import OpenGLUtilities
from mesh.shader import Shader

vertices = [
    [-0.5,  -0.5, 0.0,   0.0, 1, 0.0],
     
    [0.0, 0.5, 0.0,      1,0.0, 0.0],
    
    
    [0.5, -0.5, 0.0,      0.0, 0.0, 1.0]
    
   
        ]

indices = [
    0,1,2,
    
]


class Triangle():
    def __init__(self, shaderName='triangle_shader', vertices=vertices, indices=indices,rgb=True):
        self.vertices = vertices
        self.indices = indices
        self.shader = Shader(shaderName)
        
        
        
        self.glBuffer = openGLBuffer(vectorSize=3,stride=self.vertices[0].__len__())
        self.glBuffer.createVertexBuff(self.vertices,vertexAttrIndex=0)
        self.glBuffer.createIndexBuffer(self.indices,vertexAttrIndex=0)
    
        
        

        
        




